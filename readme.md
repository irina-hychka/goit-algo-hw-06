# Task 2 – Pathfinding in E-Scooter Sharing Graph using DFS and BFS

## Description

This task implements Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms to find paths in a real-world model of an e-scooter sharing network in Zolotonosha, developed in Task 1.

## Implementation Details

* **DFS (Depth-First Search)**:
  * Explores paths deeply before backtracking.
  * May return longer or suboptimal paths.

* **BFS (Breadth-First Search)**:
  * Explores all neighboring nodes first (level-by-level).
  * Guarantees the shortest path in terms of steps.

## Results
For the path from **Central Square** to **Stadium**:

* DFS path: 'Central Square → Railway Station → Machinery Plant District → Stadium'
* BFS path: 'Central Square → Stadium'

> BFS found the optimal path directly, while DFS explored a longer one due to depth-first strategy.

## Conclusion

DFS and BFS provide different traversal strategies:
- **DFS** is suitable when full exploration is needed.
- **BFS** is ideal for finding shortest paths in unweighted graphs.

This comparison illustrates the practical difference in real-world navigation scenarios.
