from dijkstra import dijkstra

test_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

if __name__ == "__main__":
    print(test_graph)
    print(test_graph['A'].values())
    
    dijkstra(test_graph,"A")
    