# Feature Scaling and PCA – Assignment

## Q1. What is Min-Max Scaling, and how is it used in data preprocessing? Provide an example.

Min-Max Scaling is a feature scaling technique that transforms numerical values into a fixed range, usually 0 to 1.

The formula is:

Scaled Value = (X - X_min) / (X_max - X_min)

It is useful when features have different ranges and we want them to have a comparable scale.

### Example

Suppose the values of a feature are:

[10, 20, 30, 40, 50]

For X = 30:

Scaled Value = (30 - 10) / (50 - 10)
             = 20 / 40
             = 0.5

So, 30 becomes 0.5 after Min-Max scaling.

### Python Example

```python
from sklearn.preprocessing import MinMaxScaler

data = [[10], [20], [30], [40], [50]]

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

print(scaled_data)
```

Output:

```text
[[0.  ]
 [0.25]
 [0.5 ]
 [0.75]
 [1.  ]]
```


## Q2. What is the Unit Vector technique in feature scaling, and how does it differ from Min-Max Scaling?

The Unit Vector technique, also called Normalization by Vector Norm, scales the values of a data point so that the length (magnitude) of the vector becomes 1.

The formula is:

Normalized Value = X / ||X||

where ||X|| is the Euclidean norm:

||X|| = sqrt(x1^2 + x2^2 + ... + xn^2)

### Example

Suppose a data point is:

[3, 4]

Its magnitude is:

sqrt(3^2 + 4^2)
= sqrt(9 + 16)
= 5

After Unit Vector scaling:

[3/5, 4/5]

= [0.6, 0.8]

The magnitude of [0.6, 0.8] is 1.

### Difference between Min-Max Scaling and Unit Vector Scaling

| Min-Max Scaling | Unit Vector Scaling |
|---|---|
| Scales each feature independently | Scales an entire data point/vector |
| Usually transforms values to 0–1 | Makes the vector's magnitude equal to 1 |
| Uses minimum and maximum values | Uses vector norm |
| Sensitive to extreme minimum/maximum values | Focuses on the direction of the vector |

### Python Example

```python
from sklearn.preprocessing import Normalizer

data = [[3, 4]]

normalizer = Normalizer()
normalized_data = normalizer.fit_transform(data)

print(normalized_data)
```

Output:

```text
[[0.6 0.8]]
```


## Q3. What is PCA (Principal Component Analysis), and how is it used in dimensionality reduction?

PCA stands for Principal Component Analysis.

It is a dimensionality reduction technique that transforms the original features into a smaller number of new features called Principal Components.

The principal components are combinations of the original features.

PCA tries to preserve as much variation (information) in the data as possible.

### How PCA works

1. Standardize the data.
2. Calculate relationships between features using the covariance structure.
3. Find directions with the highest variance.
4. Rank the principal components according to the amount of variance they explain.
5. Select the required number of components.
6. Transform the original data into the selected components.

### Example

Suppose a dataset has 10 features:

```text
Feature1, Feature2, Feature3, ..., Feature10
```

If PCA shows that the first 3 principal components explain 90% of the variance, we can reduce the dataset from:

10 features -> 3 principal components

This makes the dataset smaller while retaining most of its important information.

### Python Example

```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X = [[1, 2, 3],
     [2, 4, 6],
     [3, 6, 9],
     [4, 8, 12]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(X_pca)
print(pca.explained_variance_ratio_)
```


## Q4. What is the relationship between PCA and Feature Extraction, and how can PCA be used for Feature Extraction?

Feature Extraction means creating new features from the existing features while trying to preserve useful information.

PCA is one method of Feature Extraction.

Instead of selecting some original features, PCA creates new features called Principal Components.

For example, suppose we have:

```text
Height
Weight
Age
Blood Pressure
```

PCA may create:

```text
PC1
PC2
```

where PC1 and PC2 are combinations of the original features.

For example, conceptually:

```text
PC1 = 0.5*Height + 0.6*Weight + 0.1*Age + 0.4*BloodPressure
```

The exact coefficients are calculated by PCA from the dataset.

Therefore:

Original features -> PCA -> New extracted features (Principal Components)

### Feature Selection vs Feature Extraction

Feature Selection chooses existing features.

Example:

```text
Height, Weight, Age, Blood Pressure
              ↓
       Select Weight + Age
```

Feature Extraction creates new features.

Example:

```text
Height, Weight, Age, Blood Pressure
              ↓
             PCA
              ↓
           PC1, PC2
```

So, PCA is a Feature Extraction technique, not simply a Feature Selection technique.


## Q5. Recommendation System for a Food Delivery Service – Min-Max Scaling

Suppose the dataset contains:

```text
Price
Rating
Delivery_Time
```

Example:

| Price | Rating | Delivery Time |
|---:|---:|---:|
| 100 | 4.0 | 30 |
| 250 | 4.5 | 45 |
| 500 | 5.0 | 60 |

These features have very different ranges.

For example:

- Price ranges from around 100 to 500.
- Rating ranges from 1 to 5.
- Delivery time may range from 10 to 60 minutes.

If these values are directly used by a model, the larger numerical scale of price may influence some distance-based algorithms more strongly.

Therefore, we can use Min-Max Scaling to transform every numerical feature into the same range, such as 0 to 1.

Formula:

