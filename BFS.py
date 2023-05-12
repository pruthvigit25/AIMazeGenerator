
from pymaze import maze,agent,textLabel,COLOR
from collections import deque

def run_BFS_algo(m, s=None):
    if s is None:
        s=(m.rows,m.cols)
    frontier = deque()
    frontier.append(s)
    bfs_route = {}
    explored = [s]
    b_all_paths=[]
    num_iterations = 0 # initialize iteration counter
    while len(frontier)>0:
        num_iterations += 1 # increment iteration counter
        present_cell=frontier.popleft()
        if present_cell==m._goal:
            break
        for p in 'ESNW':
            if m.maze_map[present_cell][p]==True:
                if p=='E':
                    child_node=(present_cell[0],present_cell[1]+1)
                elif p=='W':
                    child_node=(present_cell[0],present_cell[1]-1)
                elif p=='S':
                    child_node=(present_cell[0]+1,present_cell[1])
                elif p=='N':
                    child_node=(present_cell[0]-1,present_cell[1])
                if child_node in explored:
                    continue
                frontier.append(child_node)
                explored.append(child_node)
                bfs_route[child_node] = present_cell
                b_all_paths.append(child_node)
    
    forward_route={}
    grid=m._goal
    while grid!=(m.rows,m.cols):
        forward_route[bfs_route[grid]]=grid
        grid=bfs_route[grid]
    print(f"Path: {forward_route}\nNumber of iterations: {num_iterations}")    
    bfs_agent=agent(m,footprints=True,color=COLOR.cyan,shape='square')
    m.tracePath({bfs_agent:forward_route},delay=100)
    l=textLabel(m,'BFS - Length of all the Paths Covered',len(b_all_paths)+1)
    l=textLabel(m,'BFS - Length of Shortest Path',len(forward_route)+1)
