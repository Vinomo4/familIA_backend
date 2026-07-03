#!/bin/bash

# Exit on error
set -e

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
WORKSPACE_DIR="$( cd "$SCRIPT_DIR/.." &> /dev/null && pwd )"

cd "$WORKSPACE_DIR"

echo "========================================================================"
echo "🚀 INICIANDO PIPELINE DE EVALUACIÓN DE KPIS - FamilIA"
echo "========================================================================"

# 1. Activate virtual environment
if [ -d ".venv" ]; then
    echo "📦 Activando entorno virtual (.venv)..."
    source .venv/bin/activate
else
    echo "⚠️ Entorno virtual .venv no encontrado. Asegúrese de tener las dependencias instaladas."
fi

# 2. Generate synthetic data if not already present or if forced
echo "📝 Generando datasets sintéticos..."
python3 scripts/generate_test_data.py

# 3. Run evaluation
# Default to sample-size of 30 for quick execution, allow overrides
SAMPLE_SIZE=${1:-30}

if [ "$SAMPLE_SIZE" == "all" ]; then
    echo "📊 Ejecutando evaluación completa con las 200 muestras..."
    python3 scripts/evaluate_kpis.py --run-all
else
    echo "📊 Ejecutando evaluación con tamaño de muestra = $SAMPLE_SIZE..."
    python3 scripts/evaluate_kpis.py --sample-size "$SAMPLE_SIZE"
fi

echo "========================================================================"
echo "✅ PIPELINE COMPLETADO EXITOSAMENTE"
echo "========================================================================"
