from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import Book, Cart, User, Order, PaymentGateway, EmailService
import uuid

def test_remove_from_cart_edge_cases(user):

    # No title provided:
    response = user.post('/remove_from_cart', data={})
    assert b'No book title provided.' in response.data

    # Title not in cart:
    response = user.post('/remove_from_cart', data={'title': 'Nonexistent Book'})
    assert b'is not in your cart' in response.data

    # Empty cart:
    Cart.clear()
    response = user.post('/remove_from_cart', data={'title': 'Any Book'})
    assert b'Your cart is already empty.' in response.data
