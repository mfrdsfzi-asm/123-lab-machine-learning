# 123 Lab Machine Learning

A containerized machine learning development environment using Python 3.12, UV package manager, and Jupyter.

## 🚀 Quick Start

### Using Dev Container (Recommended)

1. **Open in VS Code**: Make sure you have the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed

2. **Reopen in Container**: VS Code will prompt you to reopen in container, or use `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"
![Open in Dev Container](/.devcontainer/open_dev_container.jpg)

3. **Wait for Setup**: The environment will automatically set up (takes 2-3 minutes on first run)
4. **Start Coding**: Everything is ready! The virtual environment is activated automatically.

### Manual Setup (Alternative)

If you prefer to set up locally:

```bash
# Install uv package manager
pip install uv

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Install development dependencies
uv sync --extra dev
```

## 📦 What's Included

### Core Dependencies
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning library
- **Seaborn**: Statistical data visualization
- **Matplotlib**: Plotting library
- **Jupyter**: Interactive notebooks

### Development Tools
- **pytest**: Testing framework
- **black**: Code formatter
- **flake8**: Linting
- **mypy**: Type checking
- **python-dotenv**: Environment variable management

### System Dependencies
- **ffmpeg**: Media processing
- **libsm6, libxext6**: GUI support for OpenCV/matplotlib