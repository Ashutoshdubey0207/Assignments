# Module 72 Assignment 2: K-Nearest Neighbors (KNN)

## Q1. What is the KNN algorithm?

**K-Nearest Neighbors (KNN)** is a supervised machine learning algorithm used for both classification and regression. It predicts the output of a new data point by examining the `K` closest data points in the training dataset.

KNN is called a **lazy learning algorithm** because it does not build an explicit model during training. Instead, it stores the training data and performs calculations when making predictions.

### How KNN works
1. Choose the value of `K`.
2. Calculate the distance between the new data point and the training data points.
3. Select the `K` nearest neighbors.
4. For classification, predict the majority class.
5. For regression, calculate the average (or a weighted average) of the neighbors' target values.

**Example:** Suppose we want to classify a fruit as an apple or an orange. If `K = 5`, and among the five nearest fruits, three are apples and two are oranges, KNN classifies the new fruit as an apple.

---

## Q2. How do you choose the value of K in KNN?

The value of `K` determines how many neighboring data points influence a prediction.

- **Small K:** The model is sensitive to noise and may overfit.
- **Large K:** The model may become too generalized and underfit.
- **Optimal K:** Provides a good balance between bias and variance.

### Common methods to choose K
1. **Cross-validation:** Test different values of K and select the one with the best validation performance.
2. **Grid search:** Evaluate a range of K values systematically.
3. **Square-root rule:** Use `sqrt(n)` as a rough starting point, where `n` is the number of training samples.
4. **Odd K for binary classification:** An odd value can help avoid ties, although ties can still occur in multiclass problems.

**Example:** If the dataset contains 100 training samples, `sqrt(100) = 10`. We might test values such as `K = 3, 5, 7, 9, 11, 15` using cross-validation.

The square-root rule is only a starting point; cross-validation is generally more reliable.

---

## Q3. What is the difference between KNN classifier and KNN regressor?

| Feature | KNN Classifier | KNN Regressor |
|---|---|---|
| Purpose | Predicts categories | Predicts numerical values |
| Output | Discrete class label | Continuous number |
| Prediction method | Majority voting | Average of neighbors' target values |
| Example | Predicting spam or not spam | Predicting house prices |
| Evaluation metrics | Accuracy, precision, recall, F1-score | MAE, MSE, RMSE, R² |
| Scikit-learn class | `KNeighborsClassifier` | `KNeighborsRegressor` |

**Example of classification:** If the three nearest neighbors have labels `A, A, B`, the predicted class is `A`.

**Example of regression:** If the three nearest neighbors have house prices of ₹20 lakh, ₹25 lakh, and ₹30 lakh, the prediction is:

`(20 + 25 + 30) / 3 = 25`

Therefore, the predicted house price is ₹25 lakh.

---

## Q4. How do you measure the performance of KNN?

Performance evaluation depends on whether KNN is used for classification or regression.

### A. Classification metrics

- **Accuracy:** Proportion of total predictions that are correct.
- **Precision:** Proportion of positive predictions that are actually positive.
- **Recall:** Proportion of actual positive cases correctly identified.
- **F1-score:** Harmonic mean of precision and recall.
- **Confusion matrix:** Shows true positives, true negatives, false positives, and false negatives.
- **ROC-AUC:** Evaluates how well the model distinguishes between classes across different thresholds.

Accuracy formula:

`Accuracy = (TP + TN) / (TP + TN + FP + FN)`

### B. Regression metrics

- **MAE:** Mean Absolute Error; average absolute prediction error.
- **MSE:** Mean Squared Error; average squared prediction error.
- **RMSE:** Square root of MSE, expressed in the target variable's units.
- **R² score:** Measures how well the model explains variation in the target variable.

RMSE formula:

`RMSE = sqrt((1/n) * sum((y_i - y_pred_i)^2))`

A lower MAE, MSE, or RMSE generally indicates better predictive performance. An R² closer to 1 generally indicates a better fit, though it can also be negative.

**Important:** Use a separate test dataset for final evaluation and cross-validation for model selection.

---

## Q5. What is the curse of dimensionality in KNN?

The **curse of dimensionality** refers to the problems that arise when data has a large number of features.

In KNN, distance calculations become less informative as the number of dimensions increases. Data points become sparse, and the nearest and farthest points can have increasingly similar distances. As a result, identifying meaningful neighbors becomes difficult.

For example, predicting house prices using five relevant features may be easier than using 500 features, many of which are irrelevant.

### Problems caused by the curse of dimensionality
- Reduced prediction accuracy.
- Increased computational cost.
- Greater sensitivity to irrelevant features.
- Requirement for more training data.

### How to address it
1. Apply feature selection to remove irrelevant features.
2. Use dimensionality reduction techniques such as PCA.
3. Collect more representative training data where practical.
4. Use domain knowledge to select meaningful features.
5. Test distance metrics and model parameters through cross-validation.

---

## Q6. How do you handle missing values in KNN?

KNN relies on distance calculations, so missing values can make those calculations unreliable. They should generally be handled before fitting a standard KNN model.

### Common techniques
1. **Mean imputation:** Replace missing numerical values with the mean.
2. **Median imputation:** Replace missing numerical values with the median; this is often preferable for skewed data or data containing outliers.
3. **Mode imputation:** Replace missing categorical values with the most frequent category.
4. **KNN imputation:** Estimate missing values using similar observations.
5. **Row or column removal:** Remove rows or features with excessive missing values when appropriate.

Example using Scikit-learn:

```python
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=5))
])
```

Fit the pipeline on the training data and use it to predict on the test data. The imputer learns its replacement values from the training data only, helping prevent data leakage.

