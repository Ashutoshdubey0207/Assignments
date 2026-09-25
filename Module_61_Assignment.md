# Regression Analysis and Regularization — Assignment Answers

## Q1. Explain the concept of R-squared in linear regression models. How is it calculated, and what does it represent?

### Answer

**R-squared (R²)**, also called the **coefficient of determination**, is a regression evaluation metric that measures how much of the variation in the target variable is explained by the independent variables in the regression model.

In simple words, R² tells us:

> **How well does the regression model explain the variability in the target variable?**

### Formula

\[
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
\]

Where:

- **SS_res (Residual Sum of Squares)** = sum of squared differences between actual and predicted values.
- **SS_tot (Total Sum of Squares)** = sum of squared differences between actual values and their mean.

It can also be written as:

\[
R^2 = 1 - \frac{\sum(y_i-\hat{y}_i)^2}{\sum(y_i-\bar{y})^2}
\]

Where:

- \(y_i\) = actual value
- \(\hat{y}_i\) = predicted value
- \(\bar{y}\) = mean of actual target values

### Interpretation

An R² value is commonly interpreted as follows:

- **R² = 1** → the model explains 100% of the variation in the target.
- **R² = 0** → the model does not explain more variation than simply using the target mean as the prediction.
- **R² between 0 and 1** → the model explains that proportion of the variation.

For example, if:

\[
R^2 = 0.80
\]

it means that approximately **80% of the variation in the target variable is explained by the predictors in the model**.

The remaining 20% is not explained by the model and may be due to other variables, noise, measurement error, or an unsuitable model.

### Example

Suppose we are predicting house prices using:

- Area
- Number of bedrooms
- Age of the house
- Location-related features

If the model produces:

\[
R^2 = 0.85
\]

then the model explains approximately **85% of the variation in house prices in the data being evaluated**.

### Important limitation

A high R² does **not automatically mean that the model is good**. It does not tell us how large the prediction errors are in the original units, and adding more predictors can increase R² even when those predictors are not genuinely useful.

Therefore, R² should often be considered along with metrics such as **MAE, RMSE, and adjusted R²**.

---

## Q2. Define adjusted R-squared and explain how it differs from the regular R-squared.

### Answer

**Adjusted R-squared** is a modified version of R² that takes into account the **number of predictors in the model and the sample size**.

Regular R² generally increases or stays the same when additional predictors are added, even if those predictors contribute very little useful information.

Adjusted R² addresses this problem by applying a penalty for adding unnecessary predictors.

### Formula

\[
Adjusted\ R^2 =
1-(1-R^2)\frac{n-1}{n-p-1}
\]

Where:

- \(R^2\) = regular R-squared
- \(n\) = number of observations
- \(p\) = number of independent variables/predictors

### Difference between R² and Adjusted R²

| R² | Adjusted R² |
|---|---|
| Measures explained variation | Measures explained variation while accounting for model complexity |
| Does not penalize extra predictors | Penalizes unnecessary predictors |
| Usually increases when predictors are added | Can increase or decrease |
| Useful for understanding explanatory power | Useful for comparing models with different numbers of predictors |

### Example

Suppose a model initially has 3 predictors:

\[
R^2 = 0.80
\]

Now we add 5 more predictors that provide very little useful information.

The R² might increase to:

\[
R^2 = 0.83
\]

However, adjusted R² might decrease because the additional variables do not provide enough improvement to justify their inclusion.

Therefore, adjusted R² helps us determine whether adding predictors actually improves the model after considering model complexity.

---

## Q3. When is it more appropriate to use adjusted R-squared?

### Answer

Adjusted R² is more appropriate when we are **comparing regression models containing different numbers of predictors**.

Regular R² has a major limitation: adding another predictor can increase R² even when the new predictor contributes very little useful information.

Adjusted R² applies a penalty for additional predictors.

### Example

Suppose we have two models for predicting house prices:

**Model A:**

- Area
- Bedrooms
- Age

\[
R^2 = 0.82
\]

**Model B:**

- Area
- Bedrooms
- Age
- Distance from airport
- Number of trees
- Random feature
- Several other variables

Suppose:

\[
R^2 = 0.85
\]

Looking only at R², Model B appears better.

However, after accounting for the additional predictors:

\[
Adjusted\ R^2_A = 0.81
\]

\[
Adjusted\ R^2_B = 0.80
\]

In this situation, adjusted R² indicates that the additional predictors did not improve the model enough to justify the increased complexity.

### Therefore, adjusted R² is particularly useful when:

1. Comparing models with different numbers of predictors.
2. Evaluating whether additional variables genuinely improve a linear regression model.
3. Trying to avoid unnecessary model complexity.
4. Performing multiple linear regression with many potential predictors.

### Important point

