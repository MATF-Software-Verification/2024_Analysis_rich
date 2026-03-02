#!/bin/bash

cd "$(dirname "$0")/.."

# Kreiranje foldera za rezultate
mkdir -p coverage/results

echo "========================================="
echo "Running Pytest with Coverage for Rich"
echo "Using original Rich library tests"
echo "========================================="
echo ""

# Pokretanje Pytest sa testovima iz spoljnog rich repoa
pytest ../rich/tests/ \
    --cov=../rich/rich \
    --cov-report=term \
    --cov-report=html:coverage/results/html \
    2>&1 | tee coverage/results/report.txt

echo ""
echo "========================================="
echo "Pytest complete!"
echo "========================================="
echo ""
echo "Reports saved to:"
echo "   - coverage/results/report.txt"
echo "   - coverage/results/html/index.html"
