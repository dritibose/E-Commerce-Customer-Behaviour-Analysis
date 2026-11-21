import pandas as pd
df=pd.read_csv("data.csv")


#Duplicates
r=df.duplicated().sum()
print("Duplicate rows: ",r)
df=df.drop_duplicates()

df.isna().sum()
df[df.isna().any(axis=1)]
cleaned_df=df.dropna()

#Handling Captalization
print(df["Category"].unique())
df["Category"]=df["Category"].str.strip()
df["Category"]=df["Category"].str.title()
print(df["Category"].unique())

df["Customer_Group"]=df["Customer_Group"].str.strip()
df["Customer_Group"]=df["Customer_Group"].str.title()


df["City"]=df["City"].str.strip()
df["City"]=df["City"].str.title()



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


#Return Rate
Returning_orders=df[df["Order_Status"]=="Returned"].shape[0]
total_customers=df.shape
return_rate=(Returning_orders/total_customers[0])*100
print("Return Rate: ", return_rate,"%\n")


#category wise rating
cat_rating=df.groupby("Category")["Rating"].mean()
print("Average rating accross the categories: \n", cat_rating)

print("\n","Highest rating in category: ", cat_rating.idxmax(),"\n")


#Average delivery time
avg_delivery=completed_orders["Delivery_Days"].mean()
print("Average Delivery Days: ", avg_delivery,"\n")


#Correlation



df = pd.read_csv("data.csv")

# Calculate correlation
correlation = df["Delivery_Days"].corr(df["Rating"])

print("Correlation:", correlation,"\n")