Adjusted R² is not a replacement for test-set metrics such as RMSE or MAE. For predictive performance on unseen data, evaluation on validation/test data is still important.

---

## Q4. What are RMSE, MSE, and MAE in the context of regression analysis? How are these metrics calculated, and what do they represent?

### Answer

**RMSE, MSE, and MAE** are commonly used regression evaluation metrics. They measure the difference between the actual target values and the values predicted by a regression model.

Let:

- \(y_i\) = actual value
- \(\hat{y}_i\) = predicted value
- \(n\) = number of observations

### 1. MSE — Mean Squared Error

MSE is calculated as:

\[
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
\]

MSE squares each prediction error before taking the average.

### What does MSE represent?

It represents the **average squared prediction error**.

Because errors are squared, large errors have a much greater effect on MSE.

For example:

\[
2^2=4
\]

but:

\[
10^2=100
\]

Therefore, MSE strongly penalizes large prediction errors.

---

### 2. RMSE — Root Mean Squared Error

RMSE is the square root of MSE:

\[
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
\]

### What does RMSE represent?

RMSE represents the typical magnitude of prediction error while giving **greater importance to large errors**.

An important advantage is that RMSE has the **same unit as the target variable**.

For example, if we are predicting house prices in thousands of dollars, RMSE is also expressed in thousands of dollars.

---

### 3. MAE — Mean Absolute Error

MAE is calculated as:

\[
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
\]

MAE takes the absolute value of each error and then calculates the average.

### What does MAE represent?

MAE represents the **average absolute difference between actual and predicted values**.

For example:

\[
MAE=5
\]

means that, on average, the predictions are approximately 5 units away from the actual values.

### Simple comparison

| Metric | Calculation | Effect of large errors |
|---|---|---|
| MSE | Average squared errors | Very high |
| RMSE | Square root of MSE | High |
| MAE | Average absolute errors | Lower |

---

## Q5. Discuss the advantages and disadvantages of using RMSE, MSE, and MAE as evaluation metrics in regression analysis.

### Answer

Each metric has different advantages and disadvantages.

### MSE

#### Advantages

1. **Strongly penalizes large errors.**
2. Useful when large prediction errors are particularly undesirable.
3. Differentiable, which is useful for optimization algorithms.

#### Disadvantages

1. Because errors are squared, MSE is highly sensitive to outliers.
2. Its units are squared, making it less intuitive to interpret.
3. A few very large errors can dominate the metric.

---

### RMSE

#### Advantages

1. Strongly penalizes large errors.
2. Has the **same units as the target variable**, making interpretation easier.
3. Commonly used for regression model evaluation.
4. Useful when large errors are more costly than small errors.

#### Disadvantages

1. Sensitive to outliers.
2. A few large errors can significantly increase RMSE.
3. It may give a different picture from MAE when the dataset contains extreme errors.

---

### MAE

#### Advantages

1. Easy to understand and interpret.
2. Has the same units as the target variable.
3. Less sensitive to outliers than MSE and RMSE.
4. Treats errors more uniformly.

#### Disadvantages

1. It does not penalize large errors as strongly as RMSE.
2. It may be less appropriate when very large errors are especially costly.
3. It is less convenient than squared-error losses for some optimization methods.

### Example

Suppose two models make the following errors:

```text
Model A: 2, 3, 4, 5
Model B: 1, 2, 3, 20
```

Model B has one very large error.

MAE will increase for Model B, but RMSE will increase **much more strongly** because the error of 20 is squared.

Therefore:

- Use **RMSE** when large errors should receive greater punishment.
- Use **MAE** when you want a more robust measure of typical error.
- Use **MSE** when squared error is appropriate for the analysis or optimization.

---

## Q6. Explain the concept of Lasso regularization. How does it differ from Ridge regularization, and when is it more appropriate to use?

### Answer

**Lasso** stands for **Least Absolute Shrinkage and Selection Operator**.

Lasso is a regularization technique used in linear regression to reduce overfitting and, importantly, perform **feature selection**.

It adds an **L1 penalty** to the ordinary least-squares loss function.

### Lasso formula

\[
Loss = MSE + \lambda\sum_{j=1}^{p}|\beta_j|
\]

Where:

- \(\lambda\) = regularization strength
- \(\beta_j\) = coefficient of feature \(j\)
- \(p\) = number of features

As λ increases, the penalty becomes stronger and coefficients are pushed closer to zero.

Some coefficients can become **exactly zero**.

### Example

Suppose we have:

```text
Before Lasso:

Area       → 5.2
Bedrooms   → 2.8
Age        → -0.5
Noise      → 0.3
```

After applying Lasso:

```text
Area       → 4.8
Bedrooms   → 2.4
Age        → -0.3
Noise      → 0
```

