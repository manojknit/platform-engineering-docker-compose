# # Use an official Python runtime as the base image
# FROM python:3.10

# # Set the working directory in the container to /app
# WORKDIR /api

# # Copy requirements.txt to the working directory
# COPY requirements.txt ./

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Bundle the app source inside the Docker image
# COPY . .

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Run the command to start uWSGI
# CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000"]

# 
FROM python:3.11 as requirements-stage

# 
WORKDIR /tmp

# 
RUN pip install poetry

# 
COPY ./pyproject.toml ./poetry.lock* /tmp/

# 
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# 
FROM python:3.11

# 
WORKDIR /app

# 
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY ./ ./

# 
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]