from pyspark.sql import SparkSession
import os 

def read_generic_file(spark, file_path):
    _, file_extension = os.path.splitext(file_path)
    supported_extensions = ['.csv', '.txt']  # Add more file extensions as needed

    if file_extension.lower() in supported_extensions:
        if file_extension.lower() == '.csv':
            df = spark.read.csv(file_path, header=True, inferSchema=True)
        elif file_extension.lower() == '.txt':
            df = spark.read.text(file_path)
        return df
    else:
        raise ValueError(f"File extension {file_extension} not supported.")

def create_table_in_postgres(df, table_name, connection_properties):
    df.write.jdbc(url=connection_properties['url'], table=table_name, mode='overwrite', properties=connection_properties)
    print(f"Table '{table_name}' created successfully.")