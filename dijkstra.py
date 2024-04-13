

def drive(s,t,test_graph,L):
    distance = 0
    if test_graph[s][t] !=0:
        distance = test_graph[s][t]
        if L < distance :
            print("Your tank can't cover the distance between two cities")
            return False
        else:
            return True

def dijkstra(graph, start):
    d = graph['A'].values()
    
        