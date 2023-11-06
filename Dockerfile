# Use the official Python image as a parent image
FROM python:3.7

# Set the working directory in the container
WORKDIR /CALCULATOR_API_BACKEND

# Copy the project files into the container
COPY . /CALCULATOR_API_BACKEND

# Install project dependencies
RUN pip install -r requirements_pip.txt

# Expose the port your Django application will run on
EXPOSE 8000

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
