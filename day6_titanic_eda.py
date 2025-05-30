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

# day 8 : prepare titanic for modeling

# select input features (like Pclass, Sex, Age, Fare, Embarked)
input_features = df[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
# convert categorical variables to numerical using pd.get_dummies
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df = pd.get_dummies(df, columns=["Embarked"])

# create x (features) and y (target:Survived)
X = df.drop(columns=['Survived'])
y = df['Survived']
# split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# explain everything for day 8:
# In this code, we are preparing the Titanic dataset for modeling by selecting relevant input features and converting categorical variables into numerical format.
# 1. **Selecting Input Features**: We create a new DataFrame `input_features` that includes the columns
#    'Pclass', 'Sex', 'Age', 'Fare', and 'Embarked'. These columns represent various attributes of passengers on the Titanic.
# 2. **Converting Categorical Variables**:
#    - We map the 'Sex' column from string labels ('male' and 'female') to numerical values (0 and 1).
#    - We use `pd.get_dummies` to convert the 'Embarked' column, which contains categorical data about the port of embarkation, into multiple binary columns (one for each unique value in 'Embarked').
# 3. **Creating Features and Target Variables**:
#    - We define `X` as the DataFrame containing all columns except 'Survived', which will be our features for modeling.
#    - We define `y` as the 'Survived' column, which is our target variable indicating whether a passenger survived (1) or not (0).
# 4. **Splitting the Data**: We use `train_test_split` from `sklearn.model_selection` to split the dataset into training and testing sets.
#    - `X_train` and `y_train` will be used to train the model, while `X_test` and `y_test` will be used to evaluate its performance.
# This preparation is essential for building a machine learning model to predict survival on the Titanic based on the selected features.