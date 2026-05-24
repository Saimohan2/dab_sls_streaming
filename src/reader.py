from pyspark.sql import DataFrame

def create_df(data, spark, schema)-> DataFrame:

    df = (spark.createDataFrame(data, schema))

    return df