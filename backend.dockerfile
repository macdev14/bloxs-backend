# Use the official Python image from Docker Hub
FROM python:3.8.18-alpine3.18

# Set the working directory in the container
WORKDIR /backend

# Copy the requirements file to the working directory
COPY requirements.txt /backend



# Copy all files from your current directory to the working directory in the container
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port your app runs on
EXPOSE 5000

