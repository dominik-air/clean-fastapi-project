FROM python:3.10.5-alpine3.16

# Install extra packages for the OS
RUN apk --no-cache add build-base

# Install Python libraries
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --no-cache-dir

# Change working directory and copy all the files into the container
WORKDIR /app

COPY . .

# Expose the service
EXPOSE 8080

# Run the application
CMD ["python3", "-u", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]