COLORS = ['red','green','blue','yellow','black','white']
def find_deg_most_5(adjacency_matrix,removed_vs):
    degree = lambda vertex: sum(adjacency_matrix[vertex])
    for vertex in range(len(adjacency_matrix[0])):
        if degree(vertex)<=5 and vertex not in removed_vs:
            return vertex
    
def color_most_six(adjacency_matrix,v_list):
    coloring = {}
    num_verticies = len(adjacency_matrix[0])    
    for vertex in range(num_verticies):
        if(vertex not in v_list):
            coloring[vertex] = COLORS[vertex%6]
    return coloring
    
def set_difference(set1,set2):
    return [x for x in set1 if x not in set2]
    
def neighbor_colors(v,adjacency_matrix,coloring):
    neighbors = []
    for i in range(len(adjacency_matrix[0])):
        if adjacency_matrix[v][i] ==1 and i in coloring:
            neighbors.append(coloring[i])
    
def color_graph(adjacency_matrix):
    coloring = {}
    num_verticies = len(adjacency_matrix[0])
    if(num_verticies<=6):
        coloring = color_most_six(adjacency_matrix,[])
    
    else:
        removed_v = {}
        while num_verticies>6:
           v = find_deg_most_5(adjacency_matrix,removed_v)
           removed_v[v] = 1
           num_verticies -=1
        coloring = color_most_six(adjacency_matrix,removed_v)
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