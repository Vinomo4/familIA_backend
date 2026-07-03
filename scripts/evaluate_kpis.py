import os
import csv
import json
import time
import math
import random
import argparse
import wave
import io
import requests

# Set seed for reproducible sampling
random.seed(42)

def generate_silent_wav(duration_sec=1.5, sample_rate=16000):
    """Generates a tiny silent WAV file in memory."""
    wav_io = io.BytesIO()
    with wave.open(wav_io, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2) # 16-bit PCM
        wav_file.setframerate(sample_rate)
        # 1.5 seconds * sample_rate * 2 bytes/sample
        num_frames = int(duration_sec * sample_rate)
        wav_file.writeframes(b'\x00' * (num_frames * 2))
    return wav_io.getvalue()

def parse_args():
    parser = argparse.ArgumentParser(description="Evaluar los KPIs de rendimiento, usabilidad y seguridad de FamilIA.")
    parser.add_argument("--webhook-url", type=str, default="https://209.38.213.186.sslip.io/webhook/c92e60c4-c6e8-4e46-9685-15a72025d50a",
                        help="URL del webhook de producción de n8n.")
    parser.add_argument("--sample-size", type=int, default=30,
                        help="Tamaño de muestra a evaluar para cada KPI (1-200). Ignorado si se usa --run-all.")
    parser.add_argument("--run-all", action="store_true",
                        help="Ejecutar la evaluación completa con las 200 muestras de cada dataset.")
    parser.add_argument("--delay", type=float, default=1.5,
                        help="Retraso en segundos entre llamadas para respetar límites de API (default: 1.5s).")
    return parser.parse_args()

def wilson_score_interval(p, n, confidence=0.95):
    """Calculates the Wilson score interval for a binomial proportion."""
    if n == 0:
        return 0.0, 0.0
    z = 1.96  # 95% confidence level
    denominator = 1 + z**2 / n
    centre_adjusted_probability = p + z**2 / (2 * n)
    adjusted_variance = math.sqrt((p * (1 - p) + z**2 / (4 * n)) / n)
    lower = (centre_adjusted_probability - z * adjusted_variance) / denominator
    upper = (centre_adjusted_probability + z * adjusted_variance) / denominator
    return max(0.0, lower), min(1.0, upper)

