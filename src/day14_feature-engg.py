# Task 1

import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "Transmission": ["Automatic", "Manual", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red", "Blue"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Label Encoding (Ordinal/Binary)

le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])


# One-Hot Encoding (Nominal)

df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nEncoded Data:")
print(df)

# Task 2

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
data = {
    "Age": [22, 25, 30, 35, 40, 45, 50],
    "Salary": [20000, 25000, 40000, 60000, 80000, 100000, 120000]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Standardization
scaler_standard = StandardScaler()
df_standardized = pd.DataFrame(
    scaler_standard.fit_transform(df),
    columns=df.columns
)
print("\nStandardized Data:")
print(df_standardized)

# Normalization (MinMax)
scaler_minmax = MinMaxScaler()
df_normalized = pd.DataFrame(
    scaler_minmax.fit_transform(df),
    columns=df.columns
)
print("\nNormalized Data:")
print(df_normalized)

# Plot Histogram Before & After
plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.hist(df["Salary"])
plt.title("Original Salary")

plt.subplot(1,3,2)
plt.hist(df_standardized["Salary"])
plt.title("Standardized Salary")

plt.subplot(1,3,3)
plt.hist(df_normalized["Salary"])
plt.title("Normalized Salary")
plt.tight_layout()
plt.show()

# Task 3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

np.random.seed(42)

X = np.random.uniform(-5, 5, 200).reshape(-1, 1)
y = 4 + 3*X + 2*(X**2) + np.random.randn(200, 1)*4
y = y.ravel()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_linear)

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print("R² Score (Linear Model):", round(r2_linear, 4))
print("R² Score (Polynomial Model - Degree 2):", round(r2_poly, 4))

X_range = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)
y_linear_curve = linear_model.predict(X_range)
X_range_poly = poly.transform(X_range)
y_poly_curve = poly_model.predict(X_range_poly)

plt.figure(figsize=(8,6))
plt.scatter(X, y, color='gray', alpha=0.5, label="Actual Data")
plt.plot(X_range, y_linear_curve, color='red', label="Linear Model")
plt.plot(X_range, y_poly_curve, color='blue', label="Polynomial Model (degree=2)")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.show()
