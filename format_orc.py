from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("myApp")
sc = SparkContext(conf=conf)

irdd = sc.parallelize([100.9,18.0008934689,None,100.98239647888])

def truncateFloat(p):
    for rec in p:
        yield '%.5f' % round(rec * 100000 / 100000, 5) if isinstance(rec, float) else rec


ordd = irdd.mapPartitions(lambda p: truncateFloat(p))
print ordd.collect()