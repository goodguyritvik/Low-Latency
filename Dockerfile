FROM python:3.9-slim

# Set pip timeout to be longer
ENV PIP_DEFAULT_TIMEOUT=100

# Create app directory
WORKDIR /app

# Install system dependencies first
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy application files
COPY *.py ./

# Start scheduler
CMD ["python", "scheduler.py"]
