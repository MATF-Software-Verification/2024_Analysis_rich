#!/bin/bash

cd "$(dirname "$0")/.."


mkdir -p pytest/results

echo "========================================="
echo "Running Pytest unit tests with coverage"
echo "========================================="


pytest tests/ \
    --cov=rich.json \
    --cov-report=term \
    --cov-report=html:pytest/results/html \
    -v 2>&1 | tee pytest/results/report.txt

echo ""
echo "========================================="
echo "Pytest complete!"
echo "========================================="
echo ""
echo "Reports saved to:"
echo "   - pytest/results/report.txt"
echo "   - pytest/results/html/index.html (HTML coverage)"