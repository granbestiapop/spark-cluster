import pyspark
sc = pyspark.SparkContext(master='spark://spark-master:7077')

# A JSON dataset is pointed to by path.
# The path can be either a single text file or a directory storing text files
path = "/data/test.json"
sqlContext = pyspark.SQLContext(sc)
peopleDF = sqlContext.read.json(path)

# The inferred schema can be visualized using the printSchema() method
peopleDF.printSchema()
# root
#  |-- age: long (nullable = true)
#  |-- name: string (nullable = true)

# Creates a temporary view using the DataFrame
peopleDF.createOrReplaceTempView("people")

# SQL statements can be run by using the sql methods provided by spark
teenagerNamesDF = sqlContext.sql("SELECT name FROM people WHERE age BETWEEN 13 AND 19")
teenagerNamesDF.show()