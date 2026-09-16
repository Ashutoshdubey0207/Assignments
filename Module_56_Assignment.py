from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd
import numpy as np

'''
# Assignment: Categorical Encoding and Covariance

## Q1. What is the difference between Ordinal Encoding and Label Encoding? Provide an example of when you might choose one over the other.

### Answer:

**Ordinal Encoding** and **Label Encoding** are techniques used to convert categorical data into numerical values so that machine learning algorithms can process them.

### 1. Ordinal Encoding

Ordinal Encoding is used when the categories have a **meaningful order or ranking**.

For example, consider the variable **Education Level**:

| Education Level | Encoded Value |
| --------------- | ------------: |
| High School     |             0 |
| Bachelor's      |             1 |
| Master's        |             2 |
| PhD             |             3 |

Here, the numbers represent the actual order of education levels:

**High School < Bachelor's < Master's < PhD**

In Scikit-learn, we can specify the order explicitly:

```python
from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder(
    categories=[["High School", "Bachelor's", "Master's", "PhD"]]
)

encoded = encoder.fit_transform(
    df[["Education Level"]]
)
```

### When should we use Ordinal Encoding?

We should use Ordinal Encoding when the categories have a **natural ranking**.

**Example:**

* Education Level → High School < Bachelor's < Master's < PhD
* Satisfaction → Poor < Average < Good < Excellent
* Size → Small < Medium < Large

---

### 2. Label Encoding

Label Encoding assigns a numerical value to each category.

For example:

| Gender | Encoded Value |
| ------ | ------------: |
| Female |             0 |
| Male   |             1 |

Here, `0` and `1` are simply numerical labels. They do **not** mean that Male is greater than Female.

Label Encoding is commonly used for a **target variable** containing categorical classes.

For example:

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(
    ["Cat", "Dog", "Dog", "Cat", "Bird"]
)

print(y_encoded)
```

The categories may be encoded as:

```text
Bird → 0
Cat  → 1
Dog  → 2
```

The numbers are labels for the classes rather than meaningful rankings.

### Difference between Ordinal Encoding and Label Encoding

| Feature                   | Ordinal Encoding          | Label Encoding                  |
| ------------------------- | ------------------------- | ------------------------------- |
| Main purpose              | Encode ordered categories | Encode categorical class labels |
| Categories need an order? | **Yes**                   | **No**                          |
| Example                   | Education Level           | Target: Cat/Dog/Bird            |
| Meaning of numbers        | Represents order          | Represents class labels         |
| Common use                | Input features            | Target variable                 |

### Example of choosing between them

Suppose a dataset contains:

```text
Education Level: High School, Bachelor's, Master's, PhD
Gender: Male, Female
```

For **Education Level**, I would use **Ordinal Encoding** because there is a natural order.

For a **Gender** feature, I would generally use **One-Hot Encoding** rather than Label Encoding because Gender is nominal and has no natural order.

If the target variable is:

```text
Purchased: Yes / No
```

Label Encoding can be used to convert it into numerical class labels.

---

## Q2. Explain how Target Guided Ordinal Encoding works and provide an example of when you might use it in a machine learning project.

### Answer:

**Target Guided Ordinal Encoding** is an encoding technique in which categorical values are converted into numerical values according to their relationship with the **target variable**.

Instead of assigning numbers arbitrarily, we calculate a target-related statistic, such as the **mean target value**, for each category. The categories are then ordered according to this statistic and assigned ordinal values.

### Example

Suppose we want to predict whether a customer will purchase a product.

Our dataset contains:

| Education   | Purchased |
| ----------- | --------: |
| High School |         0 |
| Bachelor's  |         1 |
| Master's    |         1 |
| PhD         |         1 |
| High School |         0 |
| Bachelor's  |         0 |
| Master's    |         1 |
| PhD         |         1 |

First, calculate the average target value for each category.

| Education   | Average Purchased |
| ----------- | ----------------: |
| High School |              0.00 |
| Bachelor's  |              0.50 |
| Master's    |              1.00 |
| PhD         |              1.00 |

Now, we can order the categories according to their target mean:

```text
High School → Bachelor's → Master's/PhD
```

We can then assign ordinal values:

| Education   | Target Mean | Encoded Value |
| ----------- | ----------: | ------------: |
| High School |        0.00 |             0 |
| Bachelor's  |        0.50 |             1 |
| Master's    |        1.00 |             2 |
| PhD         |        1.00 |             3 |

The exact handling of tied categories can vary depending on the encoding strategy.

### When can Target Guided Ordinal Encoding be useful?

It can be useful when a categorical feature has **many categories** and we want to represent the categories using information related to the target.

For example, suppose an e-commerce dataset has:

```text
City
----
Mumbai
Delhi
Pune
Bengaluru
Jaipur
Indore
...
```

If the target is `Customer_Spending`, we can calculate the average spending for each city and use that information to create a target-guided encoding.

This can reduce the number of columns compared with One-Hot Encoding.

### Important: Avoid Data Leakage

Target Guided Encoding must be performed carefully because it uses information from the target variable.

We should **not calculate category statistics using the validation or test data**.

For example, if we are splitting the dataset into training and testing data:

```text
Training Data → calculate target means
Testing Data  → apply the already calculated mappings
```

The target values from the test set must not be used to calculate the encoding.

Otherwise, information from the test data can leak into the model during training, resulting in an overly optimistic evaluation.

---

## Q3. Define covariance and explain why it is important in statistical analysis. How is covariance calculated?

### Answer:

**Covariance** is a statistical measure that describes the **direction in which two variables change together**.

It tells us whether an increase in one variable tends to be associated with an increase or decrease in another variable.

There are three basic possibilities:

### 1. Positive Covariance

If two variables tend to increase together, their covariance is **positive**.

**Example:**

```text
Study Hours ↑ → Exam Marks ↑
```

Students who study more hours tend to obtain higher marks.

Therefore, study hours and exam marks can have positive covariance.

---

### 2. Negative Covariance

If one variable tends to increase while the other decreases, their covariance is **negative**.

**Example:**

```text
Product Price ↑ → Quantity Sold ↓
```

As the price of a product increases, the quantity demanded may decrease.

Therefore, price and quantity sold can have negative covariance.

---

### 3. Covariance Close to Zero

If there is little or no **linear relationship** between two variables, their covariance may be close to zero.

For example:

```text
Shoe Size ↔ Exam Marks
```

There may be no meaningful linear relationship between these variables.

---

### Covariance Formula

For a sample of data, covariance between variables \(X\) and \(Y\) is calculated as:

$$
Cov(X,Y) =
\frac{\sum_{i=1}^{n}(X_i-\bar X)(Y_i-\bar Y)}
{n-1}
$$

Where:

* \(X_i\) = individual value of X
* \(Y_i\) = individual value of Y
* \(\bar X\) = mean of X
* \(\bar Y\) = mean of Y
* \(n\) = number of observations

### Simple Example

Suppose we have:

| Study Hours (X) | Exam Marks (Y) |
| --------------: | -------------: |
|               2 |             40 |
|               4 |             50 |
|               6 |             60 |
|               8 |             70 |

As study hours increase, exam marks also increase.

Therefore, the covariance will be **positive**.

In Python, covariance can be calculated using Pandas:

```python
df[["Study Hours", "Exam Marks"]].cov()
```

This produces a **covariance matrix**:

```text
             Study Hours    Exam Marks
Study Hours       Var(X)       Cov(X,Y)
Exam Marks        Cov(X,Y)     Var(Y)
```

The diagonal values are the **variances** of the individual variables, while the off-diagonal values are their **covariances**.

### Why is covariance important?

Covariance is useful because it helps us:

1. Understand how two variables change together.
2. Identify the direction of their linear relationship.
3. Explore relationships between features during data analysis.
4. Understand relationships before building machine learning models.
5. Form the basis for techniques such as **Principal Component Analysis (PCA)** and covariance matrices.

### Important limitation

The magnitude of covariance depends on the **units and scale** of the variables. Therefore, covariance values from different pairs of variables are not always directly comparable.

For measuring the **strength and direction** of a linear relationship on a standardized scale, **correlation** is often more useful.

### Conclusion

Covariance tells us the **direction of the joint movement of two variables**. A positive covariance indicates that the variables tend to increase together, a negative covariance indicates that one tends to increase while the other decreases, and a covariance near zero indicates little linear co-movement.










Q4. For a dataset with the following categorical variables: Color (red, green, blue), Size (small, medium,
large), and Material (wood, metal, plastic), perform label encoding using Python's scikit-learn library.
Show your code and explain the output.'''

