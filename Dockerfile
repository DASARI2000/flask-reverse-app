# Stage 1: Build
FROM python:3.9-slim AS builder

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy application files
COPY app.py app.py

# Expose the application port
EXPOSE 5000

# Health check to ensure the application is running
HEALTHCHECK CMD curl --fail http://localhost:5000/strings || exit 1

# Command to run the application
CMD ["python", "app.py"]
