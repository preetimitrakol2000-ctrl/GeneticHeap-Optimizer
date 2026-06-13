import random
from chromosome import OrganismChromosome

def evaluate_cost_function(chromosome):
    """Mathematical Objective Target: The Sphere Function f(x) = x^2 (Global Minima at x=0)."""
    chromosome.fitness_score = chromosome.x ** 2

def execute_crossover(parent_a, parent_b):
    midpoint_gene = (parent_a.x + parent_b.x) / 2.0
    # Inject a small mutation mutation variance parameter
    mutation_delta = random.uniform(-0.1, 0.1) if random.random() > 0.7 else 0.0
    return OrganismChromosome(midpoint_gene + mutation_delta)
