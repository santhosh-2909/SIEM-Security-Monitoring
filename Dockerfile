# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Set working directory to backend to run main.py
WORKDIR /app/backend

# Run the application
CMD ["python", "main.py"]
