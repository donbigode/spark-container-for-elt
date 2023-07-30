from pyspark.sql import SparkSession
from spark_scripts.file_operations import read_generic_file, create_table_in_postgres

if __name__ == "__main__":
    # Initialize Spark session with the PostgreSQL JDBC driver
    spark = SparkSession.builder \
        .appName("Process Generic File and Create Table") \
        .config("spark.jars", "drivers/postgresql-<version>.jar") \
        .getOrCreate()

    # Configuration (modify these parameters as needed)
    file_path = "inbound/sample_data.csv"  # Change this to the actual file path in the inbound folder
    table_name = "your_table_name"  # Change this to the desired table name
    connection_properties = {
        'url': "jdbc:postgresql://your_postgres_host:5432/elt-pg",
        'user': "pg-admin",
        'password': "beterraba123",
        'driver': "org.postgresql.Driver"
    }

    try:
        # Read the file and create DataFrame
        df = read_generic_file(spark, file_path)

        # Create the table in PostgreSQL
        create_table_in_postgres(df, table_name, connection_properties)

        # Stop Spark session
        spark.stop()
    except Exception as e:
        print(f"An error occurred: {e}")

