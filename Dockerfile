# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV JUPYTER_ENABLE_LAB=yes
ENV JUPYTER_TOKEN=""
ENV JUPYTER_ALLOW_ROOT=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install UV
RUN pip install uv

# Copy project files
COPY pyproject.toml ./
COPY README.md ./
COPY data/ ./data/
COPY ensembles.ipynb ./

# Install Python dependencies with UV
RUN uv pip install --system --no-cache -e .

# Expose Jupyter port
EXPOSE 8888

# Create a non-root user for security
RUN useradd -m -u 1000 jupyter && \
    chown -R jupyter:jupyter /app && \
    mkdir -p /home/jupyter/.jupyter && \
    chown -R jupyter:jupyter /home/jupyter
USER jupyter

# Start Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]
