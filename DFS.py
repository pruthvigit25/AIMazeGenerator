
from pymaze import maze, agent, textLabel, COLOR

def run_dfs_algo(m, start=None):


    if start is None:
        start = (m.rows, m.cols)
    dfs_route = {}
    explored = [start]
    frontier = [start]
    d_all_paths=[]
    num_iterations = 0 # initialize iteration counter
    while len(frontier) > 0:
        num_iterations += 1 # increment iteration counter
        present_cell = frontier.pop()
        # dSeacrh.append(present_cell)
        if present_cell == m._goal:
            break
        pos = 0
        for p in 'ESNW':
            if m.maze_map[present_cell][p] == True:
                if p == 'E':
                    child_node = (present_cell[0], present_cell[1]+1)
                if p == 'W':
                    child_node = (present_cell[0], present_cell[1]-1)
                if p == 'N':
                    child_node = (present_cell[0]-1, present_cell[1])
                if p == 'S':
                    child_node = (present_cell[0]+1, present_cell[1])
                if child_node in explored:
                    continue
                pos += 1
                explored.append(child_node)
                frontier.append(child_node)
                dfs_route[child_node] = present_cell
                d_all_paths.append(child_node)
        if pos > 1:
            m.markCells.append(present_cell)
            
    forward_route = {}
    grid = m._goal
    while grid != start:
        forward_route[dfs_route[grid]] = grid
        grid = dfs_route[grid]
    print(f"Path: {forward_route}\nNumber of iterations: {num_iterations}")
    dfs_agent = agent(m,footprints=True,color=COLOR.yellow,shape='square')
    m.tracePath({dfs_agent: forward_route}, delay=100)
    l=textLabel(m,'DFS - Length of all the Paths Covered',len(d_all_paths)+1)
    l=textLabel(m,'DFS - Length of Shortest Path',len(forward_route)+1)


   
