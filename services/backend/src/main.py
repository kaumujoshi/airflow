import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row

def read_table():
    spark = (SparkSession.builder
        .config("spark.jars", "/usr/local/postgresql-42.2.5.jar")
        .master("local")
        .appName("PySpark_Postgres_test")
        .getOrCreate())

    myData = spark.read.format("csv").option("header","true").load("data.csv")

    myData.show()

    mode = "overwrite"
    url = "jdbc:postgresql://test_db_3:5432/template_db"
    properties = {"user": "template","password": "template","driver": "org.postgresql.Driver"}
    myData.write.option('driver', 'org.postgresql.Driver').jdbc(url=url, table="Table_name", mode=mode, properties=properties)

read_table()