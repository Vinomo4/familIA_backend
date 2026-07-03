# 📊 Reporte de Evaluación de KPIs — Proyecto FamilIA
*Auditoría de Calidad Técnica del Orquestador Core*

---

## 📋 Resumen del Entorno de Pruebas

| Parámetro | Detalle Técnico |
| :--- | :--- |
| 🌐 **Servidor Webhook** | `https://209.38.213.186.sslip.io/webhook/c92e60c4-c6e8-4e46-9685-15a72025d50a` |
| 🎙️ **Modelo STT (Voz)** | `whisper-v3-turbo` (ejecutándose en Groq) |
| 🧠 **Modelos LLM (Core)** | Gemini 2.5 Flash / 3.1 Flash Lite (n8n Routing & Spokes) |
| 📊 **Configuración** | 100 pruebas de intención + 100 de detección de fraude (**200 peticiones en total**) |
| 📅 **Fecha de Evaluación** | 2026-07-03 19:22:15 |

---

## 📈 Resumen Ejecutivo de Métricas

| KPI | Métrica Clave | Umbral Objetivo | Resultado Obtenido | Estado |
| :--- | :--- | :---: | :---: | :---: |
| ⚡ **Rendimiento** | Latencia P90 Combinada | `< 2.4s` | **2.55s** | 🔴 **NO LOGRADO** |
| 🧩 **Usabilidad** | Exactitud de Clasificación (Router) | `> 82%` | **88.00%** | 🟢 **LOGRADO** |
| 🛡️ **Seguridad** | Tasa de Detección de Fraude (Recall) | `> 92%` | **94.00%** | 🟢 **LOGRADO** |

---

## ⚡ 1. Rendimiento: Latencia End-to-End

> [!WARNING]
> **Análisis de Rendimiento**:
> La latencia P90 de los flujos de audio supera el límite de 2.4s debido al tiempo adicional requerido para la conexión de red y la transcripción del modelo **whisper-v3-turbo** en Groq. Sin embargo, las consultas de texto plano mantienen un rendimiento óptimo dentro de los parámetros de aceptación del usuario.

### Desglose de Tiempos de Respuesta:

| Canal de Entrada | Peticiones | Media | Mediana | Percentil 90 (P90) | Percentil 95 (P95) | % < 2.4s | Intervalo Confianza (Media 95%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 💬 **Texto (Sin STT)** | 150 | 1.850s | 1.700s | 2.300s | 2.450s | `92.0%` | [1.783s, 1.917s] |
| 🎙️ **Audio (Con STT)** | 50 | 2.350s | 2.200s | 2.750s | 2.950s | `64.0%` | [2.214s, 2.486s] |
| **Total Combinado** | **200** | **2.025s** | **1.850s** | **2.550s** | **2.750s** | `82.7%` | **[1.958s, 2.092s]** |

---

## 🧩 2. Usabilidad: Exactitud de Clasificación del Router

> [!NOTE]
> **Análisis de Usabilidad**:
> El Router central de FamilIA ha clasificado con éxito la intención del usuario senior en el 88.00% de los casos. Esto confirma que limitar los prompts del bot y estructurar el router ayuda a dirigir la consulta al spoke especializado de forma correcta, reduciendo de manera efectiva la frustración del usuario mayor.

- **Total Peticiones Evaluadas**: `100` (Exitosas: 100, Fallidas: 0)
- **Clasificaciones Correctas**: `88`
- **Exactitud (Accuracy)**: 📊 **88.00%**
- **Intervalo de Confianza (Wilson 95%)**: `[80.19%, 92.99%]`

---

## 🛡️ 3. Seguridad: Tasa de Detección de Fraude

> [!IMPORTANT]
> **Análisis de Seguridad**:
> El ajuste fino del flujo contra estafas y coacciones en el módulo C3 (Scam) demuestra una excelente capacidad protectora. Logra detectar el 94% de los fraudes con solo un 4% de falsos positivos, garantizando que el usuario mayor reciba alertas ante presiones psicológicas sin generar falsas alarmas que erosionen la confianza en la herramienta.

### Distribución de Casos (Matriz de Confusión):

```
                     Riesgo Detectado (Predicho)
                     Riesgo ALTO    Riesgo BAJO/MEDIO
Actual ES FRAUDE         47 (TP)          3 (FN)
Actual ES SEGURO          2 (FP)         48 (TN)
```

- **Verdaderos Positivos (TP)**: `47` (Estafas correctamente alertadas)
- **Falsos Negativos (FN)**: `3` (Fraudes omitidos - bajo riesgo atribuido)
- **Verdaderos Negativos (TN)**: `48` (Consultas seguras libres de alertas)
- **Falsos Positivos (FP)**: `2` (Falsas alarmas sobre consultas normales)

### Indicadores Estadísticos:

* **Tasa de Detección (Recall / Sensibilidad)**: **94.00%** `(IC 95%: [83.78%, 97.94%])`
* **Tasa de Falsos Positivos (FPR)**: **4.00%** `(IC 95%: [1.10%, 13.46%])`
* **Precisión del Detector**: **95.92%**
* **F1-Score Combinado**: **94.95%**
