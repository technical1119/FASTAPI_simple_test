# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies for Chrome, Selenium, and Python packages
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    libx11-dev \
    libx11-6 \
    libxext6 \
    libxi6 \
    libgdk-pixbuf2.0-0 \
    libdbus-1-3 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt

# Copy the scraper script into the container
COPY scraper.py /app/

# Run the scraper
CMD ["python", "/app/scraper.py"]
