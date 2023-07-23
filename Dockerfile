# Use the official Python base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy all Python files to the container's working directory
COPY main.py machineInfo.py /app/

# Install the required Python packages
RUN pip install psutil gputil

# Run the Python program when the container starts
CMD ["python", "main.py"]