FROM python:3.10.5-alpine3.16

# Install extra packages for the OS
RUN apk --no-cache add build-base

# Change working directory and copy all the files into the container
WORKDIR /app

COPY . .

# Expose the service
EXPOSE 9000

# Run the application
CMD ["python3", "-u", "-m", "http.server", "--bind", "0.0.0.0", "9000"]