from pyspark.sql import functions as F

def clean_df(df):

    df = (df.filter(F.col("id").isNotNull())
          .withColumn("city", F.trim("city")))
    
    return df