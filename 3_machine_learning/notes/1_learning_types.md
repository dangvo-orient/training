# type of learning

## by the type of supervision (feedback)

1. supervised learning

- the model is trained on **labeled** data (input -> known output)
- the goal is to learn a mapping from inputs to outputs

2. unsupervised learning

- the model works on **unlabeled** data, finding hidden structures or patterns

3. semi-supervised learning

- use a small amount of labeled data + large amount of unlabeled data

4. self-supervised learning

- labels are generated automatically from data itself

5. reinforcement learning (RL)

- an agent learns by interacting with an environment and receiving rewards or penalties based on its action

## by learning style

- offline (batch) learning: train models on a whole fixed dataset at once, then deploy
- online learning: model updates continuously as new data arrives-
    - train model incrementally as new data becomes available
    - the model updates its parameters continuously or at intervals, adapting to changes in data patterns over time
- active learning: the model actively queries for the most informative data points to label

## by the learning objective

- classification: assign an input to one of several categories
- regression: predict a continuous value
- clustering: group similar data points without labels
- dimensional reduction: reduce features while preserving information
- generative model: learn the underlying distribution to generate new samples

# ranking

ranking refers to learning a model that sorts items (documents, products, etc) by their relevance, importance to a query or user preference

## how
- ranking models rely on a scoring function that predicts a relevance score for each item based on input features. the items are then sorted by these scores. 
- the inputs include a query and associated documents, and the output is a ranked list of documents

## ranking approaches

ranking problems -> classified based on how the model learns from training data

1. pointwise
   
- treat ranking as a regression problem, predicting the relevance score of each item independently
- the loss function measures the difference between the predicted and true relevance scores, requiring absolute relevance label (not always available)

2. pairwise

- focus on relative preferences between pairs of documents
- learn by comparing pairs of items and predicting which one should rank higher, transforming the task into a binary classification problem

3. listwise

- learn from the entire ranked list at once, optimizing a ranking metric directly

# recommender system

a type of ML system designed to provide personalized suggestions to users by predicting their preferences for items (movies, products, etc)

goal: help users discover items they are most likely to engage with, buy, or enjoy - without manually searching

## types of recommender systems

1. content-based filtering

- recommend items relying on the features of items and user preferences
- works well in cold-start scenarios where new items or users are introduced, requiring detailed metadata

2. collaborative filtering

- predicts user preferences based on the behavior of other users
    - user-based: finds users with similar preferences and recommends items they liked
    - item-based: identifies items similar to those the user has interacted with and recommends them
- effective but requires sufficient interaction data to perform well

3. hybrid systems

- combine multiple methods (e.g content + collaborative) to leverage the strengths of each

## challenges

- cold start: new users or new items lack data
- data sparsity: most users interact with only a tiny fraction of items
- scalability: large datasets require efficient computation
- diversity & accuracy: balancing novel recommendation with ones the user is likely to pick
