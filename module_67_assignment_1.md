# Module 67 — Assignment 1
## Decision Tree Classification and Evaluation Metrics

### Q1. Describe the decision tree classifier algorithm and how it works to make predictions.

A **Decision Tree Classifier** is a supervised machine learning algorithm used to classify data into different categories based on input features. It works like a flowchart by asking a series of questions and making decisions based on the answers.

For example, it can predict whether an email is spam or not spam based on features such as the sender, keywords, and number of links.

**Main components of a decision tree:**
- **Root node:** The first node that represents the entire dataset.
- **Decision node:** A node where a condition is applied to split the data.
- **Branch:** The outcome of a decision or condition.
- **Leaf node:** The final node that provides the predicted class.

**How the algorithm works:**
1. Start with the complete training dataset.
2. Examine available features and select the best feature for splitting the data.
3. Divide the dataset into smaller groups based on a condition.
4. Repeat this process for the resulting groups until a stopping condition is reached.
5. Assign a class to each leaf node based on the training samples that reach it.
6. For new data, follow the decision rules from the root to a leaf and predict the corresponding class.

**Example:** To predict whether a person will play cricket, a tree might ask whether the weather is sunny. If yes, it may check humidity. If humidity is high, predict “No”; otherwise, predict “Yes.”

---

### Q2. Provide a step-by-step explanation of the mathematical intuition behind decision tree classification.

The mathematical intuition behind a decision tree is to find the best feature and threshold that divide the dataset into groups containing as similar class labels as possible.

#### Step 1: Calculate impurity

Impurity measures how mixed the class labels are within a dataset. Two common measures are **Gini impurity** and **entropy**.

**Gini impurity:**

\[
Gini(D)=1-\sum_{i=1}^{K}p_i^2
\]

Where:
- \(D\) is the dataset at a node.
- \(K\) is the number of classes.
- \(p_i\) is the proportion of samples belonging to class \(i\).

Suppose a node contains 6 positive and 4 negative samples:

\[
p_+=\frac{6}{10}=0.6,\qquad p_-=\frac{4}{10}=0.4
\]

\[
Gini(D)=1-(0.6^2+0.4^2)=0.48
\]

A Gini impurity of zero means the node contains samples from only one class.

**Entropy:**

\[
H(D)=-\sum_{i=1}^{K}p_i\log_2(p_i)
\]

Entropy measures uncertainty or disorder in a node. It is zero when all samples belong to the same class.

#### Step 2: Evaluate possible splits

The algorithm considers different features and thresholds to determine how effectively each split separates the classes.

For example, the feature age could be split using:

\[
Age\leq 30
\]

This creates two groups: age less than or equal to 30, and age greater than 30.

#### Step 3: Calculate weighted impurity after splitting

The impurity of child nodes is combined using their relative sizes:

\[
I_{\text{split}}=\frac{N_L}{N}I_L+\frac{N_R}{N}I_R
\]

Where \(N\) is the total number of samples, \(N_L,N_R\) are the numbers of samples in the left and right child nodes, and \(I_L,I_R\) are their impurity values.

Suppose a split produces:
- Left child: 5 positive and 0 negative samples.
- Right child: 1 positive and 4 negative samples.

The left child has Gini impurity \(0\). The right child has:

\[
Gini_R=1-\left(\frac15\right)^2-\left(\frac45\right)^2=0.32
\]

The weighted impurity is:

\[
I_{\text{split}}=\frac5{10}(0)+\frac5{10}(0.32)=0.16
\]

The original impurity was \(0.48\), so this split improves class separation.

#### Step 4: Select the best split

The algorithm chooses the split that produces the greatest impurity reduction:

\[
\text{Gini Gain}=Gini(D)-I_{\text{split}}
\]

\[
\text{Gini Gain}=0.48-0.16=0.32
\]

A larger gain indicates a more effective split. When entropy is used, the corresponding measure is called **information gain**.

#### Step 5: Repeat recursively

The algorithm applies the same procedure to child nodes until it reaches a stopping condition, such as maximum depth, minimum samples per node, or sufficiently pure leaves.

#### Step 6: Make predictions

For a new observation, the model follows the decision rules until it reaches a leaf node. It predicts the majority class at that leaf, or class probabilities based on the samples there.

---

### Q3. Explain how a decision tree classifier can be used to solve a binary classification problem.

A **binary classification problem** is a machine learning problem in which the target variable has only two possible classes, such as Yes/No, True/False, or 0/1.

For example, a decision tree can predict whether a person has diabetes using features such as glucose level, BMI, and age.

