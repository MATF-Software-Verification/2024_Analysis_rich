#!/bin/bash
cd "$(dirname "$0")"
echo "========================================="
echo "Running all analysis"
echo "========================================="
echo ""
./pytest/run_tests.sh
echo ""
./coverage/run_coverage.sh
echo ""
./pylint/run_pylint.sh
echo ""
./mypy/run_mypy.sh
echo ""
./radon/run_radon.sh
echo ""
./vulture/run_vulture.sh
echo ""
./interrogate/run_interrogate.sh
echo ""
echo "========================================="
echo "Analysis completed!"
echo "========================================="
