import pandas as pd
path = r"C:\Users\Lenovo\Desktop\Phase-1 Projects\House Price Predictior Model\Data\train.csv"
df = pd.read_csv(path,sep = ',')
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())