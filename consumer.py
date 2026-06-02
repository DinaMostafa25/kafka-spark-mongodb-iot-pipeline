from pyspark.sql import SparkSession

# spark = (
#     SparkSession.builder
#     .appName("KafkaConsumer")
#     .master("local[*]")
#     .getOrCreate()

# )



# print("Spark Session Created Successfully")

#  spark.stop()



spark = (
    SparkSession.builder
    .appName("KafkaConsumer")
    .master("local[*]")
    .config( # add kafka connector
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0"
    )
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df = ( # create streaming df
    spark.readStream
    .format("kafka")
    .option(
        "kafka.bootstrap.servers",
        "localhost:9094,localhost:9095,localhost:9096"
    )
    .option("subscribe", "factory-sensors")
    .option("startingOffsets", "latest")
    .load()
)

query = (
    df.selectExpr(
        "CAST(value AS STRING)"
    )
    .writeStream # start output stream
    .format("console") # to print result on cosole
    .outputMode("append") # I need new rows only
    .start() # action
)

query.awaitTermination() # keep stream alive