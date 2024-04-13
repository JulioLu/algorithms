test_graph=[[0,1,2,1],
            [1,0,1,1],
            [2,1,0,1],
            [1,1,1,0]]

print(test_graph)

def drive(s, t, test_graph, L):
    if(test_graph[s][t] != 0):
        
        