# Instructions for Composing and Running Docker Containers

This README provides step-by-step instructions on how to compose and run Docker containers for Spark and PostgreSQL, allowing you to interact with the Spark cluster and insert data into the PostgreSQL database using PySpark.

## Prerequisites

Before proceeding, make sure you have the following installed on your system:

- Docker: Follow the instructions for your specific operating system from the official Docker website: [Get Docker](https://docs.docker.com/get-docker/)
- Docker Compose: Follow the instructions for your specific operating system from the official Docker Compose website: [Install Docker Compose](https://docs.docker.com/compose/install/)
- PySpark: Make sure you have PySpark installed on your local machine. You can install it using pip:

  ```bash
  pip install pyspark
  ```

## Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your_username/your_repository.git
cd your_repository
```

## Step 2: Create Dockerfiles

In the project directory, create two separate Dockerfiles, one for Spark and another for PostgreSQL.

**Dockerfile for Spark (`spark/Dockerfile`):**
```Dockerfile
# Use a base image with Java and Spark pre-installed
FROM bitnami/spark:latest

# Optionally, you can add additional configurations or copy files to the container if needed
# COPY your_additional_files /path/in/container
# ENV some_environment_variable=value

# Expose Spark ports (change the ports accordingly if needed)
EXPOSE 4040 8080 7077
```

**Dockerfile for PostgreSQL (`postgres/Dockerfile`):**
```Dockerfile
# Use the official PostgreSQL image from Docker Hub
FROM postgres:latest

# Optionally, you can add additional configurations or copy files to the container if needed
# COPY your_additional_files /path/in/container
# ENV some_environment_variable=value

# Expose PostgreSQL port (default is 5432)
EXPOSE 5432
```

## Step 3: Create Docker Compose File

Create a `docker-compose.yml` file in the project directory to manage the containers:

```yaml
version: '3'

services:
  spark:
    build:
      context: ./spark
    ports:
      - "4040:4040" # Spark UI
      - "8080:8080" # Spark Master UI
      - "7077:7077" # Spark Master Port
    # Add any other configuration you need for Spark container

  postgres:
    build:
      context: ./postgres
    ports:
      - "5432:5432" # PostgreSQL port
    environment:
      POSTGRES_USER: your_postgres_user
      POSTGRES_PASSWORD: your_postgres_password
      POSTGRES_DB: your_postgres_database
    # Add any other configuration you need for PostgreSQL container
```

Replace `your_postgres_user`, `your_postgres_password`, and `your_postgres_database` with your desired PostgreSQL credentials.

## Step 4: Build and Run the Containers

In the project directory, build and run the containers using Docker Compose:

```bash
docker-compose build
docker-compose up -d
```

The `docker-compose build` command will build the images for Spark and PostgreSQL based on the Dockerfiles you created earlier. The `docker-compose up -d` command will start the containers in detached mode (in the background).

## Step 5: Access Spark and Insert Data into PostgreSQL

To access the Spark container and use PySpark to insert data into the PostgreSQL database, follow these steps:

### Access the Spark container:

```bash
docker-compose exec spark bash
```

### Use PySpark to interact with PostgreSQL:

```python
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Spark PostgreSQL Example") \
    .getOrCreate()

# Sample DataFrame with data
data = [(1, 10), (2, 20), (3, 30)]
columns = ["id", "value"]
df = spark.createDataFrame(data, columns)

# PostgreSQL connection properties
url = "jdbc:postgresql://postgres:5432/your_database"  # Use the hostname "postgres" as it is the service name in Docker Compose
properties = {
    "user": "your_postgres_user",
    "password": "your_postgres_password",
    "driver": "org.postgresql.Driver"
}

# Write DataFrame to PostgreSQL
df.write.jdbc(url=url, table="your_table_name", mode="append", properties=properties)

# Stop Spark session
spark.stop()
```

Replace `"your_database"`, `"your_postgres_user"`, `"your_postgres_password"`, and `"your_table_name"` with the appropriate values for your PostgreSQL setup.

## Step 6: Accessing PostgreSQL Data with DBeaver (Optional)

To access and explore the data inserted into the PostgreSQL database, you can use DBeaver, a popular database management tool. Follow the instructions in the previous section "How to Access the Results of this DB using DBeaver" to configure DBeaver and connect to the PostgreSQL database.

That's it! You have now successfully composed and run Docker containers for Spark and PostgreSQL, and you can use PySpark to interact with the Spark cluster and insert data into the PostgreSQL database.