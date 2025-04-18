from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import os


def test_pyspark():
    spark = SparkSession.builder \
        .appName("test_pyspark") \
        .getOrCreate()

    # Define sample data as a list of tuples
    data = [
        (1, "Alice", 29),
        (2, "Bob", 35),
        (3, "Charlie", 23)
    ]

    # Define the column names
    columns = ["id", "name", "age"]

    # Create a DataFrame using the sample data
    df = spark.createDataFrame(data, schema=columns)

    # Save the DataFrame as a permanent table named 'people'
    df.write.mode("overwrite").saveAsTable("people")

    try:
        print(spark.sql("show tables").show())

        # (Optional) Query the newly created permanent table to verify the data
        result = spark.sql("SELECT * FROM default.people")
        assert result.count() == 3
        print(result.show())
    finally:
        spark.sql("DROP TABLE IF EXISTS people")
        people_table_row = spark.sql("show tables").where(
            F.col("tableName") == "people")
        assert people_table_row.count() == 0
        spark.stop()
