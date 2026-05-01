.PHONY: help install dev test lint docker-build

help:
	@echo "WatchdogX Commands"

install:
	pip install -e .

dev:
	pip install -e ".[dev]"
	pip install black ruff pytest pytest-asyncio pytest-cov

test:
	pytest tests/ -v --cov=watchdogx

lint:
	black --check src/ tests/
	ruff check src/ tests/

docker-build:
	docker build -t watchdogx:latest .
