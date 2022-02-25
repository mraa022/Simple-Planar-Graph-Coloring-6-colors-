COLORS = ['red','green','blue','yellow','black','white']
def get_degree(vertex,matrix,removed_v):
    degree = 0
    #the sum of entries in a row of an adjacency matrix is that vertex's degree
    for i in range(len(matrix[0])):
        v = i
        if v not in removed_v:
            degree += matrix[vertex][v]
    return degree
def find_deg_most_5(adjacency_matrix,removed_vs):
    # if G is a simple planar graph there is always a v such that deg(v)<=5.
    # this function finds such a v
    for vertex in range(len(adjacency_matrix[0])):
        if get_degree(vertex,adjacency_matrix,removed_vs)<=5 and vertex not in removed_vs:
            return vertex
    
def color_most_six(adjacency_matrix,v_list):
    # if |V|<= 6 then it can be colored with at most 6 colors
    # since you can just give each vertex a different color
    coloring = {}
    num_verticies = len(adjacency_matrix[0])    
    for vertex in range(num_verticies):
        if(vertex not in v_list):
            coloring[vertex+1] = COLORS[vertex%6] # %6 is there because the vertex's number might be >5 (list out of range)
    return coloring
    
def set_difference(set1,set2):
    return [x for x in set1 if x not in set2]
    
def neighbor_colors(v,adjacency_matrix,coloring):
    # a function that finds the colors of a vertex's neighbors
    neighbors_c = []
    for i in range(len(adjacency_matrix[0])):
        if adjacency_matrix[v][i] ==1 and i+1 in coloring:
            neighbors_c.append(coloring[i+1])
    return neighbors_c
def color_graph(adjacency_matrix):
    coloring = {}
    num_verticies = len(adjacency_matrix[0])
    if(num_verticies<=6):
        coloring = color_most_six(adjacency_matrix,[])
    
    else:
        removed_v = {}
        removed_stack = []
        # first color 6 Vs
        while num_verticies>6:
           v = find_deg_most_5(adjacency_matrix,removed_v)
           removed_v[v] = 1
           removed_stack.append(v)
           num_verticies -=1
        coloring = color_most_six(adjacency_matrix,removed_v)
        # then color the rest
        while len(removed_stack)!=0:
            vertex = removed_stack.pop()
            v_neighbor_colors = neighbor_colors(vertex,adjacency_matrix,coloring)
            v_color = set_difference(COLORS,v_neighbor_colors)[0]
            coloring[vertex+1] = v_color
    return coloring
    
adjacency_matrix = [[0, 0, 0, 0, 1, 0, 1, 1], 
                    [0, 0, 1, 0, 0, 1, 1, 1], 
                    [0, 1, 0, 0, 0, 1, 0, 0], 
                    [0, 0, 0, 0, 1, 1, 0, 0], 
                    [1, 0, 0, 1, 0, 1, 1, 0], 
                    [0, 1, 1, 1, 1, 0, 1, 0], 
                    [1, 1, 0, 0, 1, 1, 0, 1], 
                    [1, 1, 0, 0, 0, 0, 1, 0]]
print(color_graph(adjacency_matrix))
