test_graph =[[0,1,2,1],[1,0,1,1],[2,1,0,1],[1,1,1,0]]





def f(s,t,test_graph,L):
    distance = 0
    if test_graph[s][t] !=0:
        distance = test_graph[s][t]
        if distance >=L:
            print("To long distance")
            return
        