df = pd.DataFrame({
    'colors': ['red','green','blue','blue','green']
})

color_encoder = LabelEncoder()
encoded_colors = color_encoder.fit_transform(df['colors'])
encoded_df = pd.DataFrame({
    'colors_encoded': encoded_colors
})
final_df = pd.concat((df,encoded_df),axis=1)
# print(final_df)

size_encoder = LabelEncoder()

size_df = pd.DataFrame({
    'size':['small','medium','large','medium','small','large']
})

encoded_size = size_encoder.fit_transform(size_df['size'])

encoded_df_size = pd.DataFrame({
    'encoded_size': encoded_size
})
final_size_df = pd.concat((size_df,encoded_df_size),axis=1,)
#print(final_size_df)

# Material (wood, metal, plastic)

encoder = LabelEncoder()

material_df = pd.DataFrame({
    'Material' : ['wood','metal','plastic']
})

encoded_material = encoder.fit_transform(material_df['Material'])

encoded_material_df = pd.DataFrame({
    'encoded_material': encoded_material
})
final_material_df = pd.concat((material_df,encoded_material_df),axis=1)
#print(final_material_df)

# Label encoder basically encode based on the alphabatical order of the data for example
# 'colors': ['red','green','blue','blue','green']
# blue = 0 green = 1 red = 2

