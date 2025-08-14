# Databricks notebook source
# MAGIC %md
# MAGIC Trial Notebook for Notebook Automation using Widgets

# COMMAND ----------

# Sample code to print result
def addition(a,b):
  return a+b

sum_no = addition(10,12)
print(sum_no)

# COMMAND ----------

dbutils.notebook.exit(str(sum_no))