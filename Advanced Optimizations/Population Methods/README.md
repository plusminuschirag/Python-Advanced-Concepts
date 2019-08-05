# Population Methods:

- Population-based methods keep around a sample of
candidate solutions rather than a single candidate solution. 
- Each of the solutions is involved in
tweaking and quality assessment, but what prevents this from being just a parallel hill-climber __is
that candidate solutions affect how other candidates will hill-climb in the quality function.__ This
could happen either by good solutions causing poor solutions to be rejected and new ones created,
or by causing them to be Tweaked in the direction of the better solutions.


__Common Terms Used in Evolutionary Computation:__

| Term | Meaning |
| --- | --- |
individual|a candidate solution
child and parent|a child is the Tweaked copy of a candidate solution (its parent)
population|set of candidate solutions
fitness|quality
fitness landscape|quality function
fitness assessment or evaluation|computing the fitness of an individual
selection|picking individuals based on their fitness
mutation|plain Tweaking. This is often thought as “asexual” breeding.
recombination or crossover|a special Tweak which takes two parents, swaps sections of them, and (usually) produces two children. This is often thought as “sexual” breeding.
breeding|producing one or more children from a population of parents
genotype or genome |through an iterated process of selection and Tweaking (typically mutation or recombination) an individual’s data structure, as used during breeding
chromosome |a genotype in the form of a fixed-length vector
gene |a particular slot position in a chromosome
allele | a particular setting of a gene
phenotype|how the individual operates during fitness assessment
generation | one cycle of fitness assessment, breeding, and population re-assembly; or the population produced each such cycle














