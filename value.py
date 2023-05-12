
import time
from pymaze import maze, agent, COLOR, textLabel
import numpy as np
import tracemalloc

# Value Iteration function to find values for all nodes
def calc_val(Prob, Rew, gamma, covergence_threshold):
    values = {stage: 0 for stage in Prob}
    while True:
        d = 0
        for m in Prob:
            v = values[m]
            max_q = -np.inf
            for x in Prob[m]:
                r = Rew[m][x] + gamma * values[Prob[m][x]]
                if r > max_q:
                    max_q = r
            values[m] = max_q
            d = max(d, abs(v - values[m]))
        if d < covergence_threshold:
            break
    return values


def run_value_iteration_algo(maze, gamma, covergence_threshold):


    #Starting memory tracking
    tracemalloc.start()

    #Defining the states and transitive function
    directions = ['N', 'S', 'E', 'W']
    probability = {}
    rewards = {}
    for p in range(1, maze.rows+1):
        for q in range(1, maze.cols+1):
            node = (p, q)
            probability[node] = {}
            rewards[node] = {}
            for x in directions:
                if x == 'N':
                    new_stage = (p-1, q)
                elif x == 'S':
                    new_stage = (p+1, q)
                elif x == 'E':
                    new_stage = (p, q+1)
                elif x == 'W':
                    new_stage = (p, q-1)

                if maze.maze_map[node][x] == 1:
                    probability[node][x] = new_stage
                    rewards[node][x] = -1
                else:
                    probability[node][x] = node
                    rewards[node][x] = -100
            if node == (1, 1):
                rewards[node]['E'] = 100


    # Find the optimal policy based on the values
    start_time = time.time()
    V = calc_val(probability, rewards, gamma, covergence_threshold)
    end_time = time.time()
    actual_time = end_time - start_time
    print('Execution time:', actual_time*1000, 'ms')
    policy_it = {}
    for m in probability:
        max_q = -np.inf
        for x in probability[m]:
            r = rewards[m][x] + V[probability[m][x]]
            if r > max_q:
                max_q = r
                policy_it[m] = x

    # Print the path and trace it in the maze
    path = [(maze.rows, maze.cols)]
    current_node = (maze.rows, maze.cols)
    while current_node != (1, 1):
        action = policy_it[current_node]
        if action == 'N':
            new_stage = (current_node[0]-1, current_node[1])
        elif action == 'S':
            new_stage = (current_node[0]+1, current_node[1])
        elif action == 'E':
            new_stage = (current_node[0], current_node[1]+1)
        elif action == 'W':
            new_stage = (current_node[0], current_node[1]-1)
        path.append(new_stage)
        current_node = new_stage

    current, peak = tracemalloc.get_traced_memory()
    print(f"Memory Used is : {peak*0.000001} MB")
    #Ending memory tracking
    tracemalloc.stop()

    print(path)
    x = agent(maze, footprints=True, color=COLOR.red)
    maze.tracePath({x: path})
    l = textLabel(maze, "MDP Value Iteration - No of nodes in shortest path found : ", len(path))

