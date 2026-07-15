#!/bin/bash

# Putanja do rich projekta
RICH_DIR="$(cd "$(dirname "$0")/../rich" && pwd)"

# Apsolutna putanja do foldera sa skriptom (pre cd)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RESULTS_DIR="$SCRIPT_DIR/results"

mkdir -p "$RESULTS_DIR"

cd "$RICH_DIR"

echo "========================================="
echo "Running MyPy type checking"
echo "========================================="
echo ""
echo "Running mypy..."
mypy rich/ \
  --ignore-missing-imports \
  --html-report "$RESULTS_DIR" \
  --txt-report "$RESULTS_DIR" \
  2>&1 | tee "$RESULTS_DIR/report.txt"
echo ""
echo "========================================="
echo "MyPy complete!"
echo "========================================="
echo ""
echo "Reports saved to:"
echo "   - mypy/results/report.txt   (terminalski izlaz)"
echo "   - mypy/results/index.txt    (tabela po modulima)"
echo "   - mypy/results/index.html   (HTML izvestaj)"