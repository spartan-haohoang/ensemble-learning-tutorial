.PHONY: help install install-dev test lint format clean docker-build docker-run docker-stop docs

# Default target
help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Installation
install: ## Install production dependencies
	uv sync

install-dev: ## Install development dependencies
	uv sync --dev
	uv run pre-commit install

# Development
test: ## Run tests
	uv run pytest tests/ -v --cov=. --cov-report=html --cov-report=term

lint: ## Run linting
	uv run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	uv run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	uv run mypy . --ignore-missing-imports

format: ## Format code
	uv run black .
	uv run isort . --profile black
	uv run nbqa-black notebooks/
	uv run nbqa-isort notebooks/ --profile black

format-check: ## Check code formatting
	uv run black . --check
	uv run isort . --check-only --profile black
	uv run nbqa-black notebooks/ --check

# Docker
docker-build: ## Build Docker image
	docker build -t ensemble-learning:latest .

docker-run: ## Run Docker container
	docker-compose up -d

docker-stop: ## Stop Docker container
	docker-compose down

docker-logs: ## Show Docker logs
	docker-compose logs -f

# Jupyter
jupyter: ## Start Jupyter Lab
	uv run jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root

jupyter-notebook: ## Start Jupyter Notebook
	uv run jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# Data
download-data: ## Download sample datasets (placeholder)
	@echo "Downloading sample datasets..."
	@echo "Add your data download logic here"

# Documentation
docs: ## Generate documentation
	uv run sphinx-build -b html docs/ docs/_build/html

docs-serve: ## Serve documentation locally
	cd docs/_build/html && python -m http.server 8000

# Cleanup
clean: ## Clean up temporary files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .coverage
	rm -rf htmlcov/

clean-docker: ## Clean up Docker resources
	docker system prune -f
	docker volume prune -f

# Security
security-scan: ## Run security scans
	uv run bandit -r . -f json -o bandit-report.json
	uv run safety check

# Pre-commit
pre-commit: ## Run pre-commit hooks on all files
	uv run pre-commit run --all-files

# CI/CD helpers
ci-test: ## Run tests for CI
	uv run pytest tests/ -v --cov=. --cov-report=xml --junitxml=test-results.xml

ci-lint: ## Run linting for CI
	uv run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	uv run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	uv run mypy . --ignore-missing-imports

# Development workflow
dev-setup: install-dev ## Set up development environment
	@echo "Development environment setup complete!"
	@echo "Run 'make jupyter' to start Jupyter Lab"

# Production deployment
deploy: docker-build ## Deploy to production (placeholder)
	@echo "Deployment logic goes here"

# Monitoring
monitor: ## Show system resources
	@echo "=== Docker Containers ==="
	docker ps
	@echo "\n=== System Resources ==="
	docker stats --no-stream
