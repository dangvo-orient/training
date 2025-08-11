# classification / regression

- type: supervised

## classification

classification categorizes data into predefined groups based on shared characteristics. ML models learn the characteristics of each group from the input data and then generalize this information to new data points

examples: classify email types, determine the type of tumor from a medical scan, categorize customer feedback

metrics: accuracy / F1 / ROC-AUC

## regression

used to predict a continuous outcome value using the value of input variables, analyzing the input data to understand the relationship between variables

examples: predict a student's future exam score, may use study time, sleep hours, and previous grade averages as input variables

metrics: MSE / RMSE / MAE

# Support Vector Machine (SVM)

- type: supervised (classification & regression via SVR)
- goal: find a decision boundary (hyperplane) that maximizes the margin between classes, can use kernels to handle nonlinearity

concepts:
- hyperplane: SVM aims to find the optimal hyperplane that separates data points of different classes (e.g in a 2D, this is a line)
- margin: is the distance between the hyperplane and the nearest data points from each classes (called support vectors) -> SVM maximizes this margin to ensure better generalization
- support vectors: the data points closest to the hyperplane -> critical in defining the position and orientation of the hyperplane
- kernel: SVM uses kernel functions to transform data into higher dimensions where it becomes easier to separate classes (e.g linear, polynomial, redial basis function (RBF), sigmoid)

advantages:
- work well for both linear and non-linear data
- effective in high-dimensional spaces
- robust to overfitting, especially in cases with a clear margin of separation

# Decision Tree

- type: supervised (classification & regression)
- goal: tree of decision nodes that split features to make predictions (if-then style)
- interpretable models, when feature importance and rules are valuable

## how

- models work by splitting data into subsets based on features -> decision making
- each leaf node provides a prediction and the splits create a tree-like structure

## types of Decision Tree

- ID3: uses **information gain** to split data and works well for classification but prone to overfitting and struggles with continuous data
- C4.5: advance version of ID3 with **gain ratio** for both discrete and continuous data but struggle with noisy data
- CART: minimizes **gini impurity** for classification and **MSE** for regression with pruning technique to prevent overfitting
- CHAID: uses chi-square tests for splitting and is effective for large categorical datasets but not for continuous data
- MARS: extended version of CART using **piecewise linear functions** to model non-linear relationships but computationally expensive
- Conditional Inference Trees: uses statistical hypothesis testing for unbiased splits and handles various data types but it is slower than others

# Ensemble Learning

- involves training multiple base models (called *learners* or *weak learners*) and then combining their predictions to produce a final output
- core idea: a group of diverse models working together can outperform any single model by compensating for each other's errors

common ensemble techniques:
- bagging (e.g Random Forest): builds multiple models on different random subsets of data sampled with replacement
- boosting (e.g AdaBoost, Gradient Boosting, XGBoost, LightGBM): sequentially train models where each new model focuses on correcting previous model's errors
- Stacking: combines multiple diverse models and uses another model, called a meta-learner, to learn how to best combine their predictions

pros/cons:
- improved accuracy, robustness, flexibility, handlers feature interactions
- less interpretable, more compute

# Unsupervised Techniques

- goal: learn hidden structures and underlying patterns from unlabeled data - no `y` provided
- used to discover groups, compress features, visualize high-dim data, detect outliers, etc

common methods:
- clustering: k-means, DBSCAN, hierarchical clustering
- dimensional reduction: PCA, t-SNE
- density / novelty detection: gaussian mixture models, isolation forest, one-class SVM