**Steps:**
1. **Collect data:** Gather records containing input features and target labels.
2. **Prepare data:** Handle missing values, encode categorical variables if required, and split data into training and testing sets.
3. **Train the model:** The tree learns conditions that separate the two classes using Gini impurity or entropy.
4. **Create decision rules:** The tree selects features and thresholds that improve class separation.
5. **Predict:** For a new observation, follow the decision rules to predict class 0 or class 1.
6. **Evaluate:** Compare predictions with actual labels using a confusion matrix, precision, recall, F1 score, and other suitable metrics.

**Python example:**

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Input features and binary target
X = [
    [120, 22],
    [180, 32],
    [100, 20],
    [200, 35],
    [130, 25],
    [190, 30]
]

y = [0, 1, 0, 1, 0, 1]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

# Create and train the classifier
model = DecisionTreeClassifier(
    criterion="gini", random_state=42
)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Predictions:", y_pred)
print("Actual values:", y_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
```

Here, the two input features represent glucose level and BMI, and the target labels represent two classes. This is an illustrative dataset, not a real clinical dataset.

**Note:** In a medical application, accuracy alone is not sufficient. Recall, false negatives, data quality, and clinical validation are also important.

---

### Q4. Discuss the geometric intuition behind decision tree classification and how it can be used to make predictions.

The geometric intuition behind a decision tree is that it divides the feature space into smaller regions using decision boundaries. Each region is assigned a predicted class.

Suppose a dataset has two features:
- \(X_1\): Age
- \(X_2\): Income

A tree might use rules such as:
- If age is less than or equal to 30, predict Class A.
- If age is greater than 30 and income is less than or equal to ₹50,000, predict Class B.
- Otherwise, predict Class A.

**How the feature space is divided:**
1. A condition such as \(X_1\leq 30\) creates a vertical boundary in a two-dimensional feature space.
2. A condition such as \(X_2\leq 50{,}000\) creates a horizontal boundary.
3. Additional conditions divide the space into smaller rectangular regions.
4. Each region corresponds to a leaf node that predicts a class.

When a new observation enters the model, its feature values determine which region it belongs to. The model then predicts the class assigned to that region.

Unlike logistic regression, which commonly uses a linear decision boundary, a decision tree can create complex, nonlinear boundaries by combining multiple axis-aligned splits. Its regions are rectangular in the original feature space, although the overall boundary can be irregular.

---

### Q5. Define the confusion matrix and describe how it can be used to evaluate the performance of a classification model.

A **confusion matrix** is a table that compares actual class labels with predicted class labels. It helps identify correct and incorrect predictions.

For binary classification:

| Actual / Predicted | Predicted Positive | Predicted Negative |
|---|---:|---:|
| Actual Positive | True Positive (TP) | False Negative (FN) |
| Actual Negative | False Positive (FP) | True Negative (TN) |

**Four components:**
- **True Positive (TP):** The model correctly predicts the positive class.
- **True Negative (TN):** The model correctly predicts the negative class.
- **False Positive (FP):** The model predicts positive when the actual class is negative.
- **False Negative (FN):** The model predicts negative when the actual class is positive.

The confusion matrix provides the values required to calculate several metrics.

**Accuracy** measures the proportion of all predictions that are correct:

\[
Accuracy=\frac{TP+TN}{TP+TN+FP+FN}
\]

**Precision** measures how many predicted positives are actually positive:

\[
Precision=\frac{TP}{TP+FP}
\]

**Recall** measures how many actual positives the model correctly identifies:

\[
Recall=\frac{TP}{TP+FN}
\]

**F1 score** combines precision and recall:

\[
F1=2\times\frac{Precision\times Recall}{Precision+Recall}
\]

These metrics help identify different types of model errors and determine whether a classifier meets the requirements of an application.

---

### Q6. Provide an example of a confusion matrix and explain how precision, recall, and F1 score can be calculated from it.

Consider a spam email detection model tested on 100 emails, of which 40 are actually spam and 60 are not spam.

| Actual / Predicted | Spam | Not Spam |
|---|---:|---:|
| Actual Spam | TP = 30 | FN = 10 |
| Actual Not Spam | FP = 5 | TN = 55 |

Therefore:
- True Positive = 30
- False Positive = 5
- False Negative = 10
- True Negative = 55

#### 1. Precision

Precision measures the proportion of emails predicted as spam that are actually spam.

\[
Precision=\frac{TP}{TP+FP}=\frac{30}{30+5}
\]

\[
\boxed{Precision=85.71\%}
\]

Approximately 85.71% of emails classified as spam are actually spam.

#### 2. Recall

Recall measures the proportion of actual spam emails that the model successfully identifies.

\[
Recall=\frac{TP}{TP+FN}=\frac{30}{30+10}
\]

\[
\boxed{Recall=75\%}
\]

The model identifies 75% of all actual spam emails. The remaining 25% are missed.

#### 3. F1 score

The F1 score is the harmonic mean of precision and recall.

\[
F1=2\times\frac{P\times R}{P+R}
\]

Using the unrounded values:

\[
F1=2\times\frac{0.8571\times0.75}{0.8571+0.75}
\]

\[
\boxed{F1\approx80\%}
\]

**Interpretation:**
- **Precision (85.71%):** Most emails flagged as spam are genuinely spam.
- **Recall (75%):** The model detects three-quarters of all spam emails.
- **F1 score (80%):** The model achieves a balance between precision and recall.

---

### Q7. Discuss the importance of choosing an appropriate evaluation metric for a classification problem and explain how this can be done.

Choosing an appropriate evaluation metric is important because different classification problems have different objectives and different costs associated with incorrect predictions.

For example, a false negative in cancer screening may delay treatment, whereas a false positive in spam detection may cause a legitimate email to be placed in the spam folder.

**Why the choice of metric matters:**
1. **Different error costs:** False positives and false negatives may have different consequences.
2. **Imbalanced datasets:** Accuracy can be misleading when one class is much more common than another.
3. **Business objectives:** A business may prioritize avoiding unnecessary interventions, identifying as many potential customers as possible, or balancing both goals.
4. **Reliable model comparison:** A suitable metric helps compare models according to the actual problem requirements.

**Common evaluation metrics:**

| Metric | When it is useful |
|---|---|
| Accuracy | When both classes matter and class distribution is reasonably balanced |
| Precision | When false positives are costly |
| Recall | When false negatives are costly |
| F1 score | When both precision and recall matter |
| ROC-AUC | When comparing ranking and discrimination across classification thresholds |
| PR-AUC | Particularly useful for positive-class detection in highly imbalanced datasets |

**How to choose a metric:**
1. Understand the objective of the classification problem.
2. Identify the consequences of false positives and false negatives.
3. Examine the class distribution in the dataset.
4. Select a primary metric that matches the problem requirements.
5. Use additional metrics and the confusion matrix to understand model errors.
6. Choose a decision threshold based on the desired trade-off, and validate the final model on unseen data.

**Example:** For a fraud detection system, recall may be important because missed fraud is costly. However, precision also matters because investigating too many legitimate transactions can waste resources.

The best metric depends on the specific application rather than on a universal rule.

---

### Q8. Provide an example of a classification problem where precision is the most important metric, and explain why.

A suitable example is an **email spam filtering system**, particularly when the system automatically deletes or quarantines emails classified as spam.

Precision is important because incorrectly classifying a legitimate email as spam can cause the user to miss important messages, such as job offers, business communications, or password-reset emails.

Suppose the model classifies 100 emails as spam:
- 95 are genuinely spam.
- 5 are legitimate emails incorrectly classified as spam.

\[
Precision=\frac{TP}{TP+FP}=\frac{95}{100}=95\%
\]

The model has a precision of 95%, meaning that 95% of the emails flagged as spam are genuinely spam.

**Why precision is important:**
- It reduces the number of legitimate emails incorrectly flagged as spam.
- It increases user trust in the filtering system.
- It is valuable when false positives have serious consequences.

**Conclusion:** Precision should be prioritized when false positives are especially costly. However, recall should also be monitored so that excessive numbers of spam emails do not reach the inbox.

---

### Q9. Provide an example of a classification problem where recall is the most important metric, and explain why.

A suitable example is a **medical screening system for detecting a potentially serious disease**, such as cancer.

Recall is important because failing to identify a person who actually has the disease can delay further testing and treatment. In this situation, false negatives can have severe consequences.

Suppose a screening model examines 100 patients who actually have the disease:
- It correctly identifies 95 patients as positive.
- It incorrectly classifies 5 patients as negative.

\[
Recall=\frac{TP}{TP+FN}=\frac{95}{95+5}=95\%
\]

The model has a recall of 95%, meaning that it identifies 95% of the patients who actually have the disease.

**Why recall is important:**
- It reduces the number of actual positive cases that go undetected.
- It helps identify patients who may require further medical testing.
- It is valuable when the consequences of missing a positive case are severe.

**Conclusion:** Recall should be prioritized when false negatives are especially costly. However, high recall can produce more false positives, so confirmatory testing and appropriate clinical evaluation remain necessary.

---

## Quick Revision: Precision vs. Recall

| Precision | Recall |
|---|---|
| Focuses on predicted positive cases | Focuses on actual positive cases |
| \(TP/(TP+FP)\) | \(TP/(TP+FN)\) |
| Helps reduce false positives | Helps reduce false negatives |
| Example: avoiding legitimate emails being marked as spam | Example: detecting as many disease cases as possible |

**Remember:**
- **Precision:** Of everything the model flagged, how much was correct?
- **Recall:** Of everything that should have been flagged, how much did the model find?
