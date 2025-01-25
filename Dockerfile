# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy source files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
