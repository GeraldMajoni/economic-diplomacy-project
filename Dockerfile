# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Prevent Python from writing .pyc files to disk and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for mysqlclient (using MariaDB packages)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        pkg-config \
        libmariadb-dev \
        libmariadb-dev-compat \
        build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy the pip requirements file into the container
COPY requirements.txt /app/

# Upgrade pip and install the Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Command to run the Django application using gunicorn
CMD ["gunicorn", "ed_project.wsgi:application", "--bind", "0.0.0.0:8000"]
