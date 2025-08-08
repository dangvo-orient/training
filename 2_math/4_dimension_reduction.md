dimension reduction: a process that simplifies complex dataset by combining similar or correlated features, helping in improving analysis and computational efficiency

# Principal Component Analysis (PCA)

- used to reduce the number of features in a dataset while keeping the most important information
- change original features into new features, which don't overlap with each other and the first few keep most of the important differences found in the original data

## steps

1. standardize the data

make each feature have a mean of 0 (and a standard deviation of 1 if features are in different scale)

2. compute the covariance matrix

to see how features relate to each other whether they increase or decrease together

$X$ is the mean-centered data ($n \times p$), the covariance matrix ($p \times p$) is
$$
Cov = \frac{1}{n-1} X^T X
$$

3. find the principal components

PCS identifies new axes where the data spreads out the most

- solve the characteristic equation to get eigenvalues: $det(Cov-\lambda I) = 0$
- find eigenvectors: each is a principal component direction
- interpret:
    - eigenvalues -> how much variance each principal component captures ($\lambda_1 \ge \lambda_2 \ge ... \ge \lambda_p$)
    - eigenvectors -> the direction in the original feature space that corresponds to each principle component

examples:
| PC  | Eigenvalue | Variance explained (%) | Eigenvector (direction in F1–F4 space) |
| --- | ---------- | ---------------------- | -------------------------------------- |
| PC1 | 4.5        | 72.6%                  | \[0.70, 0.50, 0.35, 0.50]              |
| PC2 | 1.5        | 24.2%                  | \[-0.35, 0.75, -0.45, 0.30]            |
| PC3 | 0.2        | 3.2%                   | \[0.50, -0.30, -0.75, 0.20]            |

4. project onto the subspace spanned by the top k eigenvectors

select the top k components that capture most of the variance then project the original data onto these top components

in above example: choose k=2 -> variance: 96.8%

# T-distributed Stochastic Neighbor Embedding (TNSE)

non-linear method that maps high-dimensional points to 2D or 3D so local structure (neighbors) is preserved: points that are similar in high-D end up near each other in the low-D map

mainly used for visualization (exploring clusters / structure), not for downstream modeling

## steps

1. for each high-D data point, t-SNE measures how similar other points are to it - basically building a sense of each point's local neighborhood

- `perplexity` parameter: controls whether that neighborhood is tiny (very local) or broader

2. turn those neighborhood judgements into a two-way score, t-SNE combines the two points' view so a pair's similarity reflects how much they mutually consider each other neighbors

3. create a low-D space that can stretch farther apart: t-SNE uses rules that allow dissimilar points to sit very far from each other

4. compare the two neighborhoods and move points to reduce mismatch

t-SNE repeatedly checks how well the low-D matches the high-D neighborhood structure. if 2 points were neighbors in high-D but are far apart in low-D, it pulls them closer, and vice versa -> iterative process

# Neighbor Component Analysis (NCA)

supervised metric-learning method that learns a linear projection of the data so that a simple nearest-neighbor classifier works better

it warps space so points from the same class end up close together and different classes are pushed apart, maximize the chance that each point is correctly classified by its neighbors

# Lenstra-Lenstra-Lovasz (LLL)
