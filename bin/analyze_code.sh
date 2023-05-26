echo "Installing Python dependencies..."
poetry install

echo "Running pylint..."
poetry run pylint .

echo "Checking code format..."
poetry run black --check .
