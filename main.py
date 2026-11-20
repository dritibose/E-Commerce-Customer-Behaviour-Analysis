import pandas as pd
df=pd.read_csv("data.csv")

# print(df)

''''''

#Total orders
total_orders=df.shape
print("Total Orders: ", total_orders[0],"\n")

# COMPLETED ORDERS
completed_orders=df[df["Order_Status"]=="Completed"]
print("NUmber of completed orders: ", completed_orders.shape[0],"\n")

#Total Revenue
Total_revenue=completed_orders["Order_Value"].sum()
print("\n","Total Revenue: ", Total_revenue,"\n")

