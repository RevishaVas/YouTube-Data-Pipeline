# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy everything from the folder into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Default command (override if needed)
CMD ["python", "fetch_youtube.py"]  # or redis_to_postgres.py or app.py
