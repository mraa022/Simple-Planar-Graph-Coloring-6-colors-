COLORS = ['red','green','blue','yellow','black','white']
def find_deg_most_5(adjacency_matrix,removed_vs):
    # if G is a simple planar graph there is always a v such that deg(v)<=5.
    # this function finds such a v
    degree = lambda vertex: sum(adjacency_matrix[vertex]) # the sum of entries in a row of an adjacency matrix is that vertix's degree
    for vertex in range(len(adjacency_matrix[0])):
        if degree(vertex)<=5 and vertex not in removed_vs:
            return vertex
    
def color_most_six(adjacency_matrix,v_list):
    # if |V|<= 6 then it can be colored with at most 6 colors
    # since you can just give each vertex a different color
    coloring = {}
    num_verticies = len(adjacency_matrix[0])    
    for vertex in range(num_verticies):
        if(vertex not in v_list):
            coloring[vertex] = COLORS[vertex%6] # %6 is there because the vertex's number might be >5 (list out of range)
    return coloring
    
def set_difference(set1,set2):
    return [x for x in set1 if x not in set2]
    
def neighbor_colors(v,adjacency_matrix,coloring):
    # a function that funds the colors of a vertex's neighbors
    neighbors_c = []
    for i in range(len(adjacency_matrix[0])):
        if adjacency_matrix[v][i] ==1 and i in coloring:
            neighbors_c.append(coloring[i])
    return neighbors_c
def color_graph(adjacency_matrix):
    coloring = {}
    num_verticies = len(adjacency_matrix[0])
    if(num_verticies<=6):
        coloring = color_most_six(adjacency_matrix,[])
    
    else:
        removed_v = {}
        
        # first color 6 Vs
        while num_verticies>6:
           v = find_deg_most_5(adjacency_matrix,removed_v)
           removed_v[v] = 1
           num_verticies -=1
        coloring = color_most_six(adjacency_matrix,removed_v)
        
        # then color the rest
        for vertex in removed_v.keys():
            v_neighbor_colors = neighbor_colors(vertex,adjacency_matrix,coloring)
            v_color = set_difference(COLORS,v_neighbor_colors)[0]
            coloring[vertex] = v_color
    return coloring
    
adjacency_matrix = [[0, 1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 0, 0, 0, 0, 0, 0], 
                    [0, 1, 0, 0, 0, 1, 0, 0, 0], 
                    [0, 0, 0, 0, 1, 0, 0, 0, 1], 
                    [0, 0, 0, 1, 0, 1, 0, 0, 0], 
                    [0, 0, 1, 0, 1, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0, 1, 1, 0, 0],
                    [1, 0, 0, 1, 0, 0, 1, 0, 0]] 
print(color_graph(adjacency_matrix))
