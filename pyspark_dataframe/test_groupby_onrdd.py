from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, Row
from pyspark.sql.types import *
from pyspark.sql import functions
import importlib
import __builtin__
conf = SparkConf().setAppName("myApp")
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

ischema = [['order_key', 'customer_key', 'order_status', 'total_price', 'order_date', 'order_priority', 'clerk', 'ship_priority', 'comment']]

new_rdd = sqlContext.sql('select order_key,customer_key,order_status,total_price,order_date,order_priority,clerk,ship_priority,comment from  si_demo_context_1_common_datasets.TpchOrderStatus')
print new_rdd.collect()

def make_key_val(partition):
   for record in partition:
       try:
          values = record
          yield('1',values)
       except:
          pass


def convertdataType(val, applyOntype):
     if applyOntype:
        func = getattr(__builtin__, applyOntype)
        cv = func(val)
        return cv
     return val


def computeAggregates(partition):
    for record in partition:
        outRecord = []
        try:
            def createBag(records, applyOntype):
                bag = []
                for e in records:
                    val = e[ischema.index('total_price')]
                    if val is not None:
                        bag.append(convertdataType(val, applyOntype))
                return bag
            aggregates = [{'operator': 'numpy.median', 'out_field': 'total_price_median(number(10-2))', 'apply_on':'total_price'}]
            for aggr in aggregates:
                bag = []
                op = aggr['operator'].rsplit('.', 1)
                if len(op) != 2:
                    raise Exception(
                "Wrong operator: operator should be either of 'sum', 'count', 'avg', 'min','max' or should be specified as module_name.function_name")
                try:
                    mod = importlib.import_module(op[0])
                    method = getattr(mod, op[1])
                except:
                    raise Exception("Module/function specified " + aggr['operator'] + " is not present in python path.")
                applyOnType = 'bigint'
                bag = createBag(record[1], applyOnType)
                value = method(bag)
                outRecord.append(value)
            yield outRecord
        except:
            pass

groupdrdd = new_rdd.mapPartitions(lambda x : make_key_val(x)).groupByKey().mapPartitions(lambda x : computeAggregates(x))
print groupdrdd.collect()
