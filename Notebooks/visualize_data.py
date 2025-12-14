import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\Phase-1 Projects\House Price Predictior Model\Data\train.csv")
path = r"C:\Users\Lenovo\Desktop\Phase-1 Projects\House Price Predictior Model\Data\train.csv"
df = pd.read_csv(path,sep = ',')
plt.figure(figsize=(10,6))
plt.scatter(df['SquareFeet'], df['Price'])
plt.xlabel('size_sqft')
plt.ylabel('price')
plt.title('Size vs Price')
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df['Age'], df['Price'])
plt.xlabel('age_years')
plt.ylabel('price')
plt.title('age vs Price')
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df['LocationScore'],df['Price'])
plt.xlabel('LocationScore')
plt.ylabel('price')
plt.show()

print(df.corr())
print(df.head())
print(df.columns.to_list())