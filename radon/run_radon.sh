#!/bin/bash

# Putanja do rich projekta
RICH_DIR="$HOME/Desktop/rich"

# Apsolutna putanja do foldera sa skriptom (pre cd)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RESULTS_DIR="$SCRIPT_DIR/results"

mkdir -p "$RESULTS_DIR"

cd "$RICH_DIR"

echo "========================================="
echo "Running Radon code complexity analysis"
echo "========================================="
echo ""

REPORT="$RESULTS_DIR/complexity.txt"

{
  echo "========================================="
  echo "CYCLOMATIC COMPLEXITY (radon cc -a -s)"
  echo "========================================="
  radon cc rich/ -a -s
  echo ""
  echo "========================================="
  echo "MAINTAINABILITY INDEX (radon mi -s)"
  echo "========================================="
  radon mi rich/ -s
  echo ""
  echo "========================================="
  echo "RAW METRICS (radon raw -s)"
  echo "========================================="
  radon raw rich/ -s
} 2>&1 | tee "$REPORT"

echo ""
echo "========================================="
echo "Radon complete!"
echo "========================================="
echo ""
echo "Report saved to:"
echo "   - radon/results/complexity.txt"