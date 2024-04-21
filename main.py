from dijkstra import dijkstra
from dijkstra import shortest_path

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

if __name__ == "__main__":
    print(graph)
    print(graph['A'].values())

    start_node = 'A'
    end_node = 'D'

    shortest_path = shortest_path(graph, start_node, end_node)
    if shortest_path is not None:
        print("Συντομότερη διαδρομή από τον κόμβο", start_node, "στον κόμβο", end_node, ":", shortest_path)
        total_distance = sum(graph[shortest_path[i]][shortest_path[i + 1]] for i in range(len(shortest_path) - 1))
        print("Συνολική απόσταση:", total_distance)
    else:
        print("Δεν υπάρχει διαδρομή από τον κόμβο", start_node, "στον κόμβο", end_node)