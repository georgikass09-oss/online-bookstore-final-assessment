import pytest

class PaymentGateway:

 def test_valid_card():
    result = PaymentGateway.process_payment({'card_number': '4242424242424242'})
    assert result['success'] is True

def test_invalid_card():
    result = PaymentGateway.process_payment({'card_number': '123456781111'})
    assert result['success'] is False
    assert 'Invalid card number' in result['message']

def test_empty_card():
    result = PaymentGateway.process_payment({'card_number': ''})
    assert result['success'] is False

def test_missing_card_key():
    result = PaymentGateway.process_payment({})
    assert result['success'] is False