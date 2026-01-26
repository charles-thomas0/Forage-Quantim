## Script to manipulate three data files into one

import pandas as pd 

# Three loaded files

df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

# Concat

df = pd.concat([df0, df1, df2], ignore_index=True)

# Filter product

filtered_df = df[df["product"] == "pink morsel"].copy()

# Remove $

filtered_df["price"] = filtered_df["price"].replace(r"[\$,]", "", regex=True).astype(float)

# Combine Quantity & Price

filtered_df["sales"] = filtered_df["price"] * filtered_df["quantity"]

# Filter Columns

filtered_df = filtered_df[["sales", "date", "region"]]


# Output file

filtered_df.to_csv("data/output.csv", index=False)
