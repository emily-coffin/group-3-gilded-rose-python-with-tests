echo "Installing Python dependencies..."
poetry install

echo "Running pylint..."
poetry run ruff check .

echo "Checking code format..."
poetry run black --check .
