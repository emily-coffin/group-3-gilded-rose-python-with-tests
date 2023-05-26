echo "Installing Python dependencies..."
poetry install

echo "Running tests..."
poetry run pytest -s -vv \
    --cov="." \
    --cov-report=term-missing \
    --cov-report=xml \
    --cov-fail-under=90 \
    --junit-xml="./unit_test_results/test_results.xml"
