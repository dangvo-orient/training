# types of norm

a norm is a function that takes any vector and returns a non-negative number representing its magnitude

must satisfy 3 properties
- $||\vec{v}|| \ge 0$ (always non-negative) 
- |$|c \vec{v}|| = |c| . ||\vec{v}||$ (scaling)
- triangle equality: $||\vec{u} + \vec{v}|| \le ||\vec{u}|| + ||\vec{v}||$

some common norms:
- L2 norm (euclidean norm): $||\vec{v}||_2 = \sqrt{x^2_1 + x^2_2 + ... + x^2_n}$
- L1 norm (manhattan norm): $||\vec{v}||_1 = |v_1| + |v_2| + ... + |v_n|$
- L∞ norm (max norm): $||\vec{v}||_{\infty} = \max(|v_1|, |v_2|,..., |v_n|)$

# orthogonal

two vectors are orthogonal if their dot product is zero
- orthogonal vectors are independent and form a good basis
- used in projections, decompositions, and simplifying transformations

# distance

vector distance is a way of defining how far apart 2 vectors are in space, it's typically computed using the norm of their difference