For mixed numerical and categorical features, use suitable imputers and encoders for each feature type.

---

## Q7. Compare and contrast the performance of KNN classifier and regressor. Which one is better for which type of problem?

Both algorithms use neighboring observations, but they solve different prediction problems.

| Comparison | KNN Classifier | KNN Regressor |
|---|---|---|
| Target variable | Categorical | Numerical |
| Prediction | Majority vote or weighted vote | Mean or weighted mean |
| Typical applications | Disease category prediction, spam detection | House prices, sales forecasting |
| Evaluation | Accuracy, F1-score, ROC-AUC | MAE, RMSE, R² |
| Main concern | Class imbalance and noisy labels | Outliers and noisy numerical targets |

### Which one is better?
- Use **KNN Classifier** when the target is a category, such as `Pass/Fail`, `Spam/Not Spam`, or `Setosa/Versicolor/Virginica`.
- Use **KNN Regressor** when the target is a numerical value, such as salary, temperature, or house price.

Neither is universally better. Their performance depends on the dataset, feature quality, choice of K, distance metric, and preprocessing. Compare them with appropriate validation metrics for the problem.

---

## Q8. What are the strengths and weaknesses of the KNN algorithm for classification and regression tasks, and how can these be addressed?

### Strengths
1. **Simple to understand:** Its logic is easy to explain and implement.
2. **No explicit training phase:** It stores observations instead of learning a complex model.
3. **Nonlinear decision boundaries:** It can model complex patterns without assuming a linear relationship.
4. **Works for classification and regression:** The same neighbor-search principle supports both tasks.
5. **Adaptable:** Different distance metrics and distance-weighted predictions can be used.

### Weaknesses and solutions

| Weakness | How to address it |
|---|---|
| Slow predictions on large datasets | Use efficient neighbor-search methods or approximate nearest-neighbor search |
| Sensitive to feature scales | Apply standardization or normalization |
| Curse of dimensionality | Use feature selection or PCA |
| Sensitive to noise and outliers | Tune K and consider distance-weighted predictions |
| Sensitive to irrelevant features | Remove unhelpful features |
| Requires memory to store training data | Reduce the dataset or use an alternative model when memory is limited |
| Can struggle with imbalanced classes | Use suitable resampling methods, class-aware strategies, and precision/recall metrics |
| Missing values can disrupt distances | Impute missing values before applying KNN |

KNN is often useful for small to medium-sized datasets with meaningful distance relationships. For very large or high-dimensional datasets, other algorithms may be more efficient or accurate.

---

## Q9. What is the difference between Euclidean distance and Manhattan distance in KNN?

Both are distance metrics used to measure the similarity between data points.

### 1. Euclidean distance

Measures the straight-line distance between two points.

**Formula:**

`d(x, y) = sqrt(sum((x_i - y_i)^2))`

Example: For points `A = (1, 2)` and `B = (4, 6)`:

`d = sqrt((4 - 1)^2 + (6 - 2)^2) = 5`

### 2. Manhattan distance

Measures the sum of the absolute differences between coordinates. It is also called city-block distance.

**Formula:**

`d(x, y) = sum(abs(x_i - y_i))`

For the same points:

`d = abs(4 - 1) + abs(6 - 2) = 7`

| Feature | Euclidean | Manhattan |
|---|---|---|
| Path | Straight line | Horizontal and vertical movements |
| Sensitivity | Squared differences make large coordinate differences influential | Uses absolute differences |
| Formula | Square root of squared differences | Sum of absolute differences |
| Common use | Continuous numerical data with meaningful straight-line geometry | Grid-like movement or problems where coordinate-wise differences are meaningful |

**Which is better?** Neither is always better. Test both using cross-validation. The most suitable metric depends on the data's geometry and feature representation.

---

## Q10. What is the role of feature scaling in KNN?

Feature scaling is important because KNN uses distances to identify neighboring data points. If features have very different scales, features with larger numerical values can dominate the distance calculation.

**Example:** Suppose a dataset contains:
- Age: 18–70
- Annual income: ₹100,000–₹2,000,000

Without scaling, income may dominate the distance calculation even if age is also important for prediction.

### Common feature-scaling methods

**1. Standardization**

Transforms features to have approximately zero mean and unit standard deviation.

`z = (x - mean) / standard_deviation`

**2. Min-max normalization**

Usually scales values to a range of 0 to 1.

`x_scaled = (x - x_min) / (x_max - x_min)`

### Example in Python

```python
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

model = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=5))
])

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

Here, the scaler learns the feature statistics from `X_train` and applies the same transformation to `X_test`.

### Benefits of feature scaling
- Prevents large-scale features from dominating distances.
- Makes distance calculations more meaningful.
- Can improve classification and regression performance.
- Helps KNN treat features more comparably, although scaling alone does not determine their importance.

**Conclusion:** Feature scaling is generally essential for KNN when numerical features use different units or ranges. Choose the scaling method based on the data and fit it only on the training set.

---

## Quick Revision

- **KNN:** Predicts using the nearest observations.
- **KNN Classifier:** Predicts a class using voting.
- **KNN Regressor:** Predicts a numerical value using an average or weighted average.
- **Choosing K:** Use cross-validation to find a suitable value.
- **Curse of dimensionality:** Many features can make distances less informative.
- **Missing values:** Impute them before standard KNN.
- **Euclidean distance:** Straight-line distance.
- **Manhattan distance:** Sum of absolute coordinate differences.
- **Feature scaling:** Keeps features with different units from unfairly dominating distance calculations.
- **Evaluation:** Classification uses metrics such as accuracy and F1-score; regression uses MAE, RMSE, and R².