def calculate_latency_stats(latencies):
    if not latencies:
        return {}
    latencies.sort()
    n = len(latencies)
    mean_lat = sum(latencies) / n
    median_lat = latencies[n // 2] if n % 2 != 0 else (latencies[n // 2 - 1] + latencies[n // 2]) / 2
    
    # Percentiles
    p90_idx = max(0, min(n - 1, int(n * 0.90)))
    p95_idx = max(0, min(n - 1, int(n * 0.95)))
    p90 = latencies[p90_idx]
    p95 = latencies[p95_idx]
    
    under_threshold = sum(1 for l in latencies if l < 2.4)
    pct_under_threshold = (under_threshold / n) * 100
    
    # Confidence Interval for Mean (Normal approximation since n is usually >= 30)
    variance = sum((x - mean_lat) ** 2 for x in latencies) / max(1, n - 1)
    std_dev = math.sqrt(variance)
    std_error = std_dev / math.sqrt(n)
    ci_half = 1.96 * std_error
    ci_lower = max(0.0, mean_lat - ci_half)
    ci_upper = mean_lat + ci_half
    
    return {
        "count": n,
        "mean": mean_lat,
        "median": median_lat,
        "p90": p90,
        "p95": p95,
        "std_dev": std_dev,
        "pct_under_2_4s": pct_under_threshold,
        "ci_95_mean": (ci_lower, ci_upper)
    }

def call_n8n_webhook(url, text, user_id="U001", send_audio=False, timeout=40):
    """Sends a request to the n8n webhook (either as json text or multipart audio)."""
    headers = {}
    start_time = time.time()
    
    try:
        if send_audio:
            # Generate temporary audio of the speech (silence simulation)
            audio_bytes = generate_silent_wav()
            files = {
                'audio': ('audio_kpi_test.wav', audio_bytes, 'audio/wav')
            }
            # If sending audio, the text can be empty or we can pass it as form data
            data = {
                'user_id': user_id,
                'text': text  # The STT is bypassed or combined in main hub
            }
            response = requests.post(url, files=files, data=data, timeout=timeout)
        else:
            headers = {"Content-Type": "application/json"}
            payload = {
                "user_id": user_id,
                "text": text
            }
            response = requests.post(url, json=payload, headers=headers, timeout=timeout)
            
        latency = time.time() - start_time
        
        if response.status_code == 200:
            return response.json(), latency, True
        else:
            return {"error": f"HTTP status {response.status_code}", "body": response.text}, latency, False
    except Exception as e:
        latency = time.time() - start_time
        return {"error": str(e)}, latency, False

def run_evaluation():
    args = parse_args()
    print("=" * 60)
    print("🤖 INICIANDO EVALUACIÓN DE KPIS - FamilIA")
    print(f"Endpoint: {args.webhook_url}")
    
    base_dir = "/home/vinomo/programming/master/data_science_and_ai/familIA/data/synthetic/kpi_testing"
    router_file = os.path.join(base_dir, "router_classification.csv")
    fraud_file = os.path.join(base_dir, "fraud_detection.csv")
    
    if not os.path.exists(router_file) or not os.path.exists(fraud_file):
        print("❌ Error: Datasets no encontrados. Ejecute primero generate_test_data.py.")
        return
        
    # Read datasets
    with open(router_file, 'r', encoding='utf-8') as f:
        router_cases = list(csv.DictReader(f))
    with open(fraud_file, 'r', encoding='utf-8') as f:
        fraud_cases = list(csv.DictReader(f))
        
    # Determine sample size
    router_sample_size = len(router_cases) if args.run_all else min(args.sample_size, len(router_cases))
    fraud_sample_size = len(fraud_cases) if args.run_all else min(args.sample_size, len(fraud_cases))
    
    # Sample cases
    sampled_router = random.sample(router_cases, router_sample_size)
    sampled_fraud = random.sample(fraud_cases, fraud_sample_size)
    
    print(f"Muestras de Clasificación del Router: {router_sample_size}")
    print(f"Muestras de Detección de Fraude: {fraud_sample_size}")
    print(f"Retraso entre peticiones: {args.delay}s")
    print("=" * 60)
    
    # Store all latency measurements
    text_latencies = []
    audio_latencies = []
    all_responses = []
    
    # ----------------------------------------------------
    # PHASE 1: ROUTER CLASSIFICATION ACCURACY & LATENCY
    # ----------------------------------------------------
    print("\n👉 Fase 1: Evaluando Clasificación del Router y Latencia...")
    correct_classifications = 0
    failed_requests_router = 0
    
    # To measure STT latency impact, we send 50% of requests as audio
    audio_count = 0
    
    router_results_log = []
    
    for i, case in enumerate(sampled_router):
        text = case["text"]
        expected = case["expected_category"]
        
        # Decide if this request will be sent as audio
        send_as_audio = (i % 2 == 0)
        if send_as_audio:
            audio_count += 1
            
        print(f"[{i+1}/{router_sample_size}] Evaluando ('{text[:35]}...') -> Esperado: {expected} | Envío: {'Audio' if send_as_audio else 'Texto'}")
        
        res, latency, success = call_n8n_webhook(args.webhook_url, text, send_audio=send_as_audio)
        
        if send_as_audio:
            audio_latencies.append(latency)
        else:
            text_latencies.append(latency)
            
        if not success:
            print(f"  ⚠️ Error en la llamada: {res.get('error')}")
            failed_requests_router += 1
            router_results_log.append({
                "text": text,
                "expected": expected,
                "classified": "ERROR",
                "correct": False,
                "latency": latency,
                "error": res.get("error")
            })
            time.sleep(args.delay)
            continue
            
        # Reconstruct classification from response
        spoke = res.get("spoke", "")
        has_extracted_text = ("texto_extraido" in res or "extracted_text" in res)
        
        # Mapping logic
        classified_category = "UNKNOWN"
        if spoke == "MANAGEMENT":
            classified_category = "MANAGEMENT"
        elif spoke == "C2_INTERFACE":
            classified_category = "INTERFACE"
        elif spoke == "C1_DOCUMENT":
            classified_category = "DOCUMENT"
        elif spoke == "SCAM_DETECTION":
            if has_extracted_text:
                classified_category = "DOCUMENT"
            else:
                classified_category = "SCAM"
                
        is_correct = (classified_category == expected)
        if is_correct:
            correct_classifications += 1
            
        router_results_log.append({
            "text": text,
            "expected": expected,
            "classified": classified_category,
            "correct": is_correct,
            "latency": latency,
            "response": res
        })
        
        print(f"  Resultado: Clasificado como {classified_category} | {'✅ CORRECTO' if is_correct else '❌ INCORRECTO'} | Latencia: {latency:.2f}s")
        time.sleep(args.delay)

    # ----------------------------------------------------
    # PHASE 2: FRAUD DETECTION ACCURACY (SECURITY KPI)
    # ----------------------------------------------------
    print("\n👉 Fase 2: Evaluando Detección de Fraude (Seguridad)...")
    tp, fp, tn, fn = 0, 0, 0, 0
    failed_requests_fraud = 0
    fraud_results_log = []
    
    for i, case in enumerate(sampled_fraud):
        text = case["text"]
        is_fraud = case["is_fraud"] == 'True' or case["is_fraud"] is True
        fraud_type = case["fraud_type"]
        
        # Fraud queries are sent as text
        print(f"[{i+1}/{fraud_sample_size}] Evaluando detector de fraudes: '{text[:35]}...' -> ¿Es Fraude?: {is_fraud}")
        
        res, latency, success = call_n8n_webhook(args.webhook_url, text, send_audio=False)
        text_latencies.append(latency)
        
        if not success:
            print(f"  ⚠️ Error en la llamada: {res.get('error')}")
            failed_requests_fraud += 1
            fraud_results_log.append({
                "text": text,
                "is_fraud": is_fraud,
                "fraud_type": fraud_type,
                "detected": None,
                "correct": False,
                "latency": latency,
                "error": res.get("error")
            })
            time.sleep(args.delay)
            continue
            
        # Determine if fraud was flagged as ALTO risk
        # The scam module returns evaluation.risk_level or evaluation.risk_score
        # Check either directly or under nested evaluation key
        evaluation = res.get("evaluation", {})
        risk_level = evaluation.get("risk_level", "")
        risk_score = evaluation.get("risk_score", 0)
        spoke = res.get("spoke", "")
        
        # If spoke is SCAM_DETECTION and risk level is ALTO, or risk_score >= 75
        is_flagged_as_fraud = (spoke == "SCAM_DETECTION" and (risk_level == "ALTO" or risk_score >= 75))
        
        # If C1 (document analysis) ran, and risk is high, it maps to SCAM_DETECTION spoke with risk >= 75
        if not is_flagged_as_fraud and risk_score >= 75:
            is_flagged_as_fraud = True
            
        if is_fraud:
            if is_flagged_as_fraud:
                tp += 1
                detected_correctly = True
            else:
                fn += 1
                detected_correctly = False
        else:
            if is_flagged_as_fraud:
                fp += 1
                detected_correctly = False
            else:
                tn += 1
                detected_correctly = True
                
        fraud_results_log.append({
            "text": text,
            "is_fraud": is_fraud,
            "fraud_type": fraud_type,
            "detected_as_fraud": is_flagged_as_fraud,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "correct": detected_correctly,
            "latency": latency,
            "response": res
        })
        
        status_msg = "TP (Detector acertó)" if (is_fraud and is_flagged_as_fraud) else \
                     "TN (Control acertó)" if (not is_fraud and not is_flagged_as_fraud) else \
                     "FN (Fraude NO detectado!) 🚨" if (is_fraud and not is_flagged_as_fraud) else \
                     "FP (Falso Positivo!) ⚠️"
                     
        print(f"  Resultado: {status_msg} | Nivel de Riesgo: {risk_level} (Score: {risk_score}) | Latencia: {latency:.2f}s")
        time.sleep(args.delay)

    # ----------------------------------------------------
    # METRIC CALCULATIONS & REPORT GENERATION
    # ----------------------------------------------------
    print("\n" + "=" * 60)
    print("📊 CÁLCULO FINAL DE METRICAS Y ANÁLISIS ESTADÍSTICO")
    print("=" * 60)
    
    # 1. Router Classification metrics
    completed_router = router_sample_size - failed_requests_router
    router_accuracy = (correct_classifications / completed_router) if completed_router > 0 else 0
    router_ci = wilson_score_interval(router_accuracy, completed_router)
    
    # 2. Fraud detection metrics
    completed_fraud = fraud_sample_size - failed_requests_fraud
    recall = (tp / (tp + fn)) if (tp + fn) > 0 else 0
    fpr = (fp / (fp + tn)) if (fp + tn) > 0 else 0
    precision = (tp / (tp + fp)) if (tp + fp) > 0 else 0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0
    
    recall_ci = wilson_score_interval(recall, tp + fn)
    fpr_ci = wilson_score_interval(fpr, fp + tn)
    
    # 3. Latency metrics
    all_latencies = text_latencies + audio_latencies
    overall_stats = calculate_latency_stats(all_latencies)
    text_stats = calculate_latency_stats(text_latencies)
    audio_stats = calculate_latency_stats(audio_latencies)
    
    # Format markdown report
    markdown_report = f"""# Reporte de Evaluación de KPIs - FamilIA

**Fecha de Ejecución**: {time.strftime('%Y-%m-%d %H:%M:%S')}
**Servidor Webhook**: `{args.webhook_url}`
**Configuración**: Muestra de Clasificación = {router_sample_size}, Muestra de Fraude = {fraud_sample_size} (Total peticiones = {router_sample_size + fraud_sample_size})

---

## ⚡ 1. Rendimiento: Latencia End-to-End
*Objetivo de Latencia: Promedio y Percentil 90 < 2.4s (Mitiga el riesgo de abandono)*

| Tipo de Solicitud | Peticiones | Media Latencia | Mediana | Percentil 90 | Percentil 95 | % < 2.4s | Intervalo Confianza (Media 95%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Texto (Sin STT)** | {text_stats.get('count', 0)} | {text_stats.get('mean', 0):.3f}s | {text_stats.get('median', 0):.3f}s | {text_stats.get('p90', 0):.3f}s | {text_stats.get('p95', 0):.3f}s | **{text_stats.get('pct_under_2_4s', 0):.1f}%** | [{text_stats.get('ci_95_mean', (0,0))[0]:.3f}s, {text_stats.get('ci_95_mean', (0,0))[1]:.3f}s] |
| **Audio (Con STT)** | {audio_stats.get('count', 0)} | {audio_stats.get('mean', 0):.3f}s | {audio_stats.get('median', 0):.3f}s | {audio_stats.get('p90', 0):.3f}s | {audio_stats.get('p95', 0):.3f}s | **{audio_stats.get('pct_under_2_4s', 0):.1f}%** | [{audio_stats.get('ci_95_mean', (0,0))[0]:.3f}s, {audio_stats.get('ci_95_mean', (0,0))[1]:.3f}s] |
| **Total Combinado** | {overall_stats.get('count', 0)} | {overall_stats.get('mean', 0):.3f}s | {overall_stats.get('median', 0):.3f}s | {overall_stats.get('p90', 0):.3f}s | {overall_stats.get('p95', 0):.3f}s | **{overall_stats.get('pct_under_2_4s', 0):.1f}%** | [{overall_stats.get('ci_95_mean', (0,0))[0]:.3f}s, {overall_stats.get('ci_95_mean', (0,0))[1]:.3f}s] |

> [!NOTE]
> La latencia de audio incluye el paso de transcripción de voz a texto (STT) utilizando el modelo **whisper-v3-turbo** en Groq y su enrutamiento en n8n.
> **Estado del Objetivo**: {'✅ LOGRADO' if overall_stats.get('p90', 9.9) < 2.4 else '❌ NO LOGRADO'} (Percentil 90 Combinado = {overall_stats.get('p90', 0):.2f}s)

---

## 🧩 2. Usabilidad: Exactitud de Clasificación del Router
*Objetivo de Usabilidad: Exactitud (Accuracy) > 82% (Clasificación correcta del flujo)*

- **Peticiones Completadas**: {completed_router} (Fallidas: {failed_requests_router})
- **Clasificaciones Correctas**: {correct_classifications}
- **Exactitud (Accuracy)**: **{router_accuracy * 100:.2f}%**
- **Intervalo de Confianza (Wilson 95%)**: **[{router_ci[0]*100:.2f}%, {router_ci[1]*100:.2f}%]**

> **Estado del Objetivo**: {'✅ LOGRADO' if router_accuracy > 0.82 else '❌ NO LOGRADO'} (Objetivo > 82%)

---

## 🛡️ 3. Seguridad: Tasa de Detección de Fraude
*Objetivo de Seguridad: Tasa de Detección (Recall) > 92% (Protección contra estafas y manipulación)*

### Matriz de Confusión Virtual:
- **Verdaderos Positivos (TP)**: {tp} (Estafas correctamente detectadas)
- **Falsos Negativos (FN)**: {fn} (Estafas no detectadas / omitidas)
- **Verdaderos Negativos (TN)**: {tn} (Mensajes seguros correctamente clasificados)
- **Falsos Positivos (FP)**: {fp} (Falsas alarmas sobre mensajes seguros)

### Métricas de Seguridad Calculadas:
- **Tasa de Detección de Fraude (Recall / Sensibilidad)**: **{recall * 100:.2f}%**
  - *Intervalo de Confianza (Wilson 95%)*: [{recall_ci[0]*100:.2f}%, {recall_ci[1]*100:.2f}%]
- **Tasa de Falsos Positivos (FPR / Falsas Alarmas)**: **{fpr * 100:.2f}%**
  - *Intervalo de Confianza (Wilson 95%)*: [{fpr_ci[0]*100:.2f}%, {fpr_ci[1]*100:.2f}%]
- **Precisión del Detector**: **{precision * 100:.2f}%**
- **F1-Score Combinado**: **{f1 * 100:.2f}%**

> **Estado del Objetivo**: {'✅ LOGRADO' if recall > 0.92 else '❌ NO LOGRADO'} (Objetivo > 92%)
"""

    print(markdown_report)
    
    # Save detailed JSON report
    report_data = {
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
        "webhook_url": args.webhook_url,
        "sample_sizes": {
            "router_requested": router_sample_size,
            "router_completed": completed_router,
            "router_failed": failed_requests_router,
            "fraud_requested": fraud_sample_size,
            "fraud_completed": completed_fraud,
            "fraud_failed": failed_requests_fraud
        },
        "performance_latency": {
            "overall": overall_stats,
            "text_only": text_stats,
            "audio_only": audio_stats
        },
        "usability_classification": {
            "accuracy": router_accuracy,
            "correct": correct_classifications,
            "total": completed_router,
            "ci_95": router_ci
        },
        "security_fraud_detection": {
            "confusion_matrix": {
                "tp": tp,
                "fn": fn,
                "tn": tn,
                "fp": fp
            },
            "metrics": {
                "recall": recall,
                "fpr": fpr,
                "precision": precision,
                "f1_score": f1
            },
            "ci_95": {
                "recall": recall_ci,
                "fpr": fpr_ci
            }
        },
        "logs": {
            "router_evaluations": router_results_log,
            "fraud_evaluations": fraud_results_log
        }
    }
    
    # Serialize tuples for JSON
    def serialize_tuples(obj):
        if isinstance(obj, tuple):
            return list(obj)
        elif isinstance(obj, dict):
            return {k: serialize_tuples(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [serialize_tuples(i) for i in obj]
        return obj
        
    serialized_report = serialize_tuples(report_data)
    
    results_file = "/home/vinomo/programming/master/data_science_and_ai/familIA/data/kpi_evaluation_results.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(serialized_report, f, indent=2, ensure_ascii=False)
        
    print(f"Reporte detallado guardado en {results_file}")
    
    # Write the markdown report to a file in the workspace for easy user access
    report_md_file = "/home/vinomo/programming/master/data_science_and_ai/familIA/data/kpi_evaluation_report.md"
    with open(report_md_file, 'w', encoding='utf-8') as f:
        f.write(markdown_report)
    print(f"Reporte Markdown guardado en {report_md_file}")

if __name__ == "__main__":
    run_evaluation()
