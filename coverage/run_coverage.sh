#!/bin/bash

# Putanje do projekta i test foldera
RICH_DIR="$HOME/Desktop/rich"
NEW_TESTS="$HOME/Desktop/2024_Analysis_rich/tests"

# Apsolutna putanja do foldera sa skriptom (pre cd)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RESULTS_DIR="$SCRIPT_DIR/results"

mkdir -p "$RESULTS_DIR"

cd "$RICH_DIR"

echo "========================================="
echo "Running Coverage (original + new tests)"
echo "========================================="
echo ""
echo "Running tests with coverage..."
pytest tests/ "$NEW_TESTS" \
  --cov=rich \
  --cov-report=term \
  2>&1 | tee "$RESULTS_DIR/report.txt"
echo ""
echo "========================================="
echo "Coverage complete!"
echo "========================================="
echo ""
echo "Report saved to:"
echo "   - coverage/results/report.txt"
