# 1. Read a CSV file of sales data and calculate total revenue.
# Revenue=Quantity Sold×Unit Price−Discount

import pandas as pd
import numpy as np
df = pd.read_csv(r"C:/Users/gayat/Downloads/sales_data.csv")
print(df.head())

col = df.columns
print("columns are:", col)

NullValues = df.isnull().sum()
print("Null values are:", NullValues)


df['Revenue'] = (df['Quantity_Sold'] * df['Unit_Price']) - df['Discount']

#total revenue
total_revenue = df['Revenue'].sum()

print("Total Revenue:", total_revenue)