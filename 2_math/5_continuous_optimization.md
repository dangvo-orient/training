# Gradient Descent

## gradient

the gradient of a function is a vector of all its partial derivatives

it tells:
- **direction** of steepest increase (where the function grows the fastest)
- **magnitude** (length of the vector) tells you how steep that slope is

example: standing on a hill -> the gradient is the arrow pointing straight uphill from the current position

## descent

to descent means to go downward. in optimization, it means moving in the opposite direction of gradient

since the gradient points towards the steepest increase, we want the steepest decrease (to minimize cost) -> move against the gradient

## definition

an optimization algorithm used to find minimum (or maximum) of a function by iteratively moving toward the opposite direction of the gradient of the function at the current point

## steps

1. initialize parameters: start a some initial point $\theta_0$ (random or based on heuristics)
2. compute the gradient: calculate the gradient (slope) $\nabla f(\theta)$ of the cost function at the current position
3. move a small step in the opposite direction of the gradient:
$$\theta_{new} = \theta_{old} - \alpha \nabla f(\theta_{old})$$
4. repeat until convergence

## variants

n: the number of samples

- batch GD (B=n): use the entire dataset to compute each gradient update
    - accurate but slow for large datasets
- stochastic gradient descent (B=1): use one random sample per update
    - fast but noise -> helps escape local minima
- mini-batch gradient descent (B=m < n): use a small batch of samples per update
    - good trade-off between speed and stability
- others: Momentum, NAG, AdaGrad, RMSProp, Adam, etc