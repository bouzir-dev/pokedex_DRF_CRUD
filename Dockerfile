FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the working directory
COPY . /app

# Install pipenv and dependencies from Pipfile
RUN pip install pipenv
RUN pipenv install --system --deploy

# Set the entrypoint script as executable
RUN chmod +x entrypoint.sh

# Run the entrypoint script when the container starts
ENTRYPOINT ["./entrypoint.sh"]