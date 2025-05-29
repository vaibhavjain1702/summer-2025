import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('train.csv')
print(df.head()) # Display the first few rows of the DataFrame
print(df.info()) # Get information about the dataset, including data types and non-null counts
print(df.describe()) # Generate descriptive statistics for numerical columns
print(df.isnull().sum()) # Check for missing values in each column
print(df.value_counts()) # Count unique values in the DataFrame
# count of survivors by gender visualization
sns.countplot(x='Survived',hue='Sex',data=df)
plt.show()
# fare distribution by class
sns.boxplot(x='Pclass',y='Fare',data=df)
plt.title('Fare Distribution by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.show()
# missing values heatmap
sns.heatmap(df.isnull(),cbar=False,cmap='viridis')
plt.title('Missing Values Heatmap')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.show()

# day 7 update: cleaning and post-eda tasks

#fill missing values in 'Age' with the median
df['Age'].fillna(df['Age'].median(), inplace=True)
#fill missing values in 'Embarked' with the mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
#drop 'Cabin' column due to high number of missing values
df.drop('Cabin', axis=1, inplace=True)

# recheck .isnull().sum()
print(df.isnull().sum())  # Check for missing values again after cleaning

# save cleaned csv
df.to_csv('cleaned_titanic_data.csv', index=False)

# heatmap to confirm no missing values
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap After Cleaning')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.show()

# what does cbar mean in sns.heatmap?
# In `sns.heatmap`, the parameter `cbar` stands for "color bar." It is a boolean parameter that determines whether to display a color bar alongside the heatmap. The color bar provides a reference for the values represented by the colors in the heatmap, helping to interpret the data visually. If `cbar=True`, the color bar will be shown; if `cbar=False`, it will not be displayed. In your code, `cbar=False` means that the heatmap will be displayed without a color bar.