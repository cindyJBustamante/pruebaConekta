from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
from pyspark.sql.types import StructType,StructField, StringType, TimestampType, DecimalType, DateType



#Start the sparkSession
spark = SparkSession.builder.master("local").appName("PruebaConekta").enableHiveSupport().getOrCreate()
session = SparkSession.builder.getOrCreate()


#Set the connection parameter to SQL Server
properties = {
    "user": sys.argv[1],
    "password": sys.argv[2],
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

host = sys.argv[3]
port = sys.argv[4]

url="jdbc:sqlserver://"+host+":"+port+";databaseName=DBZ18;"


#Reading the data from hive
data_prueba_hive = spark.sql("select *  from data_prueba_tecnica")


#Loading data to sql Server 
data_prueba_hive.write.mode("Append").jdbc(url, "CMP.data_prueba_SqlS", mode = 'append', properties=properties)

#Download the data from sql Server 
data_sqlServer = spark.read.jdbc(url, "CMP.data_prueba_SqlS", properties=properties)

#Removing nulls from the data 
data_clean = data_sqlServer.filter(col("id").isNotNull() & col("company_id").isNotNull() & col("amount").isNotNull() & col("status").isNotNull() & col("created_at").isNotNull())
data_clean.createOrReplaceTempView("data_clean")

#Transforming data to the final schema
df_clean = spark.sql("Select substr(id,1,24) as id, substr(name,1,130) as name, substr(company_id,1,24) as company_id, cast(amount as decimal(16,2)) as amount, cast(status as varchar(30)) as status, cast(created_at as timestamp) as created_at, cast(paid_at as timestamp) as paid_at from data_clean")
data_rdd  = df_clean.rdd

data_schema = StructType([ \
    StructField("id",StringType(),False), \
    StructField("company_name",StringType(),True), \
    StructField("company_id",StringType(),False), \
    StructField("amount", DecimalType(18,2), False), \
    StructField("status", StringType(), False), \
    StructField("created_at", TimestampType(), False), \
    StructField("updated_at", TimestampType(), True) \
  ])
 
data_trasformed = spark.createDataFrame(data=data_rdd,schema=data_schema)

#Writing final eschema in a hive table
data_trasformed.write.mode("append").saveAsTable("final_data_table")