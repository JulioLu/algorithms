from customerline import customer_line
from customerline import sum_service_times
from customerline import Customer

if __name__ == "__main__":
    # Δημιουργούμε πελάτες
    customer1 = Customer(1, 6)  # ID: 1, Χρόνος Εξυπηρέτησης: 6 λεπτά
    customer2 = Customer(2, 1)  # ID: 2, Χρόνος Εξυπηρέτησης: 1 λεπτό
    customer3 = Customer(3, 1)  # ID: 3, Χρόνος Εξυπηρέτησης: 1 λεπτό
    customer4 = Customer(4, 1)  # ID: 4, Χρόνος Εξυπηρέτησης: 1 λεπτό
    customer5 = Customer(5, 1)  # ID: 5, Χρόνος Εξυπηρέτησης: 1 λεπτό
    customer6 = Customer(6, 1)  # ID: 6, Χρόνος Εξυπηρέτησης: 1 λεπτό

    # Προσθέτουμε τους πελάτες στην ουρά
    customer_queue = customer_line(customer1)
    customer_queue = customer_line(customer2)
    customer_queue = customer_line(customer3)
    customer_queue = customer_line(customer4)
    customer_queue = customer_line(customer5)
    customer_queue = customer_line(customer6)