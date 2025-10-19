from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import Book, Cart, User, Order, PaymentGateway, EmailService
import uuid

def register():
    """User registration with graceful error handling"""
    try:
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            name = request.form.get('name')
            address = request.form.get('address', '')

            # Basic validation
            if not email or not password or not name:
                return jsonify({"error": "Email, password, and name are required."}), 400

            # Simulate registration logic
            # user = User.create(email=email, password=password, name=name, address=address)

            return jsonify({"message": "Registration successful."}), 200

    except KeyError as ke:
        return jsonify({"error": f"Missing field: {str(ke)}"}), 400
    except Exception as e:

        return jsonify({"error": "Unexpected error occurred. Please try again."}), 500 