'''Q5. Calculate the covariance matrix for the following variables in a dataset: Age, Income, and Education
level. Interpret the results.'''


df = pd.DataFrame({
    "Age": [22, 25, 28, 30, 35, 40, 45, 29, 33, 38, 50, 27, 31, 42, 55],
    "Income": [25000, 32000, 45000, 52000, 68000, 75000, 90000, 48000,
               60000, 72000, 95000, 40000, 55000, 82000, 110000],
    "Education_level": [
        "High School", "Bachelor", "Bachelor", "Master", "Master",
        "Master", "PhD", "Bachelor", "Bachelor", "Master",
        "PhD", "High School", "Bachelor", "Master", "PhD"
    ]
})

encoder = OrdinalEncoder(categories=[["High School", "Bachelor","Master","PhD"]])
encoded_df = encoder.fit_transform(df[['Education_level']])
df['Encoded_Edu_df'] = encoded_df
# print("covariance of income and age")
# print(df[['Income','Age']].cov(numeric_only=True))



'''
Q6. You are working on a machine learning project with a dataset containing several categorical
variables, including "Gender" (Male/Female), "Education Level" (High School/Bachelor's/Master's/PhD),
and "Employment Status" (Unemployed/Part-Time/Full-Time). Which encoding method would you use for
each variable, and why?
Ans =>
I would use One-Hot Encoding for Gender because it is nominal, Ordinal Encoding for Education Level because it 
has a natural order, and One-Hot Encoding for Employment Status because its categories should not be assumed to 
have a numerical order.

Q7. You are analyzing a dataset with two continuous variables, "Temperature" and "Humidity", and two
categorical variables, "Weather Condition" (Sunny/Cloudy/Rainy) and "Wind Direction" (North/South/
East/West). Calculate the covariance between each pair of variables and interpret the results.

'''
data = {
    "Temperature": [
        31.2, 28.5, 26.8, 24.3, 22.7,
        30.1, 32.5, 27.9, 25.4, 23.8,
        29.6, 33.1, 21.9, 26.5, 30.8,
        28.2, 24.9, 22.4, 31.7, 27.3
    ],

    "Humidity": [
        58, 72, 81, 88, 91,
        65, 52, 76, 85, 93,
        68, 49, 95, 79, 61,
        74, 89, 92, 55, 83
    ],

    "Weather Condition": [
        "Sunny", "Cloudy", "Rainy", "Rainy", "Rainy",
        "Sunny", "Sunny", "Cloudy", "Rainy", "Rainy",
        "Cloudy", "Sunny", "Rainy", "Cloudy", "Sunny",
        "Cloudy", "Rainy", "Rainy", "Sunny", "Cloudy"
    ],

    "Wind Direction": [
        "North", "East", "South", "West", "South",
        "East", "North", "West", "South", "West",
        "East", "North", "West", "South", "East",
        "North", "West", "South", "East", "North"
    ]
}

df = pd.DataFrame(data)
encoder = OneHotEncoder(sparse_output=False) # to get the output in therms of array

encoded_df = encoder.fit_transform(df[['Weather Condition',"Wind Direction"]])
data_df = pd.DataFrame(
    encoded_df,columns=encoder.get_feature_names_out(['Weather Condition',"Wind Direction"])
)
final_data = pd.concat((df,data_df),axis=1)
print(final_data)