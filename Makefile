analyze_code:
	./bin/analyze_code.sh
format:
	poetry run black .
	poetry run ruff --fix .
unit_tests:
	bin/test.sh
