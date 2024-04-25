import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('medical_examination.csv')

# Task 1: Add an overweight column
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (df['BMI'] > 25).astype(int)

# Task 2: Normalize the data
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Task 3: Convert data into long format and create a catplot
df_catplot = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'alco', 'active', 'smoke', 'overweight'])
plt.figure(figsize=(10, 8))
sns.catplot(x='variable', hue='value', col='cardio', kind='count', data=df_catplot)
plt.show()

# Task 4: Clean the data
df = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

# Task 5: Create a correlation matrix and plot using seaborn's heatmap
correlation_matrix = df.corr()
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.1f', cmap='coolwarm', mask=mask)
plt.title('Correlation Matrix')
plt.show()
