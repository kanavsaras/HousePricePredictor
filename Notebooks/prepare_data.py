import pandas as pd
from sklearn.model_selection import train_test_split
path = r"C:\Users\Lenovo\Desktop\Phase-1 Projects\House Price Predictior Model\Data\train.csv"
df = pd.read_csv(path,sep = ',')
X = df.drop('Price',axis=1)
y = df['Price']

print("Features (X):")
print(X.iloc[:2])

print("\nTarget (y):")
print(y.iloc[:2])

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)

print(f"\nTotal houses: {len(df)}")
print(f"Training houses: {len(X_train)}")
print(f"Testing houses : {len(X_test)}")

print("\nTraining set first row:")
print(X_train.iloc[0])
print(y_train.iloc[0])