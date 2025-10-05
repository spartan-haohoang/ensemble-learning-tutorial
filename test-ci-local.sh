#!/bin/bash

# Local CI Testing Script
# This script runs the same commands as your GitHub Actions CI pipeline

set -e  # Exit on any error

echo "🚀 Starting local CI test..."

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Please run this script from the project root."
    exit 1
fi

# Install dependencies (same as CI)
echo "📦 Installing dependencies..."
uv sync --extra dev

# Run linting with flake8 (same as CI)
echo "🔍 Running flake8 linting..."
uv run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude=.venv
uv run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude=.venv

# Run type checking with mypy (same as CI)
echo "🔍 Running mypy type checking..."
uv run mypy . --ignore-missing-imports

# Run tests with pytest (same as CI)
echo "🧪 Running tests..."
uv run pytest tests/ -v --cov=. --cov-report=xml

echo "✅ Local CI test completed successfully!"
echo "🎉 Your code should pass the GitHub Actions CI pipeline!"
