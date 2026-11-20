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


#Average Order Value
average_order_value=completed_orders["Order_Value"].mean()
print("Average order value: ", average_order_value,"\n")


#NEW PEOPLE SPENDIND VS RETURNING PEOLPE SPENDING
group_spending=completed_orders.groupby("Customer_Group")["Order_Value"].mean()
print(group_spending,"\n")


repeating_customers=df[df["Customer_Group"]=="Returning"]["Customer_ID"].nunique()
print("NUmber of repeating customers: ", repeating_customers,"\n")

cancelled_orders=df[df["Order_Status"]=="Cancelled"]
print("Number of cancelled orders: ", cancelled_orders,"\n")


#Cancellation rate
cancelled_count=cancelled_orders.shape
total_orders=df.shape
cancellation_rate=(cancelled_count[0]/total_orders[0])*100


print("Cancellation Rate: ", cancellation_rate, "%\n")