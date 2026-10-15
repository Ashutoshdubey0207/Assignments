# Model 66 Assignment 2

## Q1. What is the purpose of GridSearchCV in machine learning, and how does it work?

**GridSearchCV** is a technique used to find the best hyperparameters for a machine learning model. It tests different combinations of hyperparameters and selects the combination that performs best according to a chosen evaluation metric.

**How it works:**
1. Define the model and the hyperparameters to test.
2. Create a grid of possible hyperparameter values.
3. Use cross-validation to evaluate each combination on different subsets of the training data.
4. Calculate the average performance for each combination.
5. Select the combination with the best average score.
6. With `refit=True` (the default), train the selected model on the full training dataset.

**Example:**

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)

param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [5, 10]
}

grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy"
)

grid_search.fit(X_train, y_train)

print(grid_search.best_params_)
print(grid_search.best_score_)
```

This tests four hyperparameter combinations using five-fold cross-validation.

## Q2. Describe the difference between GridSearchCV and RandomizedSearchCV, and when might you choose one over the other.

Both techniques tune hyperparameters, but they explore the search space differently.

| Feature | GridSearchCV | RandomizedSearchCV |
|---|---|---|
| Search method | Tests every specified combination | Samples a fixed number of combinations |
| Computational cost | Can be high for large grids | Often lower for large search spaces |
| Coverage | Exhaustive over the specified grid | Depends on the number of samples |
| Best suited for | Small search spaces | Large search spaces |
| Main advantage | Systematic search of all specified combinations | Efficient exploration of many possible values |

**Example:**

```python
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_grid,
    n_iter=3,
    cv=5,
    scoring="accuracy",
    random_state=42
)

random_search.fit(X_train, y_train)

print(random_search.best_params_)
print(random_search.best_score_)
```

Here, `n_iter=3` means three parameter combinations are sampled and evaluated, with five-fold cross-validation for each.

**When to choose:**
- Choose **GridSearchCV** when the search space is small and you want to test every specified combination.
- Choose **RandomizedSearchCV** when the search space is large and you want to explore it with less computational effort.

## Q3. What is data leakage, and why is it a problem in machine learning? Provide an example.

**Data leakage** occurs when information that would not legitimately be available at prediction time influences model training or evaluation.

It is a problem because it can make a model appear more accurate during testing than it will be in real-world use.

**Example:** Suppose we are building a model to predict diabetes. Before splitting the dataset into training and testing sets, we calculate the average glucose level using the entire dataset and use it to fill missing values. The test data has influenced preprocessing, which can leak information into model development.

Another example is using a patient's future medical information to predict whether the patient has a disease today.

**Why it is a problem:**
- It produces overly optimistic evaluation results.
- It makes model performance estimates less reliable.
- It can lead to poor predictions in real-world situations.

## Q4. How can you prevent data leakage when building a machine learning model?

Data leakage can be reduced by following these practices:

1. **Split the data first:** Separate training and testing data before fitting preprocessing steps.
2. **Fit preprocessing only on training data:** Learn imputation values, scaling parameters, and feature-selection rules from training data only.
3. **Use pipelines:** Put preprocessing and model training in a pipeline so cross-validation fits preprocessing separately within each training fold.
4. **Avoid future information:** Use only features that would be available at prediction time.
5. **Use suitable splitting methods:** For time-series data, split chronologically. For related records, use group-based splitting where appropriate.
6. **Keep the test set separate:** Do not use it to select features, tune hyperparameters, or repeatedly improve the model.

**Example using a Scikit-learn pipeline:**

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = make_pipeline(
    SimpleImputer(strategy="mean"),
    StandardScaler(),
    LogisticRegression()
)

pipeline.fit(X_train, y_train)

print("Test accuracy:", pipeline.score(X_test, y_test))
```

The imputer and scaler learn their parameters from the training data only.

## Q5. What is a confusion matrix, and what does it tell you about the performance of a classification model?

A **confusion matrix** is a table that compares actual class labels with predicted class labels.

For binary classification, it contains four values:

| Actual / Predicted | Predicted Positive | Predicted Negative |
|---|---:|---:|
| Actual Positive | True Positive (TP) | False Negative (FN) |
| Actual Negative | False Positive (FP) | True Negative (TN) |

- **True Positive (TP):** The model correctly predicts the positive class.
- **True Negative (TN):** The model correctly predicts the negative class.
- **False Positive (FP):** The model predicts positive when the actual class is negative.
- **False Negative (FN):** The model predicts negative when the actual class is positive.

The confusion matrix shows how many predictions are correct and what kinds of mistakes the model makes.

## Q6. Explain the difference between precision and recall in the context of a confusion matrix.

**Precision** measures how many observations predicted as positive are actually positive.

\[
\text{Precision} = \frac{TP}{TP + FP}
\]

