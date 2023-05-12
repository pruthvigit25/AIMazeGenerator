from pymaze import maze, agent, textLabel, COLOR
import value
import Policy
import astar
import DFS
import BFS

def maze_algorithms(rows, columns, name='run_all'):


    m = maze(rows, columns)
    m.CreateMaze(loopPercent=100)

    #Running MDP - Value Iteration Algorithm 
    if name == 'vi' or name =='run_all':
        value.run_value_iteration_algo(m, 0.6, 0.0001)
    if name == 'pi' or name =='run_all':
        Policy.run_value_iteration_algo(m, 0.6, 0.0001)
    if name == 'astar' or name =='run_all':
        astar.run_aStar_algo(m)
    if name == 'dfs' or name =='run_all':
        DFS.run_dfs_algo(m)
    if name == 'bfs' or name =='run_all':
        BFS.run_BFS_algo(m)

    m.run()

def main():

    maze_algorithms(5, 10,'astar')

if __name__ == '__main__':
    main()

