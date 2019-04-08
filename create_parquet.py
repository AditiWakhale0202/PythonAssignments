from pyspark import SparkConf, SparkContext
from pyspark import HiveContext

sc = SparkContext(conf=SparkConf().setAppName("My App"))
sqlContext = HiveContext(sc)


df1 = sqlContext.sql('select * from si_demo_context_branderstanding.sector_wise_brand_data')
df1.write.format('parquet').save("/home/aditi/dump_parquet/")
#df1.write().format('parquet')