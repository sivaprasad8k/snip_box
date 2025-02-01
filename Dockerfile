# Use the official Python 3.11 image as the base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Set the working directory in the container
WORKDIR /app

# Install any dependencies you might need
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose the port the app will run on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
