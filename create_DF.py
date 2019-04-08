import pyspark
import pyspark.sql.functions
from pyspark import SparkConf, SparkContext, SQLContext,HiveContext

conf = SparkConf().setAppName('myApp')

sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

import datetime
#query = "select * from wiki_Wiki_PageViewsDaily.flow1_groupby_3"
dataframe = sqlContext.createDataFrame([[datetime.date(2017,1,1),datetime.datetime(2017,11,1,18,02)],[datetime.date(2017,1,1),datetime.datetime(2017,11,1,18,02)],[datetime.date(2017,1,1),datetime.datetime(2017,11,1,18,02)]],['datecol','timestampcol'])

dataframe.show()
print dataframe


# DEFINE HELPER FUNCTIONS HERE
def yourHelperFunction(df, targetCols):

    import datetime
    def add_five_days(col_name):
        print col_name
        return col_name+datetime.timedelta(days=5)
    print(df)
    actual_df = df
    for col_name in targetCols:
        actual_df = actual_df.withColumn(col_name, add_five_days(df[col_name]))
    return actual_df


yourHelperFunction(dataframe,['datecol'])