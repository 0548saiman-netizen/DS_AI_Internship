# Task 1

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

data = {
    'Price': [250000, 300000, 450000, 150000, 600000, 350000, 800000,
              275000, 500000, 650000, 225000, 400000, 550000, 720000, 180000],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Bangalore', 'Mumbai', 'Bangalore',
             'Chennai', 'Delhi', 'Bangalore', 'Chennai', 'Mumbai', 'Delhi', 'Bangalore', 'Chennai'],
    'Bedrooms': [3,2,4,2,4,3,5,2,3,4,1,3,4,4,2],
    'Bathrooms': [2,2,3,1,3,2,4,2,3,3,1,2,2,3,1],
    'Area_sqft': [1500,1200,2100,800,2400,1600,3000,1100,2000,2300,700,1800,2200,2600,900]
}

df = pd.DataFrame(data)
plt.figure(figsize=(10,6))
sns.histplot(df['Price'], kde=True, bins=10, color='skyblue')
plt.title('Distribution of Housing Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

price_skewness = skew(df['Price'])
price_kurtosis = kurtosis(df['Price'])

print(f"Skewness of Price: {price_skewness:.2f}")
print(f"Kurtosis of Price: {price_kurtosis:.2f}")

plt.figure(figsize=(8,5))
sns.countplot(data=df, x='City', order=df['City'].value_counts().index, palette='viridis')
plt.title('Number of Houses per City')
plt.xlabel('City')
plt.ylabel('Count')
plt.show()

# Task 2

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Price': [250000, 300000, 450000, 150000, 600000, 350000, 800000,
              275000, 500000, 650000, 225000, 400000, 550000, 720000, 180000],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Bangalore', 'Mumbai', 'Bangalore',
             'Chennai', 'Delhi', 'Bangalore', 'Chennai', 'Mumbai', 'Delhi', 'Bangalore', 'Chennai'],
    'Bedrooms': [3,2,4,2,4,3,5,2,3,4,1,3,4,4,2],
    'Bathrooms': [2,2,3,1,3,2,4,2,3,3,1,2,2,3,1],
    'Area_sqft': [1500,1200,2100,800,2400,1600,3000,1100,2000,2300,700,1800,2200,2600,900]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Area_sqft', y='Price', hue='City', palette='deep', s=100)
plt.title('Price vs House Area (sqft)')
plt.xlabel('Area (sqft)')
plt.ylabel('Price')
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='City', y='Price', palette='pastel')
plt.title('Price Distribution by City')
plt.xlabel('City')
plt.ylabel('Price')
plt.show()

# Task 3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Price': [250000, 300000, 450000, 150000, 600000, 350000, 800000,
              275000, 500000, 650000, 225000, 400000, 550000, 720000, 180000],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Bangalore', 'Mumbai', 'Bangalore',
             'Chennai', 'Delhi', 'Bangalore', 'Chennai', 'Mumbai', 'Delhi', 'Bangalore', 'Chennai'],
    'Bedrooms': [3,2,4,2,4,3,5,2,3,4,1,3,4,4,2],
    'Bathrooms': [2,2,3,1,3,2,4,2,3,3,1,2,2,3,1],
    'Area_sqft': [1500,1200,2100,800,2400,1600,3000,1100,2000,2300,700,1800,2200,2600,900]
}

df = pd.DataFrame(data)

corr_matrix = df[['Price', 'Bedrooms', 'Bathrooms', 'Area_sqft']].corr()
print("Correlation Matrix:\n", corr_matrix)
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

high_corr = []
for i in corr_matrix.columns:
    for j in corr_matrix.columns:
        if i != j and corr_matrix.loc[i,j] > 0.8:
            high_corr.append((i,j,corr_matrix.loc[i,j]))

print("Highly correlated variables (corr > 0.8):")
for pair in set(high_corr):
    print(f"{pair[0]} and {pair[1]}: {pair[2]:.2f}")
plt.figure(figsize=(8,5))
sns.boxplot(df['Price'], color='lightcoral')
plt.title('Boxplot of Housing Prices')
plt.xlabel('Price')
plt.show()


