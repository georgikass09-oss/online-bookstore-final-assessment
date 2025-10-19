# performance Testing with timeit
def get_order_history(self):
         return [order for order in self.orders]  

import timeit
class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

# Creation a chief for multiple orders
class OrderChief:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_order_history(self):
        return [order for order in self.orders]

# Setup function to manage many orders
def setup_chief():
    chief = OrderChief()
    for i in range(10000):    # Simulate large order history
        chief.add_order(Order(order_id=i, amount=100.0))
    return chief

# Wrapper for timeit

def measure_order_history():
    chief = setup_chief()
    chief.get_order_history()

# Run the benchmark
execution_time = timeit.timeit(measure_order_history, number=20)
print(f"Average execution time over 20 runs: {execution_time:.4f} seconds")

Average execution time over 20 runs: 0.0897 seconds
