#!/bin/bash


RICH_DIR="$HOME/Desktop/rich"


SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RESULTS_DIR="$SCRIPT_DIR/results"

mkdir -p "$RESULTS_DIR"

cd "$RICH_DIR"

echo "========================================="
echo "Running Interrogate docstring coverage"
echo "========================================="
echo ""
echo "Running interrogate..."
interrogate rich/ -v 2>&1 | tee "$RESULTS_DIR/report.txt"
echo ""
echo "========================================="
echo "Interrogate complete!"
echo "========================================="
echo ""
echo "Report saved to:"
echo "   - interrogate/results/report.txt"