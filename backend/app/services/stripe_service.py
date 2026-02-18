import stripe

class StripeService:
    def __init__(self, api_key):
        stripe.api_key = api_key

    def create_payment(self, amount, currency='usd', payment_method=None):
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=currency,
                payment_method=payment_method,
                confirm=True
            )
            return payment_intent
        except Exception as e:
            raise Exception(f'Payment failed: {str(e)}')

    def create_subscription(self, customer_id, price_id):
        try:
            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[{'price': price_id}],
                expand=['latest_invoice.payment_intent']
            )
            return subscription
        except Exception as e:
            raise Exception(f'Subscription creation failed: {str(e)}')

    def cancel_subscription(self, subscription_id):
        try:
            stripe.Subscription.delete(subscription_id)
        except Exception as e:
            raise Exception(f'Canceling subscription failed: {str(e)}')

    def list_customer_subscriptions(self, customer_id):
        try:
            subscriptions = stripe.Subscription.list(customer=customer_id)
            return subscriptions
        except Exception as e:
            raise Exception(f'Listing subscriptions failed: {str(e)}')
