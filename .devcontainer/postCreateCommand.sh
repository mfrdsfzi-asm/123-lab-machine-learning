#!/bin/bash

# Exit on any error
set -e

echo "🚀 Setting up development environment..."

# Update pip first
echo "📦 Updating pip..."
pip install --upgrade pip

# Install uv first as it's our primary package manager
echo "📦 Installing uv package manager..."
pip install uv

# Install system dependencies
echo "🛠️ Installing system dependencies..."
sudo apt-get update && sudo apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    git \
    curl \
    wget

# Create virtual environment using uv if it doesn't exist
echo "📦 Setting up Python virtual environment..."
if [ ! -d ".venv" ]; then
    uv venv
fi

# Sync dependencies from pyproject.toml and uv.lock
echo "📦 Installing Python dependencies..."
uv sync

# Install additional development tools in the virtual environment
echo "🛠️ Installing development tools..."
uv add --dev jupyter ipykernel ipywidgets python-dotenv

# Activate virtual environment
echo "✅ Activating virtual environment..."
source .venv/bin/activate

# Configure Jupyter kernel
echo "📦 Setting up Jupyter kernel..."
python -m ipykernel install --user --name=123lab-ml --display-name="123 Lab ML"

echo "✅ Development environment setup complete!"
echo "✅ Virtual environment is activated and ready to use."
echo "✅ To manually activate later, run: source .venv/bin/activate"


