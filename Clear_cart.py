from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import Book, Cart, User, Order, PaymentGateway, EmailService
import uuid 

def test_clear_cart_edge_cases(client):
    # No user in session
    with client.session_transaction() as sess:
        sess.clear()
    response = client.post('/clear_cart')
    assert b'You must be logged in' in response.data

    # User with no cart
    mock_user = User(id=1, name='TestUser')
    mock_user.cart = None
    response = client.post('/clear_cart')
    assert b'No cart found' in response.data

    # Empty cart
    mock_user.cart = Cart()
    response = client.post('/clear_cart')
    assert b'already empty' in response.data

    # Cart with items
    mock_user.cart.add_book(Book('Test Book', 10.0), quantity=2)
    response = client.post('/clear_cart')
    assert b'Cart cleared!' in response.data