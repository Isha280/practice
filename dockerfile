FROM python:3.11-slim

# Create app directory
WORKDIR /app

# Copy package files
COPY requirement.txt .

# Install dependencies
RUN pip install -r requirement.txt

# Copy project files
COPY app.py .

# Expose app port
EXPOSE 5000

# Start app
CMD ["python", "app.py"]
