'''Q1. How can you create a Bokeh plot using Python code?'''
from flask import Flask, render_template
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import figure, show
from bokeh.io import curdoc
import random
# Create data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure
p = figure(title="Simple Bokeh Plot",
           x_axis_label="X-axis",
           y_axis_label="Y-axis")

# Add a line
p.line(x, y, line_width=2)

# Display the plot
show(p)

'''Q2. What are glyphs in Bokeh, and how can you add them to a Bokeh plot? Explain with an example.'''
# Glyphs are the basic visual shapes used by Bokeh to represent data on a plot. They can be circles, lines, rectangles, squares, bars, triangles, etc.

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
p = figure(title="Bokeh Glyph Example",
           x_axis_label="X",
           y_axis_label="Y")

# Add circle glyphs
p.circle(x, y, size=10)
show(p)
p.square(x,y,size=10)
# Display the plot
show(p)
'''Q3. How can you customize the appearance of a Bokeh plot, including the axes, title, and legend?'''
# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# Create plot
p = figure(
    title="Sales Growth",
    x_axis_label="Month",
    y_axis_label="Sales"
)

# Add line
p.line(x, y, line_width=3, legend_label="Sales")

# Customize X-axis
p.xaxis.axis_label_text_font_size = "16pt"
p.xaxis.major_label_text_font_size = "12pt"

# Customize Y-axis differently
p.yaxis.axis_label_text_font_size = "12pt"
p.yaxis.major_label_text_font_size = "16pt"

# Customize title
p.title.text_font_size = "20pt"

# Customize legend
p.legend.location = "top_left"

show(p)



'''Q4. What is a Bokeh server, and how can you use it to create interactive plots that can be updated in
real time?'''
# Create plot
p = figure(
    title="Real-Time Data",
    x_axis_label="Time",
    y_axis_label="Value"
)

# Initial data
x = [0]
y = [random.randint(1, 100)]

# Add line
line = p.line(x, y, line_width=3)

# Function to update data
def update():
    new_x = x[-1] + 1
    new_y = random.randint(1, 100)

    x.append(new_x)
    y.append(new_y)

    line.data_source.data = {
        "x": x,
        "y": y
    }

# Update every 1000 milliseconds
curdoc().add_periodic_callback(update, 1000)

# Add plot to the document
curdoc().add_root(p)

# to run the code = python -m bokeh serve --show app.py

'''Q5. How can you embed a Bokeh plot into a web page or dashboard using Flask or Django?'''

app = Flask(__name__)


@app.route("/")
def home():

    x = [1, 2, 3, 4, 5]
    y = [10, 20, 30, 40, 50]

    p = figure(
        title="Sales Data",
        x_axis_label="Month",
        y_axis_label="Sales"
    )

    p.line(x, y, line_width=3)

    # Get Bokeh plot HTML and JavaScript
    script, div = components(p)

    # BokehJS resources
    bokeh_js = CDN.render()

    return render_template(
        "index.html",
        script=script,
        div=div,
        bokeh_js=bokeh_js
    )


if __name__ == "__main__":
    app.run(debug=True)