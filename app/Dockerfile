# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Run tests before starting Flask application
RUN python3 app_test.py

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP app.py

# Run the command to start Flask application
CMD ["flask", "run", "--host=0.0.0.0"]