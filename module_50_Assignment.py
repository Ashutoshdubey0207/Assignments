'''Q1: Explain the following with an example:F
C) Artificial Intelligence
Ans = Artificial intelligence (AI) refers to computer systems capable of 
performing complex tasks that historically only humans could do, such as reasoning, making decisions, or solving problems.

<) Machine Learnin,
Ans => Machine learning is a part of artificial intelligence.
 It uses data and math models to let computers learn tasks without hard-coded rules. Systems spot patterns and improve from experience.

I) Deep Learning
Ans => Deep learning is a subset of machine learning that uses multi-layered artificial neural networks to mimic the human brain. 
It allows computers to autonomously process complex, unstructured data—like images, sound, and text—and learn patterns without explicit 
human programming


Q2: What is supervised learning? List some examples of supervised learning.
Ans => Supervised learning is a type of machine learning where an algorithm is trained using labeled data. 
This means each input data point comes with a known correct output or label. The system learns patterns from these examples 
to predict outcomes for new, unseen data.
Example = Span detection,House pricing prediction, image recognition, Medical diagnosis

Q3:  What is unsupervised learning? List some examples of unsupervised learning.
Ans => Unsupervised learning is a type of machine learning where an algorithm analyzes and finds patterns in unlabeled data without human guidance. 
Instead of using pre-existing answers or labels, the model looks at raw information to group similar data points, discover hidden structures, 
or build rules on its own.
Examples =>  E-Commerce Customer Segmentation

Q4: What is the difference between AI, ML, DL, and DS?
Ans => Artificial Intelligence (AI), Machine Learning (ML), Deep Learning (DL), and Data Science (DS) are connected tech fields. 
AI is the broad goal of making smart machines. ML is a way to train systems using data. DL uses deep neural networks for complex tasks.
DS combines math and stats to find insights from data

Q5: What are the main differences between supervised, unsupervised, and semi-supervised learning?
Ans => The main differences lie in the type of data they use: supervised learning uses fully labeled data, unsupervised learning uses 
completely unlabeled data, and semi-supervised learning uses a small amount of labeled data combined with a large amount of unlabeled data.

Q6: What is train, test and validation split? Explain the importance of each term.
Ans => 
Training Set
Definition: The largest portion of the dataset used directly by the algorithm to learn weights, parameters, and hidden patterns.
Importance: Without this data, the model has nothing to learn from. It forms the foundation of the machine learning process.
Validation Set
Definition: A separate subset used during the training phase to evaluate the model's progress and tune hyperparameters (like learning rate or depth).
Importance: It prevents overfitting to the training data. It acts as an unbiased judge to help select the best model version before final testing.
Test Set
Definition: A completely untouched subset held back until the very end of the entire training and tuning process.
Importance: It provides a realistic, unbiased estimate of how well the model will perform on brand new, real-world data it has never seen before.


Q7: How can unsupervised learning be used in anomaly detection?
Unsupervised learning detects anomalies by analyzing unlabeled datasets to discover underlying patterns and establishing 
a baseline for "normal" behavior. Instead of relying on predefined training examples of fraud, errors, or system failures, 
these models flag data points that significantly deviate from the established norm, operating under the core assumption that 
anomalies are rare and inherently different from standard data.
                        Unsupervised Anomaly Detection
                                    │
    ┌──────────────────────┬────────┴─────────────┬──────────────────────┐
    ▼                      ▼                      ▼                      ▼
Isolation-Based     Density-Based          Cluster-Based          Reconstruction-Based
(e.g., Isolation    (e.g., DBSCAN,         (e.g., K-Means)        (e.g., Autoencoders,
 Forest)             LOF)                                          PCA)


Q8: List down some commonly used supervised learning algorithms and unsupervised learning
algorithms.
Supervised learning algorithms 
Logistic Regression: Calculates the chance of an event happening to sort data into categories (yes or no).
Decision Tree: Splits data into branches using true-or-false rules to make a final choice or guess.
Random Forest: Combines many small decision trees to make more accurate and stable predictions.
Support Vector Machine: Draws a clear boundary line to separate different groups of data cleanly.


Unsupervised Learning Algorithms
K-Means Clustering: Groups data items into a set number of distinct piles based on how close they are.
Principal Component Analysis: Reduces the size of complex data sets while keeping the most important information.
Hierarchical Clustering: Builds a tree-like diagram of nested groups to show how data pieces relate.
DBSCAN: Finds dense clusters of data points and marks scattered points as noise or outliers.
Apriori Algorithm: Discovers useful if-then association rules and patterns hidden inside large transaction datasets.

'''