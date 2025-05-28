# matplotlib
# it is used to create visualizations in Python.

import matplotlib.pyplot as plt
import numpy as np

xpoints= np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()

# plotting without a line
plt.plot(xpoints, ypoints, 'o')
plt.show()

# we can do the same for multiple points

# if we do not specify xpoints it will get default values as 0, 1, 2, 3, 4, 5
ypoints=np.array([3, 8, 1, 10, 5])
plt.plot(ypoints)
plt.show()

# linestyle is used to change the style of the line
plt.plot(ypoints, linestyle='dashed')
plt.show()

different_styles = ['solid', 'dashed', 'dashdot', 'dotted']
for style in different_styles:
    plt.plot(ypoints, linestyle=style)
plt.show()

# linestyle can be written as ls
# dotted can be written as ':'
# dashed can be written as '--'

colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
for color in colors:
    plt.plot(ypoints, linestyle='dashed', color=color)
plt.show()

# color can also be written as c

# hexadecimal colors can also be used
hex_colors = ['#FF5733', '#33FF57', '#3357FF', '#F0F0F0']
for hex_color in hex_colors:
    plt.plot(ypoints, linestyle='dashed', color=hex_color)
plt.show()

# linewidth can be used to change the width of the line
plt.plot(ypoints, linewidth=20.5)
plt.show()

# we can do the same for multiple lines too

# we can also label the lines
# we can also create a title for the plot

# font is also customizable
x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])

font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}

plt.title('Sports Watch Data', fontdict=font1)
plt.xlabel('Average Pulse', fontdict=font2)
plt.ylabel('Calorie Burnage', fontdict=font2)

plt.plot(x, y, color='green', linewidth=10)
plt.show()

# you can also change the location of the title
plt.title('Sports Watch Data', loc='left')
plt.plot(x,y)
plt.show()

# displaying multiple plots in a single figure
# plot 1
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,2,1) # row,column,index
plt.plot(x,y)

# plot 2
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(1,2,2) # row,column,index
plt.plot(x,y)
plt.show()

# super title can be added using suptitle()
plt.suptitle("Super Title")
plt.show()

# histogram shows frequency distribution of data
# we make a histogram using hist() function

# random data generation
x=np.random.normal(170, 10, 250)  # mean=170, std=10, n=250
print(x)
plt.hist(x)
plt.show()

# now onto bar charts
# bar charts are used to represent categorical data
# bar() function is used to create bar charts
# horizontal bar charts can be created using barh() function
# default width of bar is 0.8
# bar chart example
x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])
plt.bar(x, y)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()
# horizontal bar chart example
plt.barh(x, y)
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart Example')
plt.show()
# bar chart with custom width
plt.bar(x, y, width=0.5)  # width can be set to any value
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart with Custom Width')
plt.show()
# bar chart with custom color
plt.bar(x, y, color='orange')  # color can be set to any value
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart with Custom Color')
plt.show()

# seaborn
# seaborn is a library built on top of matplotlib that provides a high-level interface for drawing attractive statistical graphics
import seaborn as sns
sns.set_theme()
tips=sns.load_dataset('tips')
sns.relplot(
    data=tips,
    x='total_bill',y='tip',col='time',  # color by time of day
    hue='smoker', style='smoker', size='size',  # color by smoker status, style by smoker status, size by size of party
)
plt.show()

# understanding seaborn
# it is used to create visualizations in Python
import pandas as pd
df=pd.read_csv('train.csv')
# plotting age histogram
sns.histplot(df['Age'], kde=True, bins=30)  # kde=True adds a kernel density estimate
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

#countplot of survived vs gender
sns.countplot(data=df, x='Survived', hue='Sex')
plt.title('Survival Count by Gender')
plt.xlabel('Survived')
plt.ylabel('Count') 
plt.legend(title='Gender', labels=['Female', 'Male'])
plt.show()

# boxplot of fare vs pclass
sns.boxplot(data=df, x='Pclass', y='Fare', hue='Survived')
plt.title('Fare Distribution by Passenger Class and Survival')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')  
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

# heatmap of correlation matrix
corr_matrix = df.select_dtypes(include=['number']).corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()