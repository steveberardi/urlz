
test: venv/bin/activate
	PYTHONPATH=./src/ ./venv/bin/python -m pytest --cov=src/wurl/ --cov-report=term --cov-report=html .

venv/bin/activate: requirements-dev.txt
	python -m venv venv
	./venv/bin/pip install -r requirements-dev.txt

clean:
	rm -rf __pycache__
	rm -rf venv

.PHONY: clean example
