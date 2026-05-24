from spark.spark_sess import get_spark
from reader import create_df
from transformations.transform import clean_df

def main():

    spark = get_spark()

    print(spark)
    print(spark.sparkContext.master)

    data = ([
    (1, "Sai", 28, "Hyderabad"),
    (2, "Jay", 1, "Hyderabad"),
    (3, "Mounica", 26, "Hyderabad"),
    (4, "Sri", 26, "Bengaluru"),
    (5, "Ritu", 27, "Bengaluru"),
    (None, None, None, None)])

    schema = ["id", "name", "age", "city"]

    df = create_df(data, spark, schema)

    df = clean_df(df)

    df.show()

    spark.stop()

if __name__ == "__main__":

    main()