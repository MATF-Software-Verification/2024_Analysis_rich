#!/bin/bash


RICH_DIR="$(cd "$(dirname "$0")/../rich" && pwd)"


SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RESULTS_DIR="$SCRIPT_DIR/results"

mkdir -p "$RESULTS_DIR"

cd "$RICH_DIR"

echo "========================================="
echo "Running Pylint static analysis"
echo "========================================="
echo ""
echo "Running pylint..."
pylint rich/ --output-format=text --reports=y 2>&1 | tee "$RESULTS_DIR/report.txt"
echo ""
echo "========================================="
echo "Pylint complete!"
echo "========================================="
echo ""
echo "Report saved to:"
echo "   - pylint/results/report.txt"