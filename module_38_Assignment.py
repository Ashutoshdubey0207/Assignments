import seaborn as sns
import matplotlib.pyplot as plt
'''Que 1: Name any five plots that we can plot using the Seaborn library. Also, state the uses of each plot.'''
'''Ans=> Seaborn Plots and Uses
Scatterplot: Shows the relationship between two numeric variables using dots.
Lineplot: Shows how a numeric value changes over time or a continuous sequence.
Barplot: Compares a numeric value across different groups or categories.
Boxplot: Shows the range, median, and spread of data, plus any outliers.
Histogram: Shows how often different values happen within a single numeric column.'''


'''Que 2: Load the "fmri" dataset using the load_dataset function of seaborn. Plot a line plot using 
x = "timepoint" and y = "signal" for different events and regions.'''
data = sns.load_dataset("fmri")
data.plot(x="timepoint",y="signal")
plt.show()


'''Que 3: Load the "titanic" dataset using the load_dataset function of seaborn. Plot two box plots using 
x = 'pclass', y = 'age' and y = 'fare'.'''

import seaborn as sns
import matplotlib.pyplot as plt

ds2 = sns.load_dataset("titanic")

plt.figure(figsize=(10, 8))

ax1 = plt.subplot(2, 1, 1)
ds2.plot(x="pclass", y="age", kind="box", ax=ax1)
ax1.set_title("Pclass vs Age")

ax2 = plt.subplot(2, 1, 2)
ds2.plot(x="pclass", y="fare", kind="box", ax=ax2)
ax2.set_title("Pclass vs Fare")

plt.tight_layout()
plt.show()

'''Que 4: Use the "diamonds" dataset from seaborn to plot a histogram for the 'price' column. Use the hue
parameter for the 'cut' column of the diamonds dataset.'''
ds4 = sns.load_dataset("diamonds")
sns.histplot(ds4,x="price",hue="cut")
plt.show()

'''Que 5: Use the "iris" dataset from seaborn to plot a pair plot. Use the hue parameter for the "species" column
of the iris dataset.'''
ds5 = sns.load_dataset("iris")
sns.pairplot(ds5,hue="species")
plt.show()

'''Que 6: Use the "flights" dataset from seaborn to plot a heatmap.'''
ds6 = sns.load_dataset("flights")
clean_ds6 = ds6.corr(numeric_only=True)
sns.heatmap(clean_ds6,cmap="coolwarm")
plt.show()



