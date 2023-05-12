
import time
from pymaze import maze, agent, COLOR, textLabel
import numpy as np
import tracemalloc

# Policy Iteration function to evaluate and update policy on every iteration
def pol_ite(Prob, Rew, states, gamma, covergence_threshold):
    values = {stage: 0 for stage in Prob}
    policy = {stage: states[0] for stage in Prob}
    while True:
        # Process of policy evaluation 
        while True:
            d = 0
            for y in Prob:
                v = values[y]
                z = policy[y]
                values[y] = sum([Prob[y][z][new_stage] * (Rew[y][z] + gamma * values[new_stage]) for new_stage in Prob[y][z]])
                d = max(d, abs(v - values[y]))
            if d < covergence_threshold:
                break
        
        # Process of policy Improvement
        policy_stable = True
        for y in Prob:
            old_stage = policy[y]
            max_q = -np.inf
            for z in Prob[y]:
                x = sum([Prob[y][z][new_stage] * (Rew[y][z] + gamma * values[new_stage]) for new_stage in Prob[y][z]])
                if x > max_q:
                    max_q = x
                    policy[y] = z
            if old_stage != policy[y]:
                policy_stable = False
        if policy_stable:
            break
    
    return policy, values

def run_value_iteration_algo(maze, gamma, covergence_threshold):
    #Starting memory tracking
    tracemalloc.start()

    #Defining the states and transitive function

    directions = ['N', 'S', 'E', 'W']
    probability = {}
    reward = {}
    for p in range(1, maze.rows+1):
        for q in range(1, maze.cols+1):
            node = (p, q)
            probability[node] = {}
            reward[node] = {}
            for z in directions:
                if z == 'N':
                    updated_node = (p-1, q)
                elif z == 'S':
                    updated_node = (p+1, q)
                elif z == 'E':
                    updated_node = (p, q+1)
                elif z == 'W':
                    updated_node = (p, q-1)

                if maze.maze_map[node][z] == 1:
                    probability[node][z] = {updated_node: 1}
                    reward[node][z] = -1
                else:
                    probability[node][z] = {node: 1}
                    reward[node][z] = -100
            if node == (1, 1):
                reward[node]['E'] = 100


    start_time = time.time()
    # Get the optimal policy and values
    policy, V = pol_ite(probability, reward, directions, gamma, covergence_threshold)
    end_time = time.time()
    final_time = end_time - start_time
    print('Execution time:', final_time*1000, 'ms')

    path = [(maze.rows, maze.cols)]
    current_node = (maze.rows, maze.cols)
    while current_node != (1, 1):
        action = policy[current_node]
        if action == 'N':
            updated_node = (current_node[0]-1, current_node[1])
        elif action == 'S':
            updated_node = (current_node[0]+1, current_node[1])
        elif action == 'E':
            updated_node = (current_node[0], current_node[1]+1)
        elif action == 'W':
            updated_node = (current_node[0], current_node[1]-1)
        path.append(updated_node)
        current_node = updated_node

    current, peak = tracemalloc.get_traced_memory()
    print(f"Memory Used is : {peak*0.000001} MB")
    #Ending memory tracking
    tracemalloc.stop()

    # Trace the path in the maze
    z = agent(maze, footprints=True, color=COLOR.blue)
    maze.tracePath({z: path})
    l = textLabel(maze, 'MDP Policy Iteration - No of nodes in shortest path found : ', len(path))