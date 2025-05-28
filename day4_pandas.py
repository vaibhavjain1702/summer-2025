# pandas is used for analyzing, cleaning, exploring, and manipulating data.

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}   

myvar = pd.DataFrame(mydataset)
print(myvar)

print(pd.__version__)

# locate row 
print(myvar.loc[0])  # Access the first row

# named indexes
df= pd.DataFrame(mydataset, index=["a", "b", "c"])
print(df)

print(df.loc["a"])  # Access the row with index "a"

df=pd.read_csv('train.csv')  # Assuming 'data.csv' is in the same directory
print(df.head())  # Display the first few rows of the DataFrame
# print(df.to_string())  Display the entire DataFrame as a string

pd.options.display.max_rows
print(pd.options.display.max_rows)  # Set the maximum number of rows to display

print(df.tail())  # Display the last few rows of the DataFrame
print(df.info())  # Display a concise summary of the DataFrame

# counting missing values
print(df.isnull().sum())  # Count missing values in each column

# filtering passengers older than 30
old_passengers=df[df['Age']>30]
print(old_passengers) 

# sorting by fare
sorted_df = df.sort_values(by='Fare', ascending=False)
print(sorted_df.head())  # Display the first few rows of the sorted DataFrame