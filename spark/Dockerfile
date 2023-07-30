
# Use a base image with Java and Spark pre-installed
FROM bitnami/spark:latest

# Define working directory
WORKDIR /app

# Copy the Spark script and drivers to the container
COPY spark-scripts/ /app/spark-scripts
COPY jars/ app/jars

# Create directories for data and logs and set appropriate permissions
RUN mkdir -p /opt/bitnami/spark/data && \
    mkdir -p /opt/bitnami/spark/logs && \
    chmod -R 777 /opt/bitnami/spark/data && \
    chmod -R 777 /opt/bitnami/spark/logs