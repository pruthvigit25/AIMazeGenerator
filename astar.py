
from pymaze import maze,agent,textLabel, COLOR
from queue import PriorityQueue
def m_f(node1,node2):
    a1,b1=node1
    a2,b2=node2

    return abs(a1-a2) + abs(b1-b2)

def run_aStar_algo(m):

    s=(m.rows,m.cols)
    score_a={node:float('inf') for node in m.node}
    score_a[s]=0
    score_b={node:float('inf') for node in m.node}
    score_b[s]=m_f(s,(1,1))

    begin=PriorityQueue()
    begin.put((m_f(s,(1,1)),m_f(s,(1,1)),s))
    astar_route={}
    astar_search = []
    num_iterations = 0 # initialize iteration counter
    while not begin.empty():
        num_iterations += 1 # increment iteration counter
        present_cell=begin.get()[2]
        astar_search.append(present_cell)
        if present_cell==(1,1):
            break
        for p in 'ESNW':
            if m.maze_map[present_cell][p]==True:
                if p=='E':
                    child_node=(present_cell[0],present_cell[1]+1)
                if p=='W':
                    child_node=(present_cell[0],present_cell[1]-1)
                if p=='N':
                    child_node=(present_cell[0]-1,present_cell[1])
                if p=='S':
                    child_node=(present_cell[0]+1,present_cell[1])

                temp_g_score=score_a[present_cell]+1
                temp_f_score=temp_g_score+m_f(child_node,(1,1))

                if temp_f_score < score_b[child_node]:
                    score_a[child_node]= temp_g_score
                    score_b[child_node]= temp_f_score
                    begin.put((temp_f_score,m_f(child_node,(1,1)),child_node))
                    astar_route[child_node]=present_cell
    forward_route={}
    node=(1,1)
    while node!=s:
        forward_route[astar_route[node]]=node
        node=astar_route[node]
    print(f"Path: {forward_route}\nNumber of iterations: {num_iterations}")
    astar_agent=agent(m,footprints=True, shape='square', color=COLOR.green)
    m.tracePath({astar_agent:forward_route})
    l=textLabel(m,'A Star - All the Paths covered : ',len(astar_search)+1)
    l=textLabel(m,'A Star Shortest Path',len(forward_route)+1)


