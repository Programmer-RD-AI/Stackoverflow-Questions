# Use a base image compatible with ARM64 (e.g., Python 3.9 slim)
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Install the necessary Python packages
RUN pip install --no-cache-dir uv

RUN uv init 

RUN uv add numpy

# Default command
CMD ["uv", "run", "python3", "-c", "import numpy as np; print('Numpy version:', np.__version__)"]
