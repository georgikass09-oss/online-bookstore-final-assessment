from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import Book, Cart, User, Order, PaymentGateway, EmailService
import uuid

def login():
    """User login with input validation and graceful error handling"""
    try:
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            # Validate input presence
            if not email or not password:
                return jsonify({"error": "Email and password are required."}), 400

            # Simulate authentication logic
            # user = User.authenticate(email=email, password=password)
            # if not user:
            #     return jsonify({"error": "Invalid credentials."}), 401

            return jsonify({"message": "Login successful."}), 200

    except Exception as e:
        # Catch unexpected errors (e.g., malformed form data, server issues)
        print(f"Login error: {e}")

        return jsonify({"error": "An unexpected error occurred. Please try again."}), 500
