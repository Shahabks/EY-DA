# Use a Python 3.9 base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir nest_asyncio python-dotenv llama-cloud-services llama-index-core

# Copy the .env file (if you have one)
COPY .env .env

# Copy the application code
COPY Parse.py /app/Parse.py

# Command to run the application.  Make this generic.
CMD ["python", "/app/Parse.py", "--input", "/app/input.pdf", "--output", "/app/output/output.md"]