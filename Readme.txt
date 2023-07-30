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

## Project Structure

The project directory should have the following structure:

```
your_project_folder/
│
├── drivers/
│   └── postgresql-<version>.jar  <-- Place the PostgreSQL JDBC driver JAR file here
│
├── inbound/
│   └── sample_data.csv
│
├── postgres/
│   └── Dockerfile
│
├── spark/
│   └── Dockerfile
│
├── spark_scripts/
│   ├── __init__.py
│   └── file_operations.py
│
├── docker-compose.yml
├── main.py
└── Readme.txt
```

## Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/donbigode/spark-container-for-elt.git
cd spark-container-for-elt
```

## Step 2: Download the PostgreSQL JDBC Driver

Download the PostgreSQL JDBC driver (JAR file) from the PostgreSQL official website or the Maven repository. Make sure to choose the appropriate version of the JDBC driver that matches your PostgreSQL server version. Place the downloaded JAR file in the `drivers` folder inside your project directory.

## Step 3: Create Dockerfiles

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

## Step 4: Create Docker Compose File

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

## Step 5: Build and Run the Containers

In the project directory, build and run the containers using Docker Compose:

```bash
docker-compose build
docker-compose up -d
```

The `docker-compose build` command will build the images for Spark and PostgreSQL based on the Dockerfiles you created earlier. The `docker-compose up -d` command will start the containers in detached mode (in the background).

## Step 6: Run the PySpark Script

In the root of your project directory, run the `main.py` script to read the generic file and create a table in PostgreSQL:

```bash
python main.py
```

The `main.py` script will use PySpark to read the generic file (supported extensions: `.csv` and `.txt`) from the `inbound` folder and create a new table with the same column names and data types in the specified PostgreSQL database.

## Step 7: Accessing PostgreSQL Data with DBeaver (Optional)

To access and explore the data inserted into the PostgreSQL database, you can use DBeaver, a popular database management tool. Follow the instructions in the previous section "How to Access the Results of this DB using DBeaver" to configure DBeaver and connect to the PostgreSQL database.

That's it! You have now successfully composed and run Docker containers for Spark and PostgreSQL, used PySpark to interact with the Spark cluster, and inserted data into the PostgreSQL database.