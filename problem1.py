test_graph=[[0,1,2,1],
            [1,0,1,1],
            [2,1,0,1],
            [1,1,1,0]]

print(test_graph)

def drive(s,t,test_graph,L):
    distance = 0
    if test_graph[s][t] !=0:
        distance = test_graph[s][t]
        if L < distance :
            print("Your tank can't cover the distance between two cities")
            return False
        else:
            return True
    for i in range test_graph(len(test_graph)):


print(len(test_graph))