from collections import deque

customer_queue = deque()
class Customer:
    def __init__(self, customer_id, service_time):
        self.customer_id = customer_id
        self.service_time = service_time

def customer_line(customer):
    if not customer_queue:
        customer_queue.append(customer)

    wait_time = customer.service_time
    total_wait_time = sum_service_times(customer_queue)
    avg_wait_time = total_wait_time / len(customer_queue)

    if customer.service_time > avg_wait_time:
        print(f"Ο πελάτης με ID {customer.customer_id} έχει μεγάλο χρόνο αναμονής. Μπαίνει στο τέλος της ουράς")
        customer_queue.append(customer)
    else:
        print(f"Ο πελάτης με ID {customer.customer_id} έχει μικρό χρόνο αναμονής. Μπαίνει μπροστά στην ουρά.")
        customer_queue.appendleft(customer)

    print(f"Ο πελάτης με ID {customer.customer_id} βρίσκεται στην ουρά.")
    print("Πελάτες στην ουρά:")
    for c in customer_queue:
        print(f"ID: {c.customer_id}, Χρόνος Εξυπηρέτησης: {c.service_time} λεπτά")
    print(f"Ο χρόνος αναμονής είναι: {total_wait_time}")
    return customer_queue

def sum_service_times(queue):
    total_time = sum(customer.service_time for customer in queue)
    return total_time
