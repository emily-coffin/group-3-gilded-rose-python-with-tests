analyze_code:
	./bin/analyze_code.sh
format:
	poetry run black .
unit_tests:
	bin/test.sh
