import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext.getOrCreate()
spark = SparkSession.builder.getOrCreate()

# Script generated for node S3DataSource
S3DataSource_1787319989067 = spark.read.format("csv") \
    .option("inferschema", "true") \
    .option("multiLine", "true") \
    .option("header", "true") \
    .option("recursiveFileLookup", "true") \
    .option("sep", ",") \
    .load("s3://amazon-sagemaker-904233107470-eu-west-1-97b398d3b56c/dzd-59rbf0ds627n86/6n7k7vqbk2kx06/dev/")
# Script generated for node S3DataSink
S3DataSource_1787319989067.write.format("csv") \
    .option("header", False) \
    .mode("append") \
    .save("s3://amazon-sagemaker-904233107470-eu-west-1-97b398d3b56c/dzd-59rbf0ds627n86/6n7k7vqbk2kx06/spike/feature/")
