import random
from min_heap import FitnessMinHeap
from chromosome import OrganismChromosome
from evolution import evaluate_cost_function, execute_crossover

if __name__ == "__main__":
    print("🧬 Activating GeneticHeap-Optimizer Environment Pipeline...\n")

    heap_container = FitnessMinHeap()
    
    # Initialize a random tracking pool
    for _ in range(10):
        individual = OrganismChromosome(random.uniform(-10.0, 10.0))
        evaluate_cost_function(individual)
        heap_container.push_candidate(individual)

    # Breed a new generation from top performers
    best_p1 = heap_container.extract_fittest()
    best_p2 = heap_container.extract_fittest()

    offspring = execute_crossover(best_p1, best_p2)
    evaluate_cost_function(offspring)

    print(f"📥 Parent A Generation Vector: x = {best_p1.x:.4f} | Cost Score = {best_p1.fitness_score:.4f}")
    print(f"📥 Parent B Generation Vector: x = {best_p2.x:.4f} | Cost Score = {best_p2.fitness_score:.4f}")
    print(f"🔮 Bred Offspring Optimized Evolution Target Coordinate Result: x = {offspring.x:.4f}")
