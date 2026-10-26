# Module 72 Assignment 2: KNN

## Q1. What is the main difference between the Euclidean distance metric and the Manhattan distance metric in KNN? How might this difference affect the performance of a KNN classifier or regressor?

**Answer:**

Euclidean distance and Manhattan distance are two commonly used distance metrics in the K-Nearest Neighbors (KNN) algorithm. They measure the distance between two data points differently.

### 1. Euclidean Distance

Euclidean distance measures the shortest straight-line distance between two points.

**Formula:**

For two points \(P=(x_1,y_1)\) and \(Q=(x_2,y_2)\):

\[
d(P,Q)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
\]

**Example:**

Suppose \(P=(1,2)\) and \(Q=(4,6)\).

\[
d(P,Q)=\sqrt{(4-1)^2+(6-2)^2}
=\sqrt{9+16}=5
\]

### 2. Manhattan Distance

Manhattan distance measures the total distance traveled along horizontal and vertical paths, similar to moving through city streets.

**Formula:**

\[
d(P,Q)=|x_2-x_1|+|y_2-y_1|
\]

**Example:**

Using the same points:

\[
d(P,Q)=|4-1|+|6-2|=3+4=7
\]

### 3. Key Differences

| Feature | Euclidean Distance | Manhattan Distance |
|---|---|---|
| Measurement | Straight-line distance | Sum of absolute coordinate differences |
| Formula | Square root of squared differences | Sum of absolute differences |
| Path | Direct path | Horizontal and vertical paths |
| Sensitivity to large differences | More sensitive because differences are squared | Less sensitive to large differences |
| Applications | Spatial data and continuous numerical features | Grid-based movement and some high-dimensional datasets |

### 4. Effect on KNN Performance

The choice of distance metric affects which data points are considered the nearest neighbors.

- **Euclidean distance:** Often works well when straight-line distance represents meaningful similarity.
- **Manhattan distance:** Can work well when differences across individual features should contribute additively.

Different metrics may select different neighbors, which can change a classification prediction or a regression estimate.

**Conclusion:** The best distance metric depends on the dataset and problem. Both metrics can be evaluated using cross-validation to determine which performs better.

---

## Q2. How do you choose the optimal value of k for a KNN classifier or regressor? What techniques can be used to determine the optimal k value?

**Answer:**

In KNN, the value of \(k\) represents the number of nearest neighbors considered when making a prediction. Choosing the optimal \(k\) is important because it affects the model's accuracy and ability to generalize to unseen data.

### 1. Effect of Different Values of k

**Small value of k:**
- Uses only a few neighbors.
- Can capture local patterns in the data.
- Is more sensitive to noise and outliers.
- May cause overfitting.

**Large value of k:**
- Uses more neighbors to make predictions.
- Produces smoother decision boundaries or regression estimates.
- Is generally less sensitive to individual noisy observations.
- May cause underfitting if important local patterns are ignored.

For example, when \(k=1\), a classification prediction depends on the single nearest training point. When \(k=5\), it usually depends on the majority class among the five nearest points.

### 2. Techniques to Find the Optimal k

**Technique 1: Cross-Validation**

Cross-validation evaluates model performance across different subsets of the training data.

Steps:
1. Select possible \(k\) values, such as 1 to 30.
2. Train and evaluate the model using cross-validation for each value.
3. Calculate the average performance metric.
4. Select the value that provides the best cross-validation performance.

For classification, use metrics such as accuracy or F1-score. For regression, use metrics such as RMSE or MAE.

**Technique 2: Grid Search**

Grid search evaluates a predefined set of hyperparameter combinations using cross-validation.

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier())
])

param_grid = {
    "knn__n_neighbors": range(1, 31)
}

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy"
)

grid_search.fit(X_train, y_train)

