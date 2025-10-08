import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

try:
    data = pd.read_csv(input("CSV file path: "))
    print("\n=> Data loaded.\n")
except Exception as e:
    print("\n=> Error:", e)
    exit()


x = data.iloc[:, 0].values.reshape(-1, 1)
y = data.iloc[:, 1].values

model = LinearRegression().fit(x, y)
print("\n=> Training Finished By Given Data.\n")

print("\n=> Predicting By Linear Regression...\n")
target = 100
predicted_x = (target - model.intercept_) / model.coef_[0]

print("\n=> Printing Predicted Data.\n")
print(f"\n{data.columns[1]} will reach {target} at {data.columns[0]} ≈ {predicted_x:.2f}\n")

print("\n=> Plotting Data...\n")

plt.scatter(x, y)
plt.plot(x, model.predict(x), color='red')
plt.axhline(y=target, color='green', linestyle='--')
plt.axvline(x=predicted_x, color='purple', linestyle='--')
plt.xlabel(data.columns[0])
plt.ylabel(data.columns[1])
plt.title('Prediction')
plt.grid(True)
plt.show()
