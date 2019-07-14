# decide-raw
Generating decision-making algorithms by evolutionary / genetic algorithm
for a one-dimensional random walk problem

# The problem

Given a series of integer values.
The first value is designated as the original value.
The values are taken sequentially until the one that is decided to be chosen.
The decision should be done using the last `N` taken values.
The goal is to choose the greater value that is also greater than the original one.

To solve the problem, complex algorithms (composite decider) built from special linear classifiers (linear decider)
are evolved by [evolutionary algorithm](https://en.wikipedia.org/wiki/Evolutionary_algorithm).

## Linear decider

The building block of the evolved decision-making algorithm (decider) is
making decision when the linear combination of the input values is greater than zero.

The input values are the last `N` values of the actual series and the original value.

The coefficients are restricted to the integer numbers
([integer programming](https://en.wikipedia.org/wiki/Integer_programming)).
The set of integer coefficients is isomorphic with the set of rational ones,
so with using integers the same precision can be achieved.

The linear decider is a [perceptron](https://en.wikipedia.org/wiki/Perceptron),
a [linear classifier](https://en.wikipedia.org/wiki/Linear_classifier).

## Composite decider

The Linear decider can be considered as a
[literal](https://en.wikipedia.org/wiki/Literal_(mathematical_logic)) of mathematical logic:
its negation is a linear decider with the negated coefficients.

Algorithms having two possible result can be expressed in logical formula.
Every formula of the [zeroth-order or propositional logic](https://en.wikipedia.org/wiki/Propositional_calculus)
can be converted into a logically equivalent formula that is in
[conjunctive normal form](https://en.wikipedia.org/wiki/Conjunctive_normal_form) (CNF):
[conjunction](https://en.wikipedia.org/wiki/Logical_conjunction)
of [disjunction](https://en.wikipedia.org/wiki/Logical_disjunction) of literals.

Hence, having the inspiration,
the composite decider is defined as the conjunction of disjunction of linear deciders, e.g.:
```python
(lin_decider_1 or lin_decider_2) and (lin_decider_3 or lin_decider_4) and (lin_decider_5 or lin_decider_6)
```

Any [functional complete](https://en.wikipedia.org/wiki/Functional_completeness#Minimal_functionally_complete_operator_sets)
set of boolean operators could be used to express any formula of the propositional logic,
but the CNF is flat enough and easily extendable in a genetic algorithm.

In [computational complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory)
finding a satisfying assignment to a formula expressed in CNF
in which each disjunction contains at most `k` > 2 literals
([k-SAT or 3-SAT](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem)) is
[NP-complete](https://en.wikipedia.org/wiki/NP-completeness) and
[2-SAT](https://en.wikipedia.org/wiki/2-satisfiability) can be solved
in [polynomial time](https://en.wikipedia.org/wiki/Time_complexity#Polynomial_time).

Another possibility is to define the composite decider based on the
[disjunctive normal form](https://en.wikipedia.org/wiki/Disjunctive_normal_form) (DNF).

# The evolutionary algorithm

The applied evolutionary algorithm is a variant of
[evolutionary programming](https://en.wikipedia.org/wiki/Evolutionary_programming)

The input population size is kept constant by selecting always the same number of entities
with the highest [fitness](https://en.wikipedia.org/wiki/Fitness_function).

In the simplest case, the reproduction is [asexual](https://en.wikipedia.org/wiki/Asexual_reproduction)
and every entity breeds a single offspring.

The set of genetic operators consists of the following
[mutations](https://en.wikipedia.org/wiki/Mutation_(genetic_algorithm)):
- increase / decrease a coefficient of a linear decider;
- add / remove a linear decider to / from a disjunction;
- add / remove a disjunction of linear deciders to / from the conjunction;

## Factors keeping back evolution of high fitness

### [Inbreeding](https://en.wikipedia.org/wiki/Inbreeding)

The size of the population is limited by the computational power.
Genetic recombination decreases the difference between the entities
that may lead to lower variability in a smaller population.
Either lower variability or small population results similar effect as weak mutation.

### Strong mutation

Majority of mutations yield significant drop of fitness.
The bigger the mutation the lower the fitness becomes.
Frequent and / or big mutations increase the chance of degeneration to
the average of all possible fitness values, which is usually very low.

### Weak mutation

Rare and / or little mutations result slow convergence to the optimal fitness
and the process may stick or be attracted into a local optimum of the
[fitness landscape](https://en.wikipedia.org/wiki/Fitness_landscape).