print("Best k:", grid_search.best_params_["knn__n_neighbors"])
print("Best CV accuracy:", grid_search.best_score_)
```

The pipeline ensures that scaling is fitted within each cross-validation training fold.

**Technique 3: Elbow Method**

The elbow method plots the model's error against different values of \(k\).

- Test several values of \(k\).
- Calculate the error for each value.
- Plot \(k\) against the error.
- Look for a point where improvements in error begin to diminish.

The elbow may not always be clear, so cross-validation is generally a more reliable way to select \(k\).

### 3. Important Considerations

- Scale features before calculating distances.
- Choose an appropriate evaluation metric.
- Use stratified cross-validation for classification when suitable.
- Tune hyperparameters using training data only, leaving the test set untouched until final evaluation.

**Conclusion:** Cross-validation and grid search are effective techniques for selecting \(k\). The best value is the one that generalizes well rather than simply achieving the highest training accuracy.

---

## Q3. How does the choice of distance metric affect the performance of a KNN classifier or regressor? In what situations might you choose one distance metric over the other?

**Answer:**

The distance metric determines how KNN measures similarity between data points. Since KNN makes predictions using nearby observations, the metric affects which neighbors are selected and therefore influences predictions.

### 1. Common Distance Metrics

**A. Euclidean Distance**

Measures the straight-line distance between two points.

\[
d(x,y)=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
\]

**When to use:**
- Continuous numerical features.
- Spatial coordinates.
- Datasets where straight-line distance represents meaningful similarity.

**B. Manhattan Distance**

Measures the sum of the absolute differences between corresponding features.

\[
d(x,y)=\sum_{i=1}^{n}|x_i-y_i|
\]

**When to use:**
- Grid-based movement.
- Problems where additive feature differences are meaningful.
- Certain high-dimensional datasets where it performs better empirically than Euclidean distance.

**C. Minkowski Distance**

Minkowski distance is a generalized distance metric that includes Euclidean and Manhattan distances as special cases.

\[
d(x,y)=\left(\sum_{i=1}^{n}|x_i-y_i|^p\right)^{1/p}
\]

Here, \(p\) determines the type of distance:
- \(p=1\): Manhattan distance.
- \(p=2\): Euclidean distance.

### 2. Comparison of Distance Metrics

| Distance Metric | Main Characteristic | Suitable Situations |
|---|---|---|
| Euclidean | Straight-line distance | Continuous numerical data and spatial problems |
| Manhattan | Sum of absolute differences | Grid-based movement and additive differences |
| Minkowski | Generalized distance | When the distance exponent needs adjustment |
| Hamming | Counts positions that differ | Binary or categorical representations |
| Cosine distance | Measures difference in vector direction | Text vectors and high-dimensional representations |

**Note:** Hamming and cosine distances are not interchangeable with numerical distance metrics in every situation. The appropriate metric depends on the data representation and the meaning of similarity.

### 3. How Distance Metrics Affect Performance

Suppose a dataset contains two features: age and annual income. If income ranges from 20,000 to 100,000 while age ranges from 18 to 60, income may dominate distance calculations because it has a much larger numerical scale.

To address this problem, apply feature scaling, such as standardization:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Fit the scaler only on the training data to avoid data leakage.

After scaling, compare distance metrics using cross-validation.

**Conclusion:** No single distance metric is best for every dataset. Choose a metric based on the data and validate its performance experimentally.

---

## Q4. What are some common hyperparameters in KNN classifiers and regressors, and how do they affect the performance of the model? How might you go about tuning these hyperparameters to improve model performance?

**Answer:**

Hyperparameters are settings chosen before model fitting that influence how an algorithm makes predictions. In KNN, they determine how neighbors are selected and how their information is used.

### 1. Common KNN Hyperparameters

| Hyperparameter | Description | Effect on Performance |
|---|---|---|
| `n_neighbors` | Number of neighbors considered | Small values may overfit; large values may underfit |
| `weights` | Determines each neighbor's contribution | Distance weighting gives closer neighbors greater influence |
| `metric` | Specifies the distance metric | Changes which observations are considered nearest |
| `p` | Minkowski distance exponent | `p=1` gives Manhattan distance; `p=2` gives Euclidean distance |
| `algorithm` | Method used to find nearest neighbors | Affects computational efficiency |
| `leaf_size` | Controls leaf size for tree-based search algorithms | Can affect search speed and memory usage |
| `n_jobs` | Number of parallel jobs used during neighbor searches | Can improve computational speed in supported operations |

### 2. Explanation of Important Hyperparameters

**A. `n_neighbors`**

Determines how many neighbors contribute to a prediction.

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5)
```

