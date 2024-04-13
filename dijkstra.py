
test_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

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
        