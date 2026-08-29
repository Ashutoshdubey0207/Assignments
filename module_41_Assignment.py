'''Q1. What is Statistics?'''
# Ans => Statistics is the science of collecting,organizing and analyzing the data.

'''Q2. Define the different types of statistics and give an example of when each type might be used.'''
# Ans => The two major categories of statistics are descriptive statistics and inferential statistics.
# Descriptive statistics summarize or describe the main features of a collected set of data. 
# They do not make conclusions about a larger group; they only describe what is visible in the 
# immediate data.

# Inferential statistics take data from a smaller sample group and use it to make predictions, 
# test hypotheses, or draw conclusions about a larger population.

'''Q3. What are the different types of data and how do they differ from each other? Provide an example of
each type of data.'''
# There are twot types of data in statistics : Qualitative(categorical) and quantitative(numerical)
# qualitative are of two types : Nomirnal and Ordinal
# Nominal Data - Categories with no natural order or ranking. you can count them but cannot sort them from lowest to highest
# Example = eye colors (blue,green , brown)
# Ordinal Data - categories that have a meaningful order or ranking, but the exact distance between the tank is not measurable or equal
# Example = Survey satisfaction ratings (satisfied, neutral,dissatisfied).
# Quantitative DATA - Quantitative data represents numerical values and amount that can be counted or measured.
# Quantitative data is divided into two parts - Discrete and Continuous
# Discrete Data => Countable whole nubers that take specific, distinct integer values and cannot be vroken down into fractions.
# Example: the number of students in the class rule.
# Continuous => Measurable values that can take any value within a finite or infinte range, including decimals and fractions.
# Example : A person's height (eg 1.74 meters)

'''Q4. Categorise the following datasets with respect to quantitative and qualitative data types:
(i) Grading in exam: A+, A, B+, B, C+, C, D, E 
(ii) Colour of mangoes: yellow, green, orange, red
(iii) Height data of a class: [178.9, 179, 179.5, 176, 177.2, 178.3, 175.8,...]
(iv) Number of mangoes exported by a farm: [500, 600, 478, 672, ...]'''
# (i) qualitative
# (ii) Qualitative
# (iii) Quantative
# (iv) Quantative

'''Q5. Explain the concept of levels of measurement and give an example of a variable for each level.'''
# 1. Nominal Level 
# Concept :-> Data are categorized into mutually exclusive, labeled goup with no inherent order and numerical value,.
# Example Variable : Blood type (A,B,AB or O)

# 2. Ordinal Level 
# Concept :-> Data are placed into categories that can be ranked or ordered in a meaningful sequence. 
# However, the exact mathematical distance or interval between the ranks is unknown or uneven.
# Example Variable : Socioeconomic status (low, middle,high class)

# 3. Interval Level
# Concept :-> Data  are ordered with meaningful,eaul and constant distances (interals) between values. Crucially, it lacks a true or absolute zero point - meaning zero does not represent the total absence of the property.
# Example Variable : Temperature measured in Celsius or Fahrenheit.

# Ratio level 
# Concept: The highest levvel of measurement, which contains all the properties of an interval scale plus an absolute true zero point. A value o f zero means the complete absence of vaiable, making multiplication and division meaningful.
# Example variable : Weight (in kg), (distance in meter ) 


'''Q6. Why is it important to understand the level of measurement when analyzing data? Provide an
example to illustrate your answer.'''
# Ans => 
'''Understanding the level of measurement is important because it dictates which mathematical operations and statistical tests you can 
validly use on your data.Why Level of Measurement Matters.

Defines valid math:--- It stops you from performing meaningless calculations, like adding or averaging categories.
Guides statistical choice:--- It tells you whether to use a mean (average), median (middle value), or mode (most common value).
Ensures accurate conclusions:--- Using the wrong method for your data type leads to false results.'''



'''Q7. How nominal data type is different from ordinal data type.'''
# Ans => Nominal and ordinal data are both categorical data types, but nominal data has no inherent order, while ordinal data follows a meaningful sequence or rank.

'''Q8. Which type of plot can be used to display data in terms of range?'''
# Ans => A box plot or a range bar chart is used to display data in terms of range.

'''Q9. Describe the difference between descriptive and inferential statistics. Give an example of each
type of statistics and explain how they are used.'''
# Descriptive statistics summarize and describe the features of a specific dataset, whereas inferential statistics use a smaller sample to make predictions, generalizations, or test hypotheses about a larger population
'''

## 1. Descriptive Statistics

* **Goal:** Organize, present, and summarize data from a measured group without drawing conclusions about a wider group.
* **Common Tools:** 
  * Measures of central tendency (mean, median, mode)
  * Measures of dispersion (range, standard deviation, variance)
  * Charts and graphs (histograms, pie charts)
* **Example & Usage:** A teacher calculates the average (mean) test score and standard deviation for the 30 students in their specific classroom. This is used to understand past performance and see how clustered or spread out the scores are for that exact group of students.

---

## 2. Inferential Statistics

* **Goal:** Draw logical conclusions, test hypotheses, and generalize findings from sample data to a broader population.
* **Common Tools:** 
  * Hypothesis testing (t-tests, ANOVA)
  * Confidence intervals
  * Regression analysis
* **Example & Usage:** A medical researcher tests a new blood pressure medication on a random sample of 200 patients and uses a t-test to see if the reduction is statistically significant. This is used to infer whether the drug will likely lower blood pressure safely for the entire global patient population, factoring in a margin of error.
'''


'''Q10. What are some common measures of central tendency and variability used in statistics? Explain
how each measure can be used to describe a dataset.'''

''' The most common measures of central tendency are the mean, median, and mode, while the most common measures of variability are 
the range, variance, and standard deviation. Together, these statistical tools summarize where the center of your data lies and how 
spread out the individual data points are.Measures of Central TendencyMeasures of central tendency find the "center" or a representative 
value of a dataset.

Mean (Average):- Sum of all values divided by the total number of values. It describes the "balance point" of the data. It is best used for symmetrical data without extreme outliers (e.g., average test scores).
Median:- The middle value when the data is ordered from smallest to largest. It splits the dataset exactly in half. It is highly resistant to outliers, making it ideal for skewed data (e.g., median household income).
Mode:- The value that occurs most frequently in a dataset. It highlights the most popular or common characteristic. It is particularly useful for categorical data where numerical math isn't possible (e.g., the most preferred car color).

Measures of Variability (Dispersion)Measures of variability describe how spread out, scattered, or clustered the data points are around the center.

Range:- The difference between the highest and lowest values (\(Maximum - Minimum\)). It gives a quick, simple snapshot of the total span of the data, though it is highly sensitive to extreme outliers.

Variance:- The average of the squared differences from the mean. It measures how far each number in the set is from the mean and from every other number. Because the numbers are squared, it is used more as a stepping stone for other calculations rather than direct interpretation.

Standard Deviation:- The square root of the variance. It expresses the spread in the exact same units as the original data. A low standard deviation means the data points are tightly clustered around the mean; a high standard deviation means the data is widely spread out.'''