Scaled Value = (X - X_min) / (X_max - X_min)

### Python Example

```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({
    "price": [100, 250, 500],
    "rating": [4.0, 4.5, 5.0],
    "delivery_time": [30, 45, 60]
})

scaler = MinMaxScaler()

df[["price", "rating", "delivery_time"]] = scaler.fit_transform(
    df[["price", "rating", "delivery_time"]]
)

print(df)
```

After scaling, each feature will have values between 0 and 1.

This makes the numerical features comparable in scale and can be particularly useful for distance-based recommendation methods.


## Q6. Predicting Stock Prices – Using PCA for Dimensionality Reduction

Suppose a stock-price prediction dataset contains many features such as:

```text
Revenue
Profit
Debt
Assets
P/E Ratio
Market Capitalization
Trading Volume
Interest Rate
Inflation
Market Index
Moving Average
Volatility
...
```

Having a large number of features can increase computational cost and may introduce redundant information because some features can be highly correlated.

### Steps to use PCA

1. Separate the target variable (stock price) from the input features.
2. Clean missing values and prepare categorical variables if present.
3. Standardize the numerical features because PCA is affected by feature scale.
4. Apply PCA to the standardized features.
5. Examine the explained variance ratio.
6. Select enough principal components to retain most of the useful variation.
7. Use the selected principal components as input features for the prediction model.

### Example

Suppose there are:

```text
50 original features
```

After PCA, we find that:

```text
10 principal components explain 95% of the variance.
```

We can reduce:

```text
50 features -> 10 principal components
```

The model can then be trained using those 10 components.

### Important Point

PCA should generally be fitted only on the training data and then used to transform the validation/test data. This prevents information from the test set from leaking into the training process.


## Q7. Perform Min-Max Scaling on [1, 5, 10, 15, 20] to a range of -1 to 1.

We use the general Min-Max Scaling formula:

X_scaled = a + ((X - X_min) * (b - a)) / (X_max - X_min)

where:

a = -1
b = 1
X_min = 1
X_max = 20

Therefore:

X_scaled = -1 + ((X - 1) * 2) / 19

### Calculations

For X = 1:

```text
-1 + ((1 - 1) * 2) / 19
= -1
```

For X = 5:

```text
-1 + ((5 - 1) * 2) / 19
= -0.5789
```

For X = 10:

```text
-1 + ((10 - 1) * 2) / 19
= -0.0526
```

For X = 15:

```text
-1 + ((15 - 1) * 2) / 19
= 0.4737
```

For X = 20:

```text
-1 + ((20 - 1) * 2) / 19
= 1
```

### Final Answer

```text
Original: [1, 5, 10, 15, 20]

Scaled:   [-1, -0.5789, -0.0526, 0.4737, 1]
```

### Python Example

```python
from sklearn.preprocessing import MinMaxScaler

data = [[1], [5], [10], [15], [20]]

scaler = MinMaxScaler(feature_range=(-1, 1))

scaled_data = scaler.fit_transform(data)

print(scaled_data)
```


## Q8. Dataset [height, weight, age, gender, blood pressure] – Feature Extraction using PCA

The dataset contains:

```text
Height
Weight
Age
Gender
Blood Pressure
```

PCA can be used to extract a smaller number of new features called Principal Components.

### Important Point About Gender

Gender is categorical, so it cannot be directly given to PCA as text such as:

```text
Male
Female
```

It must first be encoded numerically, although the encoding approach should be chosen carefully because simple 0/1 encoding can impose a numerical relationship that may not be meaningful.

### How I would apply PCA

1. Clean the dataset.
2. Handle missing values.
3. Encode categorical variables such as gender appropriately.
4. Standardize the numerical features.
5. Apply PCA.
6. Look at the explained variance ratio.
7. Select the number of components based on how much variance we want to retain.

### How many components should be retained?

We cannot decide the exact number of principal components only from the feature names.

There are 5 original features, so PCA can produce at most 5 components.

The correct number should be selected after checking the explained variance.

For example, if the PCA results are:

```text
PC1 = 45% variance
PC2 = 25% variance
PC3 = 15% variance
PC4 = 10% variance
PC5 = 5% variance
```

Then:

```text
PC1 + PC2 + PC3 = 85%
```

We might retain 3 components if retaining around 85% of the variance is acceptable.

If we want to retain at least 90%, we may need 4 components:

```text
PC1 + PC2 + PC3 + PC4 = 95%
```

Therefore, for this dataset, I would initially try to retain enough components to explain approximately 90–95% of the variance rather than choosing an arbitrary number.

### Example

```text
Original features:
Height, Weight, Age, Gender, Blood Pressure
                    ↓
              Standardization
                    ↓
                   PCA
                    ↓
        PC1, PC2, PC3 (example)
```

This converts the original features into a smaller set of extracted features while retaining most of the information represented by the selected variance.


# Summary

- Min-Max Scaling changes feature values to a specified range such as 0–1.
- Unit Vector scaling makes the magnitude of each data vector equal to 1.
- PCA is a dimensionality reduction technique.
- PCA creates new features called Principal Components.
- PCA is therefore a Feature Extraction technique.
- Before PCA, numerical features should generally be standardized.
- The number of PCA components should be selected using explained variance rather than simply choosing an arbitrary number.
