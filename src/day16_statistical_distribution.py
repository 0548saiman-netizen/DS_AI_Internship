# Task 1

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
np.random.seed(42)

heights = np.random.normal(loc=170, scale=10, size=1000)
df_heights = pd.DataFrame({'Human Heights': heights})

incomes = np.random.exponential(scale=50000, size=1000) + 20000
df_incomes = pd.DataFrame({'Household Incomes': incomes})

scores = 100 - np.random.exponential(scale=10, size=1000)
scores = np.clip(scores, 0, 100)
df_scores = pd.DataFrame({'Test Scores': scores})

def plot_histogram_kde(df, column, title):
    plt.figure(figsize=(8,5))
    sns.histplot(df[column], kde=True, bins=30, color='skyblue')
    
    mean_val = df[column].mean()
    median_val = df[column].median()
    
    plt.axvline(mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.2f}')
    plt.axvline(median_val, color='green', linestyle='-', label=f'Median: {median_val:.2f}')
    
    plt.title(title)
    plt.legend()
    plt.show()
    
    print(f"{title} -> Mean: {mean_val:.2f}, Median: {median_val:.2f}")
    if mean_val > median_val:
        print("Observation: Right-Skewed\n")
    elif mean_val < median_val:
        print("Observation: Left-Skewed\n")
    else:
        print("Observation: Approximately Normal\n")

plot_histogram_kde(df_heights, 'Human Heights', 'Human Heights (Normal)')
plot_histogram_kde(df_incomes, 'Household Incomes', 'Household Incomes (Right-Skewed)')
plot_histogram_kde(df_scores, 'Test Scores', 'Test Scores (Left-Skewed)')


# Task 2

import pandas as pd
import numpy as np

np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=100)  # mean=170cm, std=10
df = pd.DataFrame({'Height': heights})

mean_height = df['Height'].mean()
std_height = df['Height'].std()

print(f"Mean (μ): {mean_height:.2f}")
print(f"Standard Deviation (σ): {std_height:.2f}\n")

df['z_score'] = (df['Height'] - mean_height) / std_height
outliers = df[np.abs(df['z_score']) > 3]
print("Rows with Z-score > 3 or < -3 (Outliers):")
print(outliers)

# Task 3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
np.random.seed(42)

incomes = np.random.exponential(scale=50000, size=10000) + 20000  # right-skewed
df = pd.DataFrame({'Income': incomes})

plt.figure(figsize=(8,5))
sns.histplot(df['Income'], bins=50, kde=True, color='orange')
plt.title("Original Income Distribution (Right-Skewed)")
plt.show()

sample_means = []

for _ in range(1000):
    sample = df['Income'].sample(n=30, replace=True)
    sample_means.append(sample.mean())

df_means = pd.DataFrame({'Sample Means': sample_means})

plt.figure(figsize=(8,5))
sns.histplot(df_means['Sample Means'], bins=30, kde=True, color='skyblue')
plt.title("Distribution of Sample Means (CLT in Action)")
plt.xlabel("Sample Mean")
plt.show()

print(f"Mean of sample means: {df_means['Sample Means'].mean():.2f}")
print(f"Standard deviation of sample means: {df_means['Sample Means'].std():.2f}")
