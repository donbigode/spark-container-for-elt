# spark/Dockerfile

# Use an official PySpark image as base
FROM jupyter/pyspark-notebook:latest

# Install additional dependencies if needed

# Download the PostgreSQL JDBC driver using curl
RUN curl https://jdbc.postgresql.org/download/postgresql-42.2.18.jar -o /opt/bitnami/spark/jars/postgresql-42.2.18.jar
## open and save the maven posgres.jar
# Copy the PostgreSQL JDBC driver to the Spark jars directory
COPY /opt/bitnami/spark/jars/postgresql-42.2.18.jar /usr/local/spark/jars/



# Expose Jupyter Notebook port
EXPOSE 8888
EXPOSE 7077