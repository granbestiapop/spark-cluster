import pyspark
import time
import json 
from pyspark.sql.functions import udf


def squared_udf2(s):
  s = s[1:-1].replace('""', '\"')
  json_obj = json.loads(s)
  for item in json_obj:
    if item["resourceName"]:
      return item["resourceName"]
  return ""

def test():
  s = '"[{""resourceType"":""AWS::DynamoDB::Table"",""resourceName"":""fojbcmfhjnchmmkbpgglhlphjobmdapbabimkobj""}]"'
  print(squared_udf2(s))

test()

sc = pyspark.SparkContext()#master='spark://spark-master:7077')

# A JSON dataset is pointed to by path.
# The path can be either a single text file or a directory storing text files
path = "./data/data.csv"
sqlContext = pyspark.SQLContext(sc)
df = sqlContext.read.options(header = True, quote="\"", escape="\"").csv(path)

# The inferred schema can be visualized using the printSchema() method
df.printSchema()

@udf("string")
def squared_udf(s):
  json_obj = json.loads(s)
  for item in json_obj:
    if "resourceName" in item:
      return item['resourceName']
  return ""

df.select(squared_udf("Resources"),df["Request ID"]).show(10, False)

# Define the schema
#from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField, StringType
#json_schema = ArrayType(StructType([StructField('resourceType', StringType(
#), nullable=True)]))
# Define udf
#udf_parse_json = udf(lambda s: parse_json(s), json_schema)
# Generate a new data frame with the expected schema
#df_new = df.select(udf_parse_json(df.Resources).alias("json")) #udf_parse_json(df.Resources).alias("attr_2")
#df_new.show()


#df = spark.createDataFrame(data = arrayStructureData, schema = arrayStructureSchema)
#df.printSchema()
#df.show(truncate=False)
#peopleDF.rdd.map(lambda f: parse_json(f)).toDF().show()

#select('Resources')
# Creates a temporary view using the DataFrame
#peopleDF.createOrReplaceTempView("data")

def timer(func):
  def inner(*args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    print("--- %s seconds ---" % (time.time() - start_time))
  return inner


# SQL statements can be run by using the sql methods provided by spark
@timer
def query(sqlContext, query):
  data = sqlContext.sql(query)
  data.show()

#query(sqlContext, "SELECT * FROM data limit 1")
#query(sqlContext, "SELECT count(*) FROM data")
#query(sqlContext, "SELECT * FROM data WHERE primaryName  = 'Stephen Baldwin'")


