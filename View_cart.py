from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import Book, Cart, User, Order, PaymentGateway, EmailService,client
import uuid 

def test_view_cart_edge_cases(user):

    # No user in session:
    with client.session_transaction() as sess:
        sess.clear()
    response = client.get('/view_cart')
    assert b'You must be logged in' in response.data

    # User with no cart:
    mock_user = User(id=1, name='TestUser')
    mock_user.cart = None
    response = client.get('/view_cart')
    assert b'No cart found' in response.data

    # Empty cart:
    mock_user.cart = Cart()
    response = client.get('/view_cart')
    assert b'Your cart is empty' in response.data or b'cart.html' in response.data