High precision means the model makes relatively few false-positive predictions.

**Recall** measures how many actual positive observations the model correctly identifies.

\[
\text{Recall} = \frac{TP}{TP + FN}
\]

High recall means the model misses relatively few positive cases.

| Metric | Main question | Error it helps monitor |
|---|---|---|
| Precision | How many predicted positives are correct? | False positives |
| Recall | How many actual positives were found? | False negatives |

For disease screening, high recall may be especially important because missing a disease can be costly. For spam filtering, high precision can help avoid sending legitimate emails to spam.

## Q7. How can you interpret a confusion matrix to determine which types of errors your model is making?

Interpret the matrix by examining the true-positive, true-negative, false-positive, and false-negative values.

1. **True Positives (TP):** Correctly identified positive cases.
2. **True Negatives (TN):** Correctly identified negative cases.
3. **False Positives (FP):** Negative cases incorrectly predicted as positive.
4. **False Negatives (FN):** Positive cases incorrectly predicted as negative.

**Example:**

Suppose a disease-prediction model produces the following results:

| Actual / Predicted | Disease | No disease |
|---|---:|---:|
| Disease | 80 (TP) | 20 (FN) |
| No disease | 10 (FP) | 90 (TN) |

Interpretation:
- The model correctly identifies 80 patients with the disease.
- It misses 20 patients who actually have the disease.
- It incorrectly predicts disease for 10 healthy patients.
- It correctly identifies 90 patients without the disease.

This model has more false negatives than false positives. If missing a disease is especially harmful, improving recall may be a priority.

## Q8. What are some common metrics that can be derived from a confusion matrix, and how are they calculated?

| Metric | Formula | Meaning |
|---|---|---|
| Accuracy | \(\frac{TP + TN}{TP + TN + FP + FN}\) | Proportion of all predictions that are correct |
| Precision | \(\frac{TP}{TP + FP}\) | Proportion of predicted positives that are correct |
| Recall (Sensitivity) | \(\frac{TP}{TP + FN}\) | Proportion of actual positives correctly identified |
| Specificity | \(\frac{TN}{TN + FP}\) | Proportion of actual negatives correctly identified |
| F1-score | \(2 \times \frac{Precision \times Recall}{Precision + Recall}\) | Harmonic mean of precision and recall |

**Example:** Suppose TP = 80, TN = 90, FP = 10, and FN = 20.

- **Accuracy:** \((80 + 90) / 200 = 85\%\)
- **Precision:** \(80 / (80 + 10) = 88.89\%\)
- **Recall:** \(80 / (80 + 20) = 80\%\)
- **Specificity:** \(90 / (90 + 10) = 90\%\)
- **F1-score:** \(2 \times (0.8889 \times 0.80) / (0.8889 + 0.80) \approx 84.21\%\)

These metrics provide different perspectives on performance. Accuracy alone may be misleading when classes are imbalanced.

## Q9. What is the relationship between the accuracy of a model and the values in its confusion matrix?

Accuracy is calculated directly from the confusion matrix. It measures the proportion of all predictions that are correct.

\[
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
\]

The numerator contains correct predictions (TP and TN), while the denominator contains all predictions.

**Example:** If TP = 80, TN = 90, FP = 10, and FN = 20:

\[
\text{Accuracy} = \frac{80 + 90}{200} = 85\%
\]

The model correctly classifies 85% of the observations.

**Limitation:** High accuracy does not always mean a model performs well. If 95% of observations belong to the negative class, a model that always predicts negative can achieve 95% accuracy while failing to identify any positive cases. Precision, recall, and the confusion matrix help reveal this limitation.

## Q10. How can you use a confusion matrix to identify potential biases or limitations in your machine learning model?

A confusion matrix helps identify performance problems by showing which classes are predicted correctly and which are frequently misclassified.

1. **Class imbalance:** A model may favor the majority class. Compare correct and incorrect predictions for each class.
2. **Unequal error rates:** High false-positive or false-negative rates can show that the model struggles with certain predictions.
3. **Minority-class performance:** Examine per-class precision and recall to see whether less common classes are poorly identified.
4. **Multiclass confusion:** In multiclass classification, identify which pairs of classes are frequently confused.
5. **Group-level disparities:** Where appropriate, calculate separate confusion matrices for relevant demographic or operational groups to check whether error rates differ.
6. **Model limitations:** High error rates may suggest a need for more representative data, better features, improved preprocessing, or a different decision threshold.

**Example:** A loan-approval model may perform well for most applicants but frequently misclassify applicants from a smaller group. This could indicate that the training data is not representative or that error rates differ between groups. Further analysis is needed to identify the cause.

**Conclusion:** A confusion matrix helps evaluate classification errors, compare class-level performance, and identify potential fairness concerns. However, it cannot prove bias on its own; additional analysis of the data, relevant groups, and real-world context is necessary.
