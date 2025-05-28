import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('train.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.info())
print(df.isnull().sum())
print(df.value_counts())
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
