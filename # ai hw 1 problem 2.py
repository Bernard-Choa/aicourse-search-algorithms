# ai hw 1 problem 2
from numpy.random import randint
from numpy.random import rand
from numpy.random import choice
from numpy import inf
import random

graph = {
    'a': {'b':12,'c':10,'g':12},
    'b': {'a':12,'c':8,'d':12},
    'c': {'a':10,'b':8,'d':11,'e':3,'g':9},
    'd': {'b':12,'c':11,'e':11,'f':10},
    'e': {'c':3,'d':11,'f':6,'g':7},
    'f': {'d':10,'e':6,'g':9},
    'g': {'a':12,'c':9,'e':7,'f':9}
}

# Conditions:
# - 1. beginning and end node is always 'a' (Always begin from starting node and return to starting node)
# - 2. exactly 8 nodes (So that the path visits every node once and returns to the start)
# - 3. letters besides 'a' must not appear more than once (Nodes must only be visited once)
# - 4. nodes must have valid edge
 
# fitness/objective function
def pathWeights(path):
 nodesWithoutA = ['b','c','d','e','f','g']
 edges = []

 # beginning and end node is always 'a'
 if path[0] != 'a' or path[-1] != 'a':
  return inf

 # letters besides 'a' must not appear more than once
 for n in nodesWithoutA:
  if path.count(n) > 1:
   return inf
  else:
    continue
 if path.count('a') > 2:
  return inf

 # nodes must have a valid edge
 try:
  for i in range(len(path)-1):
    sN = path[i]
    dN = path[i+1]
    edge = graph[sN][dN]
    edges.append(edge)
  return sum(edges)
 except KeyError:
  return inf
 
# tournament selection
def selection(pop, scores, k=3):
	# first random selection
	selection_ix = randint(len(pop))
	for ix in randint(0, len(pop), k-1):
		# check if better (e.g. perform a tournament)
		if scores[ix] < scores[selection_ix]:
			selection_ix = ix
	return pop[selection_ix]

# crossover two parents to create two children
def crossover(p1, p2, r_cross):
	# children are copies of parents by default
	c1, c2 = p1.copy(), p2.copy()
	# check for recombination
	if rand() < r_cross:
		# select crossover point that is not on the end of the string
		pt = randint(1, len(p1)-2)
		# perform crossover
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]

# mutation operator
def mutation(bitstring, r_mut):
	nodes = ['a','b','c','d','e','f','g']
	for i in range(len(bitstring)):
		# check for a mutation
		if rand() < r_mut:
			# flip the bit
			bitstring[i] = random.choice(nodes)

# genetic algorithm
def genetic_algorithm(objective, chromosomes, n_bits, n_iter, n_pop, r_cross, r_mut):
  nodesWithoutA = ['b','c','d','e','f','g']
  pop = []
  # generates a population of individuals with random chromosomes
  # which satisfies conditions 1 and 3
  for _ in range(n_pop):
    individual = []
    random.shuffle(nodesWithoutA)
    individual = ['a'] + nodesWithoutA + ['a']
    pop.append(individual)
    # keep track of best solution
  best, best_eval = 0, objective(pop[-1])
	# enumerate generations
  for gen in range(n_iter):
		# evaluate all candidates in the population
    scores = [objective(c) for c in pop]
		# check for new best solution
    for i in range(n_pop):
      if scores[i] < best_eval:
        best, best_eval = pop[i], scores[i]
        print(">%d, new best f(%s) = %.3f" % (gen, pop[i], scores[i]))
		# select parents
    selected = [selection(pop, scores) for _ in range(n_pop)]
		# create the next generation
    children = list()
    for i in range(0, n_pop, 2):
			# get selected parents in pairs
      p1, p2 = selected[i], selected[i+1]
			# crossover and mutation
      for c in crossover(p1, p2, r_cross):
				# mutation
        mutation(c, r_mut)
				# store for next generation
        children.append(c)
		# replace population
    pop = children
		# print(pop)
  return [best, best_eval]

# define the total iterations
n_iter = 200
# bits
n_bits = 8
# define the population size
n_pop = 100
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 1.0 / float(n_bits)
# all the nodes in the graph
nodes = ['a','b','c','d','e','f','g']
# perform the genetic algorithm search
best, score = genetic_algorithm(pathWeights, nodes, n_bits, n_iter, n_pop, r_cross, r_mut)
print('Done!')
print('f(%s) = %f' % (best, score))