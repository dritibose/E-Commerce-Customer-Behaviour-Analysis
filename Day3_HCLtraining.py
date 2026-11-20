import pandas as pd

df=pd.read_csv("66.csv")

# print(df)
# print(df.head(6),"\n")# first 6 rows

# print(df.tail(4),"\n")#last four rows
# print(df.shape,"\n")# number of rows and columnns
# print(df.columns,"\n")#column names
# print(df.info(),"\n")
#
# print(df["Order_Value"])
# print(df[["Customer_ID", "City", "Order_Value"]])

# completed=df[df["Order_Status"]=="Completed"]
# print(completed)

# # filtering out values with conditions
# expensive=df[df["Order_Value"]>3500]
# cheap=df[df["Order_Value"]<2000]
# print(expensive)
# print(cheap)

# delhi=df[df["City"]=="Delhi"]
# mumbai=df[df["City"]=="Mumbai"]
# chennai=df[df["City"]=="Chennai"]
# print(delhi)
# print(mumbai)
# print(chennai)

# result=df[(df["Order_Value"]>5000) & (df["City"]=="Delhi")]
# print(result,"\n", "People from Delhi who have spent more than 5000")


#mean ,axx min count median std
# print("Mean of Order Value:", df["Order_Value"].mean())
# print("Max of Order Value:", df["Order_Value"].max())
# print("Min of Order Value:", df["Order_Value"].min())
# print("Sum of Order Value:", df["Order_Value"].sum())

# print("Count of Order Value:", df["Order_Value"].count())
# print("Median of Order Value:", df["Order_Value"].median())
# print("Standard Deviation of Order Value:", df["Order_Value"].std())


'''#GROUP BYYYY
sales = df.groupby("Category")["Order_Value"].sum()

print(sales)
ratings = df.groupby("City")["Rating"].mean()

print(ratings)

sales = df.groupby("Category")["Order_Value"].sum()

print(sales.sort_values())'''

"""a=df["Category"].nunique()# number of unique products
b=df["Category"].unique()
c=df["Category"].value_counts()#how mant times the product got purchased

print(a,"nunique")
print(b,"unique")
print(c,"value count")"""

"""
d=df[df["Order_Value"]>3000]
print(d)"""


# Ilock= integer lock- for pirnting one data of a by index
"""e=df.iloc[3] iloc can access the data with both custom index and changed index , only with custom indexes when they integer
f=df.loc[4]  cant access with previous/original index after changin
print(e,f)"""

'''g=df.nlargest(3,"Order_Value") largest three values
h=df.nsmallest(4,"Order_Value") smallest four values
print( g,h)'''


i=df["Order_Value"].drop_duplicates().nlargest(10)
print(i)


'''
highest_selling_category=df.groupby("Category")["Order_Value"].sum()
print("Highest selling category: ", highest_selling_category.max())'''



'''sales_by_cities=df.groupby("City")["Order_Value"].sum()
print("Sales by Cities: ", sales_by_cities)
'''



'''duplicated=df[df.duplicated()].count()
delete=df.drop_duplicates()

print("Number of duplicate rows: ", duplicated)'''

# outliers-- detect using  iqr
q1=df["Order_value"].quantile(0.25)
q3=df["Order_value"].quantile(0.75)

iqr=q3-q1
print(iqr)
lower=q1-1.5+iqr
upper=q3+1.5+iqr

#Z score
df["Z_score"]=
