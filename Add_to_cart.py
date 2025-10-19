from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import Book, Cart, User, Order, PaymentGateway, EmailService
import uuid

def test_add_to_cart_edge_cases(User): 

# Missing title: 
response = User.post('/add_to_cart', data={'quantity': '2'}) 
assert b'Book not found!' in response.data 

# Non-integer quantity: 
response = User.post('/add_to_cart', data={'title': 'Some Book', 'quantity': 'abc'}) 
assert b'Invalid quantity format.' in response.data 

# Negative quantity: 
response = User.post('/add_to_cart', data={'title': 'Some Book', 'quantity': '-5'}) 
assert b'Quantity must be a positive number.' in response.data 