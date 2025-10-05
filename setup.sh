#!/bin/bash

# Setup script for Ensemble Learning project
# This script sets up the development environment

set -e

echo "🚀 Setting up Ensemble Learning Project..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "⚠️  Docker is not installed. Docker setup will be skipped."
    echo "   Install Docker to use containerized development."
fi

# Install dependencies
echo "📦 Installing dependencies..."
uv sync

# Install pre-commit hooks
echo "🔧 Setting up pre-commit hooks..."
uv run pre-commit install

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p logs
mkdir -p models
mkdir -p data/raw
mkdir -p data/processed

# Copy environment file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp env.example .env
    echo "   Please edit .env file with your configuration."
fi

# Set up Git hooks
echo "🪝 Setting up Git hooks..."
git config core.hooksPath .git/hooks

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your configuration"
echo "2. Run 'make jupyter' to start Jupyter Lab"
echo "3. Or run 'make docker-run' to use Docker"
echo ""
echo "Available commands:"
echo "- make help          # Show all available commands"
echo "- make test          # Run tests"
echo "- make lint          # Run linting"
echo "- make format        # Format code"
echo "- make docker-build  # Build Docker image"
echo "- make docker-run    # Run with Docker"