The model considers the five nearest training observations.

**B. `weights`**

Controls how much influence each neighbor has.

- `"uniform"`: All neighbors have equal weight.
- `"distance"`: Closer neighbors receive greater weight.

Example:

```python
model = KNeighborsClassifier(
    n_neighbors=5,
    weights="distance"
)
```

**C. `metric` and `p`**

These parameters control distance calculations.

```python
model = KNeighborsClassifier(
    n_neighbors=5,
    metric="minkowski",
    p=1
)
```

This configuration uses Manhattan distance.

### 3. Hyperparameter Tuning Using Grid Search

Grid search evaluates combinations of hyperparameters using cross-validation.

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier())
])

param_grid = {
    "knn__n_neighbors": [3, 5, 7, 9, 11, 15],
    "knn__weights": ["uniform", "distance"],
    "knn__metric": ["minkowski"],
    "knn__p": [1, 2]
}

grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="accuracy"
)

grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print("Best CV score:", grid_search.best_score_)
```

For regression, replace `KNeighborsClassifier` with `KNeighborsRegressor` and use an appropriate scoring metric, such as negative mean squared error.

### 4. How to Improve Model Performance

1. Scale numerical features.
2. Tune the number of neighbors.
3. Compare uniform and distance-based weighting.
4. Test different distance metrics.
5. Use cross-validation to evaluate combinations.
6. Select suitable performance metrics.
7. Evaluate the final model on an untouched test set.

**Conclusion:** Hyperparameter tuning helps identify an effective KNN configuration. Grid search, cross-validation, and feature scaling are useful techniques for improving performance.

---

## Q5. How does the size of the training set affect the performance of a KNN classifier or regressor? What techniques can be used to optimize the size of the training set?

**Answer:**

The size of the training set affects KNN's accuracy, generalization ability, memory requirements, and prediction speed.

Unlike many machine learning algorithms, KNN is a lazy learning algorithm. It stores the training observations and uses them to make predictions when new data arrives.

### 1. Effect of Training Set Size

**A. Small Training Set**

Advantages:
- Requires less memory.
- Provides faster predictions because fewer observations need to be searched.
- Requires less time to prepare the dataset.

Disadvantages:
- May not represent the underlying data distribution.
- May produce inaccurate predictions.
- Can struggle with rare classes and unusual patterns.

**B. Large Training Set**

Advantages:
- Can represent the underlying data distribution more effectively.
- May improve predictions when additional observations are informative and representative.
- Can improve the representation of minority classes.

Disadvantages:
- Requires more memory.
- Can increase prediction time.
- May introduce redundant, noisy, or misleading observations.

A larger training set does not automatically guarantee better performance. Data quality and representativeness are also important.

### 2. Techniques to Optimize Training Set Size

**Technique 1: Learning Curves**

Learning curves show how model performance changes as the training set grows.

Steps:
1. Train KNN using different training set sizes.
2. Calculate training and validation scores.
3. Plot the scores against training set size.
4. Determine whether adding more data improves validation performance.

If validation performance continues improving, more training data may help. If it has stabilized, other improvements may be more useful.

**Technique 2: Data Sampling**

Select a representative subset of available data when the full dataset is too large.

Possible approaches include:
- Random sampling.
- Stratified sampling for classification.
- Sampling based on relevant groups or time periods.

Stratified sampling can help preserve class proportions.

**Technique 3: Feature Selection**

Remove irrelevant or redundant features. Fewer features can reduce distance calculations and help address the curse of dimensionality.

**Technique 4: Dimensionality Reduction**

Techniques such as Principal Component Analysis (PCA) can reduce the number of dimensions while retaining important information.

However, dimensionality reduction should be validated because it may discard information relevant to the target.

**Technique 5: Efficient Neighbor Search**

Algorithms such as KD-trees and Ball trees can improve nearest-neighbor search efficiency in suitable datasets. Their effectiveness depends on dimensionality and data structure; brute-force search may be competitive or faster in some high-dimensional settings.

**Conclusion:** The goal is not simply to maximize the number of training observations. It is to use a representative, high-quality dataset that provides good predictive performance with reasonable memory and computational requirements.

---

## Q6. What are some potential drawbacks of using KNN as a classifier or regressor? How might you overcome these drawbacks to improve the performance of the model?

**Answer:**

K-Nearest Neighbors is a simple and intuitive machine learning algorithm, but it has several limitations that can affect its performance, especially on large or high-dimensional datasets.

### 1. Major Drawbacks of KNN

**A. High Prediction Time**

KNN may need to calculate distances between a new observation and many training observations.

**Solution:**
- Use KD-trees or Ball trees when suitable.
- Use approximate nearest-neighbor search for large datasets.
- Reduce the training set size carefully when appropriate.

**B. High Memory Requirements**

KNN stores its training data rather than learning a compact model during training.

**Solution:**
- Remove duplicate or redundant observations.
- Use representative sampling.
- Consider prototype selection or compression methods.

**C. Curse of Dimensionality**

As the number of features increases, distances can become less informative. Observations may appear similarly distant, making it harder to identify meaningful neighbors.

**Solution:**
- Apply feature selection.
- Use dimensionality reduction techniques such as PCA.
- Remove irrelevant features.
- Evaluate whether the selected features meaningfully represent similarity.

**D. Sensitivity to Feature Scales**

Features with large numerical ranges can dominate distance calculations.

**Solution:**

Use standardization or normalization before fitting KNN.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)
```

