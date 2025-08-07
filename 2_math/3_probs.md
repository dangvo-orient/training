# definitions

probability: a framework for measuring uncertainty and the likelihood of events occurring

statistics: the science of collecting, analyzing, and interpreting data to make informed decision under uncertainty. While probability starts with known rules and predicts outcomes, statistics works backward - starting with observed data to infer the underlying patterns or rules

distribution: a description of how probability is spread across all possible outcomes of a random process (like a complete map showing the likelihood of every possible result)
- discrete distributions -> outcomes are countable and distinct
- continuous distributions -> outcomes can take any value within a range (e.g gaussian distribution)

## connection

- probability theory provides the rules
- statistics gives tools to apply those rules to real data
- distributions offer ready-made model for common types of randomness

example: weather forecasting
- people use statistical methods to analyze historical weather data
- apply probability theory to model atmospheric processes
- use specific distributions to represent uncertainty in their predictions


# probability space

a probability space is a mathematical construct that provides a formal model of a random process or "experiment"

it consists of three elements:
- a sample space ($\Omega$): all possible outcomes of a random process
- an event space ($F$): a set of events, where an event is a subset of outcomes in the sample space
- probability function ($P$): a rule assigning probability to each event, which is a number between 0 and 1

example of throwing a standard die
- $\Omega$ is the set {1,2,3,4,5,6}
- the even space $F$ could be the set of all subsets of the sample space, which could contain:
    - simple events such as {5} (the die lands on 5)
    - complex events such as {2,4,6} (the die lands on an even number)
- probability function $P$ then map each event to the number of outcomes in that event divided by 6 - e.g {5} would be mapped to 1/6, and {2,4,6} would be mapped to 3/6=1/2

when an experiment is conducted, it results in exactly one outcome $\omega$ from the sample space $\Omega$

# sum rule, product rule, bayes' theorem

## sum rule

the sum rule states the probability of "either this OR that" happening

sum rule: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

when $A$ and $B$ are disjoint ($A \cup B = \empty$) -> their intersection is empty -> $P(A \cup B) = P(A) + P(B)$

## product rule

the product rule states the probability of multiple events occurring together

product rule: $P(A \cap B) = P(B) \cdot P(A|B) = P(A) \cdot P(B|A)$

- independent events: e.g the probability of flipping heads twice in a row is 1/2 x 1/2 = 1/4 because each coin flip doesn't affect the other
- dependent events: $A$ and $B$ are dependent -> $P(B|A) = P(B)$ -> $P(A \cap B) = P(A) \cdot P(B)$
    - e.g drawing two cards without replacement -> the probability of getting two aces is P(first ace) x P(second ace | first was ace) = 4/52 x 3/51

    - "the probability of both A and B equals the probability of A times the probability of B given that A has occurred"

## bayes' theorem

it shows how to update beliefs when new evidence arrives -> answer the question "given that I observed this evidence, what's the probability of that hypothesis?"

formula:
$$P(H|E) = \frac{P(E|H) \times P(H)}{P(E)}$$

intuitive meanings:
- $P(H)$: prior belief about the hypothesis before seeing the evidence
- $P(E|H)$: the likelihood - how probable the evidence would be if the hypothesis were true
- $P(E)$: the total probability of observing the evidence
- $P(H|E)$: the posterior - updated belief after seeing the evidence

example: medical diagnosis
- suppose a test for a rare disease is 95% accurate. the disease affects 1 in 100 people. if so tests positive -> the probability they actually have the disease?

answer:
- know the disease -> 95% accuracy -> $P(positive|disease) = 0.95$
- 1 over 100 people can be affected -> $P(disease) = 0.01$
-

$$
\begin{aligned}
    & P(positive) \\
    &= P(positive \cap disease) + P(positive \cap no\_disease) \\
    &= P(positive|disease) \times P(disease) + P(positive|no\_disease) \times P(no\_disease) \\
    &= 0.95 \times 0.01 + 0.05 \times 0.99 \\
    &= 0.059
\end{aligned}
$$

- $P(disease|positive) = (0.95 \times 0.01) / 0.059 = 16.1\%$