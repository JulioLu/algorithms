from customerline import customer_line
from customerline import sum_service_times
from customerline import Customer
from collections import deque

if __name__ == "__main__":
    customer_queue = deque()

    # Παράδειγμα χρήσης
    customers = [
        Customer(1, 6),
        Customer(2, 2),
        Customer(3, 1),
        Customer(4, 5),
        Customer(5, 1),
        Customer(6, 11)
    ]

    for customer in customers:
        customer_queue = customer_line(customer)