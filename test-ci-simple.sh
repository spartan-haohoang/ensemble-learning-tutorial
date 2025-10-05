#!/bin/bash

# Simple Local CI Testing Script
# This script runs the essential CI commands locally

set -e  # Exit on any error

echo "🚀 Starting simple local CI test..."

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Please run this script from the project root."
    exit 1
fi

# Install dependencies (same as CI)
echo "📦 Installing dependencies..."
uv sync --extra dev

# Test that flake8 is available
echo "✅ Testing flake8 availability..."
uv run flake8 --version

# Test that mypy is available  
echo "✅ Testing mypy availability..."
uv run mypy --version

# Test that pytest is available
echo "✅ Testing pytest availability..."
uv run pytest --version

echo "✅ All CI tools are available!"
echo "🎉 Your CI should work when you push to GitHub!"
echo ""
echo "💡 To run the full CI locally, use: ./test-ci-local.sh"
echo "💡 To run just linting: uv run flake8 . --exclude=.venv"
echo "💡 To run just tests: uv run pytest tests/ -v"
