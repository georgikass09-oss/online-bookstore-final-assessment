import timeit
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import Book, Cart, User, Order, PaymentGateway, EmailService
import uuid

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Cartbook:
    def __init__(self, book, quantity):
        self.book = book
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.items = {}

    def add_book(self, book, quantity=1):
        if book.title in self.items:
            self.items[book.title].quantity += quantity
        else:
            self.items[book.title] = Cartbook(book, quantity)

    def get_total_price(self):
        return sum(item.book.price * item.quantity for item in self.items.values())

# Setup function with large quantities
def setup_cart():
    cart = Cart()
    book = Book("Huge Book quantity", 20)
    cart.add_book(book, quantity=10000)
    return cart

def total_price():
    cart = setup_cart() 
    cart.get_total_price()

execution_time = timeit.timeit(total_price, number=20)
print(f"[Cart] Average execution time over 20 runs: {execution_time:.4f} seconds") 
[Cart] Average execution time over 20 runs: 0.0000 seconds

