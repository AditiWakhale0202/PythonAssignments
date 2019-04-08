from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext

conf = SparkConf().setAppName("myApp")
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

#create a sample dataframe
india_states = sqlContext.createDataFrame([['MS','orange',11],['UP','green',9],['Karnataka','white',13],['Raj','red',12], ['Kerala','white',13]],['state','color','index'])
india_states.show()
# +---------+------+-----+
# |    state| color|index|
# +---------+------+-----+
# |       MS|orange|   11|
# |       UP| green|    9|
# |Karnataka| white|   13|
# |      Raj|   red|   12|
# |   Kerala| white|   13|
# +---------+------+-----+

# group on the basis of color and index
df_grouped = india_states.groupBy(india_states.color,india_states.index).count()
df_grouped.show()
# +------+-----+-----+
# | color|index|count|
# +------+-----+-----+
# | green|    9|    1|
# | white|   13|    2|
# |   red|   12|    1|
# |orange|   11|    1|
# +------+-----+-----+


# create another dataframe
shape_color_df = sqlContext.createDataFrame([['green','triangle'],['white','circle'],['red','square'],['orange','rhombus']],['color','shape'])
shape_color_df.show()
# +------+--------+
# | color|   shape|
# +------+--------+
# | green|triangle|
# | white|  circle|
# |   red|  square|
# |orange| rhombus|
# +------+--------+


# inner join
df_joined = shape_color_df.join(df_grouped, shape_color_df.color == df_grouped.color,'inner')
df_joined.show()
# +------+--------+------+-----+-----+
# | color|   shape| color|index|count|
# +------+--------+------+-----+-----+
# |orange| rhombus|orange|   11|    1|
# | green|triangle| green|    9|    1|
# |   red|  square|   red|   12|    1|
# | white|  circle| white|   13|    2|
# +------+--------+------+-----+-----+

# left outer join
df_joined = shape_color_df.join(df_grouped, shape_color_df.color == df_grouped.color,'left_outer')
df_joined.show()
# +------+--------+------+-----+-----+
# | color|   shape| color|index|count|
# +------+--------+------+-----+-----+
# |orange| rhombus|orange|   11|    1|
# | green|triangle| green|    9|    1|
# |   red|  square|   red|   12|    1|
# | white|  circle| white|   13|    2|
# +------+--------+------+-----+-----+

# left outer join with changed order of dataframes
joined_df = df_grouped.join(shape_color_df, df_grouped.color == shape_color_df.color,'left_outer')
joined_df.show()
# +------+-----+-----+------+--------+
# | color|index|count| color|   shape|
# +------+-----+-----+------+--------+
# |orange|   11|    1|orange| rhombus|
# | green|    9|    1| green|triangle|
# |   red|   12|    1|   red|  square|
# | white|   13|    2| white|  circle|
# +------+-----+-----+------+--------+

