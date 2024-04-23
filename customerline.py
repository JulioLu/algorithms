from collections import deque

class Customer:
    def __init__(self, customer_id, service_time):
        self.customer_id = customer_id
        self.service_time = service_time
        self.wait_time = 0  # Αρχικός χρόνος αναμονής είναι 0

def customer_line(customer, customer_queue):
    already_in_queue = any(c.customer_id == customer.customer_id for c in customer_queue)
    if already_in_queue:
        print(f"Ο πελάτης με ID {customer.customer_id} είναι ήδη στην ουρά.")
        return customer_queue

    # Εισαγωγή του πελάτη σε αύξουσα σειρά ως προς τον χρόνο εξυπηρέτησης
    inserted = False
    for i, existing_customer in enumerate(customer_queue):
        if customer.service_time < existing_customer.service_time:
            customer_queue.insert(i, customer)
            inserted = True
            break

    if not inserted:
        customer_queue.append(customer)

    # Υπολογισμός χρόνου αναμονής για κάθε πελάτη
    update_wait_times(customer_queue)

    print(f"Ο πελάτης με ID {customer.customer_id} βρίσκεται στην ουρά.")
    print("Πελάτες στην ουρά:")
    for c in customer_queue:
        print(f"ID: {c.customer_id}, Χρόνος Εξυπηρέτησης: {c.service_time} λεπτά, Χρόνος Αναμονής: {c.wait_time} λεπτά")
    total_wait_time = sum_wait_times(customer_queue)
    print(f"Ο συνολικός χρόνος αναμονής είναι: {total_wait_time}")
    return customer_queue

def sum_wait_times(queue):
    total_time = sum(customer.wait_time for customer in queue)
    return total_time

def update_wait_times(queue):
    for i in range(1, len(queue)):
        queue[i].wait_time = queue[i-1].wait_time + queue[i-1].service_time