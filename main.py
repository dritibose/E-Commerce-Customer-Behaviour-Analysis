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

#Category Analysis
category_revenue=completed_orders.groupby("Category")["Order_Value"].sum()
print("Revenue by Category: ")
print(category_revenue,"\n")


#City and Orders
print("Highest selling Category: ", category_revenue.idxmax(),"\n")

#city Analysis
City_sales=completed_orders.groupby("City")["Order_Value"].sum()


print("Highest selling City ", City_sales.idxmax(),"\n")
print("Sales by city: \n", City_sales,"\n")

city_order=df.groupby("City")["Order_ID"].count()
print("Order by cities: " ,city_order,"\n")
