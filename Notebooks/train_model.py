import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
path = r"C:\Users\Lenovo\Desktop\Phase-1 Projects\House Price Predictior Model\Data\train.csv"
df = pd.read_csv(path,sep = ',')
X = df.drop('Price',axis=1)
y = df['Price']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)

print("Creating model....")
model = LinearRegression()
model.fit(X_train,y_train)
print("Training complete!")

print("\n learned Weights: ")
for feature,weight in zip(X.columns,model.coef_):
    print(f"{feature}: ${weight:,.2f} per unit")
print(f"\nBase price (intercept): ${model.intercept_:,.2f}")

print("\nMaking Predictions on Test data....")
predictions = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test,predictions))
r2 = r2_score(y_test,predictions)

print("\nModel Performance:")
print(f" RMSE : ${rmse:,.2f}")
print(f" R_sq Score: {r2:,.4f}")

print("\n Test set results:")
print("Actual Price| Predicted Price| Difference ")
print("-"*50)
for actual,predicted in zip(y_test,predictions):
    diff = abs(actual - predicted)
    print(f"${actual:>10,.0f} | ${predicted:>15,.0f} | ${diff:>10,.0f}")
