from pyspark.sql import SparkSession

def get_spark():

    spark = SparkSession.builder.appName("streaming").getOrCreate()

    return spark