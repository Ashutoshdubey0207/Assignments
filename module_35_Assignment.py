'''Q1: What is Matplotlib? Why is it used? Name five plots that can be plotted using the Pyplot module of
Matplotlib.
Ans = >
Matplotlib is a popular, open-source Python library used for creating static, animated, and interactive 
data visualizations. It serves as the foundational plotting tool in Python, allowing users to transform raw 
datasets into clear, graphical representations.
Why Matplotlib is Used.
Data Exploration: Spotting trends, patterns, and outliers during exploratory data analysis.
Simplicity via Pyplot: Offering a simple, state-based interface that mirrors MATLAB syntax.
High Customization: Providing complete control over line styles, colors, custom labels, and gridlines.
Publication Quality: Generating high-resolution charts exportable into formats like PNG, PDF, and SVG.
Integration: Seamlessly handling data from core libraries like NumPy and Pandas.

5 Common Plots in the Pyplot Module
Line Plot (plt.plot()): Tracking continuous changes or time-series trends.
Bar Chart (plt.bar()): Comparing counts or values across discrete categorical groups.
Histogram (plt.hist()): Showing the frequency distribution of a continuous dataset.
Scatter Plot (plt.scatter()): Observing relationships or correlations between two variables.
Pie Chart (plt.pie()): Representing proportions and numerical percentages of a whole.
'''


'''Q2: What is a scatter plot? Use the following code to generate data for x and y. Using this generated data
plot a scatter plot.'''
# Note: Also add title, xlabel, and ylabel to the plot.
'''A scatter plot is a type of graph that uses dots to show the relationship between two different numerical 
variables. The horizontal x-axis shows one variable, and the vertical y-axis shows the other. Each dot represents 
a single data point.'''
import numpy as np
import matplotlib.pylab as plt
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))
plt.scatter(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()


'''Q3: Why is the subplot() function used? Draw four line plots using the subplot() function.
Use the following data:'''

x = np.array([0, 1, 2, 3, 4, 5])  
y = np.array([0, 100, 200, 300, 400, 500])
plt.subplot(2,2,1)
plt.plot(x,y)

x1 = np.array([0, 1, 2, 3, 4, 5])  
y1 = np.array([50, 20, 40, 20, 60, 70])
plt.subplot(2,2,2)
plt.plot(x1,y1)


x3 = np.array([0, 1, 2, 3, 4, 5])  
y3 = np.array([10, 20, 30, 40, 50, 60])
plt.subplot(2,2,3)
plt.plot(x3,y3)


x4 = np.array([0, 1, 2, 3, 4, 5]) 
y4 = np.array([200, 350, 250, 550, 450, 150])
plt.subplot(2,2,4)
plt.plot(x4,y4)
plt.show()

'''Q4: What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.'''

''' Bar Graph = a visual way to show categorical data using rectangular bars. The length or height of each bar matches 
the number or value for that specific group. One axis shows the groups, and the other axis shows the numbers.
uses :------------
Compare Groups: It lets people see quickly which group is bigger or smaller.
Show Frequency: It displays counts or totals for discrete items.
Spot Trends: It helps find high points, low points, and general patterns in data.
Make Data Simple: It turns complex tables of numbers into an easy picture
'''
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
plt.bar(company,profit)
plt.show()

'''Q5: What is a box plot? Why is it used? Using the following data plot a box plot.'''
box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
plt.boxplot([box1,box2])
plt.show()