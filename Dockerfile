# Use the official Python image from the Docker Hub
# This pulls the Python 3.10 slim image from the official Docker repository.
# The slim version is a smaller, optimized version of the full Python image, ideal for production environments.
FROM python:3.10-slim

# Set the working directory inside the container
# This defines the directory inside the container where all commands will be run.
# By setting it to /app, you ensure that all subsequent commands (COPY, RUN, etc.) will operate within this directory.
WORKDIR /app

# Copy the current directory contents into the container
# This copies the files from your local project directory (where the Dockerfile is located)
# into the /app directory inside the container.
# This step ensures that your application files are available for the container to use.
COPY . /app

# Install the dependencies
# This runs the pip installer to install all the Python dependencies listed in the requirements.txt file.
# The --no-cache-dir option prevents pip from caching the downloaded packages, reducing the size of the image.
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
# This exposes port 5000 on the container, which is the default port used by Flask for its web server.
# It allows you to access the Flask app from outside the container (e.g., via a browser or API client).
EXPOSE 5000

# Set the environment variable for Flask
# The FLASK_APP environment variable tells Flask which Python file to run.
# Here, it points to app.py, the main entry point for the application.
ENV FLASK_APP=app.py

# Start Flask
# This command tells Docker to run the Flask app when the container starts.
# The --host=0.0.0.0 option makes the Flask app accessible from outside the container (allowing remote access).
CMD ["flask", "run", "--host=0.0.0.0"]