**E. Sensitivity to Noise and Outliers**

Noisy observations and outliers can influence neighbor selection and predictions.

**Solution:**
- Clean the dataset.
- Investigate and handle outliers appropriately.
- Tune the value of `k`.
- Try distance-based weighting.

**F. Difficulty with Imbalanced Datasets**

When one class contains many more observations than another, KNN may favor the majority class.

**Solution:**
- Use suitable evaluation metrics, such as precision, recall, and F1-score.
- Apply class-imbalance techniques, such as carefully validated oversampling or undersampling.
- Use stratified train-test splitting.
- Consider class-sensitive approaches where appropriate.

**G. Poor Performance with Irrelevant Features**

Irrelevant features can distort distance calculations and cause the algorithm to select less useful neighbors.

**Solution:**
- Perform feature selection.
- Use domain knowledge to identify relevant variables.
- Compare different feature subsets through cross-validation.

### 2. Summary Table

| Drawback | Effect | Possible Solution |
|---|---|---|
| Slow predictions | Increased prediction time | KD-trees, Ball trees, or approximate search |
| High memory usage | Requires more storage | Sampling and prototype selection |
| Curse of dimensionality | Distances become less informative | Feature selection and PCA |
| Different feature scales | Some features dominate distances | StandardScaler or MinMaxScaler |
| Noise and outliers | Unreliable predictions | Data cleaning and hyperparameter tuning |
| Imbalanced classes | Bias toward majority class | Resampling and suitable evaluation metrics |
| Irrelevant features | Poor neighbor selection | Feature selection and domain knowledge |

**Conclusion:** KNN is useful because it is simple and easy to understand, but it can be computationally expensive and sensitive to data characteristics. Feature scaling, feature selection, hyperparameter tuning, and efficient neighbor-search techniques can help overcome many of its limitations.
