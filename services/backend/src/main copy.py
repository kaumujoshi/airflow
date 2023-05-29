import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row

def read_table():
    spark = (SparkSession.builder
        .config("spark.jars", "/usr/local/postgresql-42.2.5.jar")
        .master("local")
        .appName("PySpark_Postgres_test")
        .getOrCreate())

    myData = spark.read.format("csv").option("header","true").load("src/data.csv")

    # myData.show()

    mode = "overwrite"
    url = "jdbc:postgresql://db:5432/template_db"
    properties = {"user": "template","password": "template","driver": "org.postgresql.Driver"}
    myData.write.option('driver', 'org.postgresql.Driver').jdbc(url=url, table="Table_name", mode=mode, properties=properties)

def transform_table():

    myData = (spark.read.format("jdbc")
          .option("url", "jdbc:postgresql://db:5432/template_db")
          .option("driver", "org.postgresql.Driver")
          .option("dbtable", "Table_name")
          .option("user", "template").option("password", "template").load())
    
    #transformation
    myData_new = myData.select("value"*10)

    mode = "overwrite"
    url = "jdbc:postgresql://db:5432/template_db"
    properties = {"user": "template","password": "template","driver": "org.postgresql.Driver"}
    myData_new.write.option('driver', 'org.postgresql.Driver').jdbc(url=url, table="Table_name_2", mode=mode, properties=properties)

    