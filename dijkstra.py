def dijkstra(graph, start):
    # Αρχικοποίηση των αποστάσεων σε άπειρο για όλους τους κόμβους εκτός του start
    distances = {node: float('infinity') for node in graph} #O(V)
    # Η απόσταση από τον εαυτό του είναι πάντα 0
    distances[start] = 0 #O(1)

    # Κρατάμε ένα λεξικό που περιέχει τους προηγούμενους κόμβους κάθε κόμβου
    previous_nodes = {node: None for node in graph} #O(V)

    # Λίστα με τους κόμβους προς εξέταση, αρχικά προσθέτουμε τον start
    nodes_to_visit = [start] #O(1)

    while nodes_to_visit: #O(V)
        # Επιλέγουμε τον κόμβο με τη μικρότερη απόσταση
        current_node = None #O(1)
        for node in nodes_to_visit: #O(V)
            if current_node is None or distances[node] < distances[current_node]: #O(1)
                current_node = node #O(1)

        # Αφαιρούμε τον κόμβο από τη λίστα προς εξέταση
        nodes_to_visit.remove(current_node)  #O(V)

        # Εξερευνούμε τους γείτονες του τρέχοντα κόμβου
        for neighbor, weight in graph[current_node].items(): #O(E)
            new_distance = distances[current_node] + weight #O(1)
            # Αν η νέα απόσταση είναι μικρότερη από την αποθηκευμένη, την ενημερώνουμε
            if new_distance < distances[neighbor]: #O(1)
                distances[neighbor] = new_distance #O(1)
                previous_nodes[neighbor] = current_node #O(1)
                # Προσθέτουμε τον γείτονα στη λίστα προς εξέταση αν δεν είναι ήδη εκεί
                if neighbor not in nodes_to_visit: #O(V)
                    nodes_to_visit.append(neighbor) #O(1)

    return distances, previous_nodes #O(1)
# 2VV + VEV + V + V = VVE + 2VV + 2V

def shortest_path(graph, start, end):
    distances, previous_nodes = dijkstra(graph, start)

    # Αν δεν υπάρχει μονοπάτι από τον start στον end, επιστρέφουμε None
    if distances[end] == float('infinity'):
        return None

    # Αν υπάρχει μονοπάτι, βρίσκουμε τη διαδρομή
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    # Αντιστρέφουμε τη διαδρομή για τη σωστή σειρά
    path = path[::-1]

    return path