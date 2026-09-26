# Module 63 Assignment — Lasso Regression

## Q1. What is Lasso Regression, and how does it differ from other regression techniques?

Lasso Regression (Least Absolute Shrinkage and Selection Operator) is a linear regression technique that adds an L1 regularization penalty to ordinary least squares regression.

The cost function is:

Cost = RSS + λ Σ|βⱼ|

Where:
- RSS = Residual Sum of Squares
- λ (lambda) = regularization parameter
- βⱼ = regression coefficients

The key difference is that Lasso can force some coefficients exactly to zero, which performs automatic feature selection.

- Linear Regression → no regularization
- Ridge Regression → L2 regularization
- Lasso Regression → L1 regularization

---

## Q2. What is the main advantage of using Lasso Regression in feature selection?

The biggest advantage is automatic feature selection.

Lasso can reduce some coefficients exactly to zero. Features whose coefficients become zero are effectively excluded from the model.

For example:

| Feature | Coefficient |
|---|---:|
| Age | 2.5 |
| Income | 0.8 |
| Education | 0.0 |
| Experience | 4.1 |
| Location | 0.0 |

Lasso has effectively selected Age, Income, and Experience.

---

## Q3. How do you interpret the coefficients of a Lasso Regression model?

The coefficients are interpreted similarly to ordinary linear regression.

For example:

Salary = 20 + 5(Experience) - 2(Age)

Interpretation:
- Intercept = 20 → predicted salary when all features are zero.
- Experience coefficient = 5 → a one-unit increase in experience increases predicted salary by 5 units, keeping other features constant.
- Age coefficient = -2 → a one-unit increase in age decreases predicted salary by 2 units, keeping other features constant.

In Lasso, if a coefficient becomes 0, that feature has effectively been excluded from the model.

---

## Q4. What are the tuning parameters that can be adjusted in Lasso Regression, and how do they affect the model's performance?

The most important tuning parameter is alpha (often represented mathematically as lambda, λ).

### Small λ / alpha

- Less regularization
- Coefficients remain larger
- Model behaves more like Linear Regression
- Greater risk of overfitting

### Large λ / alpha

- More regularization
- Coefficients shrink more
- More coefficients may become zero
- Model becomes simpler
- Too much regularization can cause underfitting

Example in Scikit-learn:

```python
from sklearn.linear_model import Lasso

model = Lasso(alpha=0.1)
```

Other parameters such as `max_iter` and `tol` control the optimization process rather than the regularization strength itself.

---

## Q5. Can Lasso Regression be used for non-linear regression problems? If yes, how?

Yes.

Lasso itself is a linear model, but it can model nonlinear relationships by creating nonlinear features, such as polynomial features.

For example:

y = β₀ + β₁x + β₂x² + β₃x³

Then Lasso can be applied to these polynomial features.

Example:

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline

model = Pipeline([
    ("poly", PolynomialFeatures(degree=2)),
    ("lasso", Lasso(alpha=0.1))
])

model.fit(X_train, y_train)
```

Lasso can also remove some polynomial features by making their coefficients zero.

---

## Q6. What is the difference between Ridge Regression and Lasso Regression?

| Feature | Ridge Regression | Lasso Regression |
|---|---|---|
| Regularization | L2 | L1 |
| Penalty | λΣβⱼ² | λΣ|βⱼ| |
| Coefficients | Shrinks coefficients | Shrinks coefficients |
| Can make coefficients exactly 0? | Usually no | Yes |
| Feature selection | Not directly | Yes |
| Multicollinearity | Handles it well | Can handle it |
| Main use | Shrink coefficients | Shrink and select features |

Easy way to remember:

- Ridge → Reduce the size of coefficients.
- Lasso → Select features by making some coefficients zero.

---

## Q7. Can Lasso Regression handle multicollinearity in the input features? If yes, how?

Yes.

Lasso can help deal with multicollinearity by shrinking coefficients and potentially setting some coefficients to zero.

For example, if House Size, Number of Rooms, and Number of Bedrooms are highly correlated, Lasso may retain some features and reduce or remove others.

However, when several features are strongly correlated, Lasso's feature selection can be unstable. It may select one correlated feature and discard another similar feature depending on the data.

Therefore, Lasso helps with multicollinearity, but it does not eliminate the underlying correlation between the variables.

---

## Q8. How do you choose the optimal value of the regularization parameter (lambda) in Lasso Regression?

The usual approach is cross-validation.

Different values of lambda/alpha are tested, and the model's validation performance is compared.

For example:

- 0.001
- 0.01
- 0.1
- 1
- 10

The value that gives the best cross-validation performance is selected.

Scikit-learn provides `LassoCV` for this:

```python
from sklearn.linear_model import LassoCV

model = LassoCV(cv=5, random_state=42)

model.fit(X_train, y_train)

print("Best alpha:", model.alpha_)
```

Here, `cv=5` means 5-fold cross-validation.

`model.alpha_` gives the selected regularization strength.

### Summary

Try different lambda/alpha values → use cross-validation → compare validation error → select the best value → train the final Lasso model.
