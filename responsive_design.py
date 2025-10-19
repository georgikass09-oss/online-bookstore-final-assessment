from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from models import Book, Cart, User, Order, PaymentGateway, EmailService
import uuid 

def get_book_by_title_with_retry(max_attempts=3):
    """Retries user input until a valid book title is found or attempts exhausted"""
    attempt = 0
    while attempt < max_attempts:
        try:
            raw_input = input("Enter book title: ")
            normalized_title = str(raw_input).strip().lower()
            book = next((book for book in BOOKS if book.title.lower() == normalized_title), None) # pyright: ignore[reportUndefinedVariable]
            if book:
                return book
            else:
                print("Book not found. Please try again.")
        except Exception as e:
            print(f"Invalid input: {e}. Please enter a valid title.")
        attempt += 1
    print("Maximum attempts reached. No valid book found.")
    return None