The `Noise` feature has a coefficient of zero, so it is effectively removed from the model.

### Ridge vs Lasso

| Ridge | Lasso |
|---|---|
| Uses L2 regularization | Uses L1 regularization |
| Penalizes squared coefficients | Penalizes absolute coefficients |
| Shrinks coefficients toward zero | Can make coefficients exactly zero |
| Usually keeps all features | Can perform feature selection |
| Useful with multicollinearity | Useful when feature selection is desired |

### When is Lasso more appropriate?

Lasso can be particularly useful when:

- There are many features.
- We suspect that only a subset of features is important.
- We want a simpler and more interpretable model.
- Feature selection is an important objective.

### Limitation

When predictors are highly correlated, Lasso may select one feature and shrink another correlated feature to zero. Therefore, the selected features should not automatically be interpreted as the only scientifically important features.

---

## Q7. How do regularized linear models help to prevent overfitting in machine learning? Provide an example to illustrate.

### Answer

**Regularization** is a technique used to reduce overfitting by adding a penalty for large model coefficients.

### What is overfitting?

Overfitting occurs when a model learns the training data too closely, including noise and random patterns.

The result is often:

```text
Training performance → Very good
Test performance     → Poor
```

A regularized model tries to control this by discouraging unnecessarily large coefficients.

### Basic idea

Ordinary linear regression minimizes:

\[
Loss = MSE
\]

Regularized regression minimizes:

\[
Loss = MSE + Penalty
\]

For example:

- Ridge → L2 penalty
- Lasso → L1 penalty

### Example

Suppose we are predicting house prices using 20 features.

Without regularization, the model may learn very large coefficients:

```text
Area             → 8.5
Bedrooms         → 6.2
Age              → -2.1
Random feature   → 15.8
Noise feature    → -12.4
```

The model may be fitting noise in the training data.

After regularization:

```text
Area             → 6.8
Bedrooms         → 4.9
Age              → -1.2
Random feature   → 1.1
Noise feature    → -0.7
```

The model becomes less sensitive to random variations.

This may cause a small increase in training error but can improve performance on unseen data.

### Important trade-off

Regularization should not be too weak or too strong.

```text
Very little regularization → Overfitting
Appropriate regularization → Better generalization
Too much regularization    → Underfitting
```

Therefore, regularization helps balance **model complexity and generalization**.

---

## Q8. Discuss the limitations of regularized linear models and explain why they may not always be the best choice for regression analysis.

### Answer

Regularized linear models such as Ridge, Lasso, and Elastic Net are useful for controlling overfitting, but they are not suitable for every regression problem.

### 1. They still assume a linear relationship

Regularization does not change the fundamental structure of a linear model.

If the true relationship between the features and target is highly nonlinear, a regularized linear model may still underfit.

For example, if:

\[
y=x^2
\]

a basic linear model cannot naturally represent the curved relationship.

---

### 2. Too much regularization can cause underfitting

If λ is too large, coefficients are heavily shrunk toward zero.

Important relationships may then be weakened.

```text
λ too small → insufficient regularization → overfitting
λ appropriate → good balance
λ too large → excessive regularization → underfitting
```

---

### 3. Regularization introduces bias

Regularization intentionally introduces some bias into coefficient estimates.

This is part of the **bias-variance trade-off**:

> A little more bias can reduce variance and improve generalization.

However, excessive bias can lead to poor predictions.

---

### 4. Lasso can remove useful variables

Lasso can set coefficients exactly to zero.

When predictors are correlated, Lasso may keep one variable and remove another variable that also contains useful information.

Therefore, a coefficient of zero does not always mean that the feature is completely irrelevant.

---

### 5. Hyperparameter tuning is required

The regularization parameter λ must be chosen appropriately.

Cross-validation is commonly used to select a suitable value.

This adds an additional model-selection step.

---

### 6. They are not specifically designed for outliers

Ridge and Lasso do not automatically make regression robust to extreme outliers.

Large unusual observations can still affect the fitted model.

Outlier detection and appropriate data preprocessing may therefore still be necessary.

### Why might another model be better?

If the dataset contains complex nonlinear patterns, models such as:

- Random Forest
- Gradient Boosting
- Decision Trees
- Neural Networks

may capture those patterns more effectively.

### Conclusion

Regularized linear models are useful when the relationship is approximately linear and we need to control overfitting, multicollinearity, or feature complexity. However, they may not be the best choice when the data contains strong nonlinear relationships or other complex patterns.

---

## Q9. You are comparing the performance of two regression models using different evaluation metrics. Model A has an RMSE of 10, while Model B has an MAE of 8. Which model would you choose as the better performer, and why? Are there any limitations to your choice of metric?

### Answer

We **cannot determine which model is better simply from these values**:

