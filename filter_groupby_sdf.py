from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, Row
from pyspark.sql.types import *
from pyspark.sql import functions


conf = SparkConf().setAppName("myApp")
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)


#create a sample dataframe
india_employment = sqlContext.createDataFrame([['MS','fair',9],['UP','fair',8],['Karnataka','fair',9],['Raj','poor',3],['Bihar','poor',2],['Mizoram','poor',2],['Assam','moderate',7],['Kerala','fair',8]],['state','emp_remark','emp_index'])

# india_employment.show()
# +---------+----------+---------+
# |    state|emp_remark|emp_index|
# +---------+----------+---------+
# |       MS|      fair|        9|
# |       UP|      fair|        8|
# |Karnataka|      fair|        9|
# |      Raj|      poor|        3|
# |    Bihar|      poor|        2|
# |  Mizoram|      poor|        2|
# |    Assam|  moderate|        7|
# |   Kerala|      fair|        8|
# +---------+----------+---------+

#count
new_india_emp = india_employment.groupBy('emp_remark').count()
# new_india_emp.show()
# +----------+-----+
# |emp_remark|count|
# +----------+-----+
# |      poor|    3|
# |      fair|    4|
# |  moderate|    1|
# +----------+-----+

#avg
new_india_emp = india_employment.groupBy('emp_remark').agg({'emp_index' : 'mean'})
# new_india_emp.show()
# +----------+------------------+
# |emp_remark|    avg(emp_index)|
# +----------+------------------+
# |      poor|2.3333333333333335|
# |      fair|               8.5|
# |  moderate|               7.0|
# +----------+------------------+

#filter without udf
sample_filtered_df = new_india_emp.filter(new_india_emp.emp_remark=='moderate')
# sample_filtered_df.show()
# +----------+--------------+
# |emp_remark|avg(emp_index)|
# +----------+--------------+
# |  moderate|           7.0|
# +----------+--------------+


#filter with udf
def return_filter_expr(emp_remark):
     return emp_remark == 'moderate'


new_filtered_df = new_india_emp.filter(functions.udf(return_filter_expr,BooleanType())(new_india_emp['emp_remark']))

# py4j.protocol.Py4JJavaError: An error occurred while calling o56.filter.
# : java.lang.ClassCastException: org.apache.spark.sql.catalyst.plans.logical.Project cannot be cast to org.apache.spark.sql.catalyst.plans.logical.Aggregate
