class FitnessMinHeap:
    """Maintains chromosome references structured for minimum cost access."""
    def __init__(self):
        self.heap_pool = []

    def push_candidate(self, organism):
        self.heap_pool.append(organism)
        self._shift_up(len(self.heap_pool) - 1)

    def extract_fittest(self):
        if not self.heap_pool: return None
        if len(self.heap_pool) == 1: return self.heap_pool.pop()
        
        fittest = self.heap_pool[0]
        self.heap_pool[0] = self.heap_pool.pop()
        self._shift_down(0)
        return fittest

    def _shift_up(self, idx):
        while idx > 0 and self.heap_pool[idx].fitness_score < self.heap_pool[(idx - 1) // 2].fitness_score:
            self.heap_pool[idx], self.heap_pool[(idx - 1) // 2] = self.heap_pool[(idx - 1) // 2], self.heap_pool[idx]
            idx = (idx - 1) // 2

    def _shift_down(self, idx):
        length = len(self.heap_pool)
        while 2 * idx + 1 < length:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = left
            if right < length and self.heap_pool[right].fitness_score < self.heap_pool[left].fitness_score:
                smallest = right
            if self.heap_pool[idx].fitness_score <= self.heap_pool[smallest].fitness_score:
                break
            self.heap_pool[idx], self.heap_pool[smallest] = self.heap_pool[smallest], self.heap_pool[idx]
            idx = smallest
