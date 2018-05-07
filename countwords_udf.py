# -*- coding: utf8 -*-
def process(transform, params=None):
    if transform is not None:
        print transform
        transform = str(transform).encode('utf8')
        return len(transform.split())
    else:
        return None

def callUdf(partitions):
    try:
        for rec in partitions:
            rec_col = process(rec)
            print rec_col
            yield rec_col
    except Exception:
        pass

from pyspark import SparkConf, SparkContext

def call_df_udf(transform):
    return process(transform)

conf= SparkConf().setAppName("map")
sc= SparkContext(conf=conf)
rdd1= sc.parallelize(['Hello World','Gutan mitak',u'जगाला नमस्कार',u'Ni Hao shìjiè'])
list_rd= rdd1.collect()
outrdd = rdd1.mapPartitions(lambda partitions: callUdf(partitions))
print outrdd.collect()

from pyspark import SQLContext
from pyspark.sql import functions
from pyspark.sql.types import *

sqlContext = SQLContext(sc)
df1 = sqlContext.createDataFrame([['Hello World',1],[u'जगाला नमस्कार',3],[u'Ni Hao shìjiè',7]],['msg','ratings'])
print df1.show()
#out_df= process(df1['msg'].show())
out_df = df1.select(['msg',functions.udf(call_df_udf,StringType())(df1['msg']).cast(StringType()).alias('word_cnt')])
print out_df.show()