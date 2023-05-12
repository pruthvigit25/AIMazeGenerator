# Maze Generator and Pathfinding Algorithms

This repository contains an implementation of a maze generator and various pathfinding algorithms in Python. The maze generator creates a maze and the pathfinding algorithms (DFS, BFS, and A*) are used to find a path from the start cell to the end cell in the maze. Additionally, the repository includes implementations of MDP value iteration and policy iteration for decision-making problems.

## Algorithms

### Depth First Search (DFS)

DFS is a graph traversal algorithm that explores as far as possible down each branch before backtracking. It follows the LIFO (Last In First Out) approach and is often used to create mazes, sort topologies, and solve puzzles. While DFS does not always find the shortest path, it can be quicker than BFS.

### Breadth First Search (BFS)

BFS is another graph traversal algorithm that explores all the nodes at the current level before moving to the next level. It follows the FIFO (First In First Out) approach and is known for finding the shortest path from the start node to any other reachable node. BFS is commonly used in maze solving and puzzle games.

### A* Search Algorithm

A* is an informed search algorithm that combines the benefits of DFS and BFS. It uses a heuristic function (such as the Manhattan distance) to estimate the distance between the current and goal nodes, guiding the search towards the goal. A* is known for finding the shortest path in a graph or grid.

### Markov Decision Process (MDP)

MDP is a framework for decision-making in situations with random outcomes. The repository includes implementations of MDP value iteration and policy iteration algorithms. Value iteration calculates the expected utility starting from a given state and following an optimal policy, while policy iteration alternates between policy evaluation and policy improvement steps to determine the optimal policy.

## Repository Structure

The repository contains the following files:

- `pymaze.py`: Python script for generating mazes.
- `astar.py`, BFS.py, DFS.py, : Python script implementing the DFS, BFS, and A* algorithms.
- `value.py`: Python script implementing MDP value iteration.
- `policy.py`: Python script implementing MDP policy iteration.
- `run_maze.py': Python script to run all the algorithms.

Make sure you have Python 3 installed on your system.



