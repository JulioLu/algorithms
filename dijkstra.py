def dijkstra(graph, start):
    # Αρχικοποίηση των αποστάσεων σε άπειρο για όλους τους κόμβους εκτός του start
    distances = {node: float('infinity') for node in graph}
    # Η απόσταση από τον εαυτό του είναι πάντα 0
    distances[start] = 0

    # Κρατάμε ένα λεξικό που περιέχει τους προηγούμενους κόμβους κάθε κόμβου
    previous_nodes = {node: None for node in graph}

    # Λίστα με τους κόμβους προς εξέταση, αρχικά προσθέτουμε τον start
    nodes_to_visit = [start]

    while nodes_to_visit:
        # Επιλέγουμε τον κόμβο με τη μικρότερη απόσταση
        current_node = None
        for node in nodes_to_visit:
            if current_node is None or distances[node] < distances[current_node]:
                current_node = node

        # Αφαιρούμε τον κόμβο από τη λίστα προς εξέταση
        nodes_to_visit.remove(current_node)

        # Εξερευνούμε τους γείτονες του τρέχοντα κόμβου
        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            # Αν η νέα απόσταση είναι μικρότερη από την αποθηκευμένη, την ενημερώνουμε
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                # Προσθέτουμε τον γείτονα στη λίστα προς εξέταση αν δεν είναι ήδη εκεί
                if neighbor not in nodes_to_visit:
                    nodes_to_visit.append(neighbor)

    return distances, previous_nodes


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
