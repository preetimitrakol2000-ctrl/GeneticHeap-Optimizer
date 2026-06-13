class OrganismChromosome:
    def __init__(self, gene_value):
        self.x = gene_value
        self.fitness_score = 0.0 # Evaluated function cost value: f(x)
