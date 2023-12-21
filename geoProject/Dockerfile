# Use Python 3.12 as the base image
FROM python:3.12

# Set the working directory to /code
WORKDIR /code

# Update package lists and install required packages
RUN apt-get update \
    && apt-get install -y libpq-dev binutils libproj-dev gdal-bin \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user with UID and GID 1000
RUN adduser --disabled-password --uid 1000 --gecos '' myuser

# Add ~/.local/bin to the PATH
ENV PATH="/home/myuser/.local/bin:${PATH}"

# Switch to the non-root user
USER myuser

# Copy requirements and install them separately to leverage Docker cache
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt --user

# Copy the rest of the application code
COPY . .

# Set the entrypoint script
ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
