# locustfile.py 

from locust import User,task 
from process_checkout_service import process_checkout # pyright: ignore[reportMissingImports]

class CheckoutUser(User):
    @task
    def simulate_checkout (self):
        process_checkout ("/checkout", data={
            "shipping_address": "89 London St",
            "payment_method": "credit_card",
            "card_number": "0987654321543758",
            "expiry": "09/30",
            "cvv": "123"
        })