from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import Book, Cart, User, Order, PaymentGateway, EmailService
import uuid


def test_registration_edge_cases(client):
    # Missing fields
    response = client.post('/register', data={'email': '', 'password': '', 'name': ''})
    assert b'Please fill in all required fields' in response.data

    # Invalid email format
    response = client.post('/register', data={'email': 'invalidemail', 'password': 'pass', 'name': 'User'})
    assert b'Invalid email format' in response.data

    # Duplicate email
    User['123@Example.com'] = User('123@Example.com', 'pass', 'User', '') # type: ignore
    response = client.post('/register', data={'email': 'test@Example.com', 'password': 'pass', 'name': 'User'})
    assert b'already exists' in response.data 


def test_login_edge_cases(client):
    # Missing credentials
    response = client.post('/login', data={'email': '', 'password': ''})
    assert b'Invalid email or password' in response.data

    # Incorrect password
    User['123@Example.com'] = User('123@Example.com', 'correctpass', 'User', '') # type: ignore
    response = client.post('/login', data={'email': 'test@Example.com', 'password': 'wrongpass'})
    assert b'Invalid email or password' in response.data

    # Nonexistent email
    response = client.post('/login', data={'email': 'ghost@Example.com', 'password': 'pass'})
    assert b'Invalid email or password' in response.data