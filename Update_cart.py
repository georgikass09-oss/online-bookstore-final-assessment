from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import Book, Cart, User, Order, PaymentGateway, EmailService
import uuid 

def test_update_cart_edge_cases(client):
    # Missing title
    response = client.post('/update_cart', data={'quantity': '2'})
    assert b'No book title provided.' in response.data

    # Non-integer quantity
    response = client.post('/update_cart', data={'title': 'Some Book', 'quantity': 'abc'})
    assert b'Invalid quantity format.' in response.data

    # Book not in cart
    response = client.post('/update_cart', data={'title': 'Ghost Book', 'quantity': '1'})
    assert b'is not in your cart' in response.data

    # Negative quantity
    Cart.add_book(Book('Test Book', 10.0), quantity=2)
    response = client.post('/update_cart', data={'title': 'Test Book', 'quantity': '-1'})
    assert b'Removed "Test Book" from cart!' in response.data

