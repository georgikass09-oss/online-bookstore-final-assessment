from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import Book, Cart, User, Order, PaymentGateway, EmailService
import uuid

def test_discount_code_edge_cases(client):
    Cart.add_book(Book('Test Book', 100.0), quantity=1)

    # Valid SAVE10
    response = client.post('/apply_discount', data={'discount_code': 'SAVE10'})
    assert b'You saved $10.00' in response.data

    # Valid WELCOME20
    response = client.post('/apply_discount', data={'discount_code': 'WELCOME20'})
    assert b'You saved $20.00' in response.data

    # Invalid code
    response = client.post('/apply_discount', data={'discount_code': 'INVALID'})
    assert b'Invalid discount code' in response.data

    # Empty code
    response = client.post('/apply_discount', data={'discount_code': ''})
    assert b'Discount applied' not in response.data

    # Cart total zero
    Cart.clear()
    response = client.post('/apply_discount', data={'discount_code': 'SAVE10'})
    assert b'Your cart is empty' in response.data