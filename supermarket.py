# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:17:30 2021

@author: Nishant
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.window import Window

spark=SparkSession.builder.appName('Practice').getOrCreate()

df_supermarket=spark.read.format('csv').option('inferSchema','true').option('header','true')\
.option('sep',',').load("file:///SparkCourse/supermarket_sales.csv")

#group by to find the total value of sales for each product line

df_product_line=df_supermarket.groupBy("Product Line").agg(func.round(func.sum("Total"),2).alias("Total Value")).orderBy("Product Line")

df_product_line.show()

# to find the costliest invoice using joins in dataframe

df_costliest=df_supermarket.agg(func.max("Total").alias("Max_Total"))

df_new=df_supermarket.join(df_costliest,df_supermarket.Total==df_costliest.Max_Total,"inner")

df_new.show()

# to find the number of transactions per city using group by

df_orders=df_supermarket.groupBy("City").count().orderBy(func.desc("count"))

df_orders.show()

# to find the costliest and the second costliest invoice for each product line using window functions

windowspec=Window.partitionBy("Product Line").orderBy(func.desc("Total"))

df_window=df_supermarket.withColumn("rank",func.rank().over(windowspec)).filter(func.col("rank")<=2)

df_window.show()


#to find the total amount paid for each of the payment methods
df_payment=df_supermarket.groupBy("Payment").agg(func.round(func.sum("Total"),2).alias("Total Amount"))

df_payment.show()

spark.stop()