#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Check if a tag is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <tag>"
  exit 1
fi

TAG=$1
IMAGE_NAME="ebay-kleinanzeigen-api"

# Build the Docker image
echo "Building the Docker image..."
docker build -t $IMAGE_NAME:$TAG .

# Stop and remove any existing container with the same name
echo "Stopping and removing any existing container..."
docker stop $IMAGE_NAME || true
docker rm $IMAGE_NAME || true

# Run the Docker container with port forwarding
echo "Starting the Docker container..."
docker run -d --name $IMAGE_NAME -p 8000:8000 $IMAGE_NAME:$TAG

echo "Container is running and accessible on port 8000."