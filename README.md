# GeneticHeap-Optimizer

A dependency-free Genetic Algorithm (GA) framework built in Python to minimize non-linear equations. This project avoids sorting entire populations every generation ($O(N \log N)$), using a custom **Min-Heap Priority Queue** to track candidate fitness values instead.

## ⚡ Data Structure Complexities
* **Candidate Extraction (Best Fitness):** $O(1)$ read boundary access.
* **Population Purging/Insertion Phase:** $O(\log N)$ structural shifts.
