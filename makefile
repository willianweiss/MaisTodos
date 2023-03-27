.PHONY: build up down test locust lint coverage

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

test:
	pytest . --disable-warnings

lint:
	black . --line-length 79 -t py37 --skip-string-normalization
	isort . --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 -l 79

test-cov:
	pytest -x --cov=api --cov-report=term-missing --cov-report=xml --cov-fail-under=80 --junitxml=report.xml --disable-warnings  --cov-config=.coveragerc
