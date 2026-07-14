#!/bin/bash


RICH_DIR="$HOME/Desktop/rich"


SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RESULTS_DIR="$SCRIPT_DIR/results"

mkdir -p "$RESULTS_DIR"

cd "$RICH_DIR"

echo "========================================="
echo "Running Vulture dead code analysis"
echo "========================================="
echo ""
echo "Running vulture..."
vulture rich/ --min-confidence 60 2>&1 | tee "$RESULTS_DIR/report.txt"
echo ""
echo "========================================="
echo "Vulture complete!"
echo "========================================="
echo ""
echo "Report saved to:"
echo "   - vulture/results/report.txt"