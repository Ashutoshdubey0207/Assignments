'''Q1. Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
scatter plot for age and fare columns in the titanic dataset.'''
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



ds1 = sns.load_dataset("titanic")
fig = go.Figure()
fig.add_trace(go.Scatter(x=ds1["age"],y=ds1["fare"],mode='markers'))
fig.show()

'''Q2. Using the tips dataset in the Plotly library, plot a box plot using Plotly express.'''

ds2 = px.data.tips()
fig = px.box(ds2,y="total_bill")
fig.show()


'''Q3. Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
column with the color parameter.'''

ds3 = px.data.tips()
fig = px.histogram(ds3,x="sex",y="total_bill",pattern_shape="smoker",color="day")
fig.show()


'''Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
the color parameter.
Note: Use "sepal_length", "sepal_width", "petal_length", "petal_width" columns only with the
dimensions parameter.'''

import plotly.express as px

# Load the built-in iris dataset from Plotly Express
df = px.data.iris()

# Create the scatter matrix plot
fig = px.scatter_matrix(
    df,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species"
)

# Display the interactive plot
fig.show()



'''Q5. What is Distplot? Using Plotly express, plot a distplot.'''
'''A distplot (distribution plot) is a statistical visualization tool used to analyze the 
univariate distribution of a continuous dataset. It typically combines multiple representations 
of data into a single figure—such as a histogram to show frequency counts, a kernel density 
estimation (KDE) line to show the continuous probability density, and a rug plot to display 
individual data points'''

# 1. Load a built-in sample dataset from Plotly Express
df = px.data.tips()

# 2. Plot the distribution plot using px.histogram
fig = px.histogram(
    df, 
    x="total_bill",              # The numerical column to analyze
    color="sex",                 # Optional: group distribution by a categorical column
    marginal="rug",              # Adds a rug plot on the margin of the axis
    histnorm="probability density", # Norms the histogram to display probability density                   # Overlays a Kernel Density Estimation line curve
)

# 3. Render the interactive plot
fig.show()