- Model A → RMSE = 10
- Model B → MAE = 8

The reason is that **RMSE and MAE are different evaluation metrics**.

Although both measure prediction error, they calculate the error differently.

### RMSE

\[
RMSE=\sqrt{\frac{1}{n}\sum(y_i-\hat{y}_i)^2}
\]

RMSE squares the errors before averaging them. Therefore, **large errors have a much greater influence**.

### MAE

\[
MAE=\frac{1}{n}\sum|y_i-\hat{y}_i|
\]

MAE takes the absolute value of errors and averages them. It is therefore **less sensitive to large errors** than RMSE.

### Why can't we compare 10 and 8 directly?

The values come from different calculations.

It is similar to saying:

```text
Model A → 10 kilometers
Model B → 8 kilograms
```

We cannot say 8 is better than 10 because they measure different things.

### Correct approach

Evaluate both models using the **same metric on the same test dataset**.

For example:

| Model | RMSE | MAE |
|---|---:|---:|
| Model A | 10 | 7 |
| Model B | 12 | 8 |

Now we can compare the models using RMSE or MAE.

### Which metric should be selected?

It depends on the problem.

**RMSE is useful when:**

- Large errors are particularly costly.
- We want large errors to receive more penalty.
- Extreme prediction mistakes are important.

**MAE is useful when:**

- We want an easily interpretable average error.
- We do not want outliers to dominate the metric.
- Typical prediction error is more important than extreme errors.

### Limitation

There is no universally best regression metric.

The choice depends on the **business problem, data distribution, and cost of prediction errors**.

### Final conclusion

> **Neither Model A nor Model B can be declared better based only on RMSE = 10 and MAE = 8. The models should be evaluated using the same metric on the same test dataset. RMSE is more sensitive to large errors, whereas MAE provides a more direct measure of average absolute error.**

---

## Q10. You are comparing the performance of two regularized linear models using different types of regularization. Model A uses Ridge regularization with a regularization parameter of 0.1, while Model B uses Lasso regularization with a regularization parameter of 0.5. Which model would you choose as the better performer, and why? Are there any trade-offs or limitations to your choice of regularization method?

### Answer

We **cannot determine which model is better simply by comparing λ = 0.1 and λ = 0.5**.

The reason is that Ridge and Lasso use **different regularization penalties**.

- Model A → Ridge, λ = 0.1
- Model B → Lasso, λ = 0.5

The numerical values of λ are therefore **not directly comparable**.

### Ridge Regularization

Ridge uses an **L2 penalty**:

\[
Loss=MSE+\lambda\sum\beta_j^2
\]

Ridge shrinks coefficients toward zero but generally does not make them exactly zero.

For example:

```text
Before Ridge:
X1 → 10
X2 → 8
X3 → 5

After Ridge:
X1 → 7.5
X2 → 6.2
X3 → 3.8
```

The features remain in the model.

### Lasso Regularization

Lasso uses an **L1 penalty**:

\[
Loss=MSE+\lambda\sum|\beta_j|
\]

Lasso can shrink some coefficients exactly to zero.

For example:

```text
Before Lasso:
X1 → 10
X2 → 8
X3 → 5

After Lasso:
X1 → 7.2
X2 → 0
X3 → 3.1
```

Here, X2 is effectively removed from the model.

### How should we compare the two models?

We should train both models and evaluate them using the **same evaluation metric and the same test/validation data**.

For example:

| Model | Method | λ | RMSE | R² |
|---|---|---:|---:|---:|
| A | Ridge | 0.1 | 8.5 | 0.88 |
| B | Lasso | 0.5 | 10.2 | 0.82 |

In this example, Model A has lower RMSE and higher R², so it has better measured predictive performance on this test set.

However, if Model B produced lower RMSE and better test-set performance, we would choose Model B instead.

### Trade-offs

#### Ridge

**Advantages:**

- Handles multicollinearity well.
- Works well when many features contribute to the target.
- Keeps all features in the model.
- Produces relatively stable coefficient estimates.

**Limitation:**

- It generally does not perform feature selection because coefficients usually remain non-zero.

#### Lasso

**Advantages:**

- Performs feature selection.
- Produces a simpler model.
- Can improve interpretability when many features are irrelevant.

**Limitations:**

- Can remove useful features.
- Can behave unpredictably when predictors are strongly correlated.
- The selected variables should not automatically be interpreted as the only important variables.

### Final conclusion

> **We should not choose between Model A and Model B based only on their regularization parameters. Ridge with λ = 0.1 is not automatically better than Lasso with λ = 0.5. The two models should be evaluated using the same metric on the same validation/test data. Ridge is generally preferred when we want to retain correlated features and stabilize coefficients, while Lasso is useful when feature selection and a simpler model are important.**
