# Step 1: Use an official Python image as a base
# This sets the base image for your container, using a slim version of Python 3.10.
# It ensures that the necessary Python environment is already set up, reducing setup complexity.
FROM python:3.10-slim

# Step 2: Set working directory inside the container
# This defines the directory in the container where your code will be placed and executed.
# Any subsequent commands will be executed from this directory.
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
# This copies the entire current directory from your host machine into the container's /app folder.
# This includes all application files and directories required for your Flask app to run.
COPY . /app

# Step 4: Install dependencies
# This installs all the required Python dependencies listed in the requirements.txt file.
# The --no-cache-dir option ensures that pip doesn’t store downloaded package files, reducing the image size.
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port Flask will run on
# This exposes port 5000 on the container, allowing external access to the Flask application.
# Flask's default port is 5000, and this declaration tells Docker that the container will listen on this port.
EXPOSE 5000

# Step 6: Set environment variables
# These environment variables configure Flask's behavior:
# - FLASK_APP=app.py tells Flask which file is the application entry point.
# - FLASK_RUN_HOST=0.0.0.0 allows the Flask app to be accessed externally from the container.
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 7: Run the Flask app
# This command tells Docker to run the Flask application when the container starts.
# It uses the flask run command to start the web server for your application.
CMD ["flask", "run"]
