import razorpay
import os

class PaymentService:
    def process_payment(self, amount: float, payment_details: dict):
        api_key = os.environ.get('RAZORPAY_API_KEY')
        api_secret_key = os.environ.get('RAZORPAY_SECRET_KEY')

        razorpay_client = razorpay.Client(api_key, api_secret_key)

        order_data = {
            'amount': amount,
            'currency': 'INR',
            'payment_capture': 1,
            'receipt': payment_details
        }
        try:
            order = client.order.create(data=order_data)
            return True
        except:
            print("Payment Failed")
            return False
        