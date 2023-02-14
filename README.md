# Stripe Payment Server
This is a server built with Django that communicates with Stripe to create payment forms for various products.

## Endpoints

### GET /buy/{id}
This endpoint allows the user to obtain a Stripe Session Id to make a payment for the selected item. When this method is executed on the backend using the Python library stripe.checkout.Session.create(...), the obtained session.id is then returned as the result of the request.

### GET /item/{id}
This endpoint provides a simple HTML page with information about the selected item and a Buy button. When the user clicks the Buy button, a request is made to /buy/{id} to obtain the session_id, and with the help of the JS library Stripe, a redirect to the Checkout form stripe.redirectToCheckout(sessionId=session_id) occurs.

### GET /order/{id}
This endpoint allows the user to obtain the details of the order with the provided id.

### GET /buy/order/{id}
This endpoint allows the user to obtain a Stripe Session Id to make a payment for the selected order with the provided id.

## Usage

To access the server, visit the domain http://spar86.pythonanywhere.com. 
The login credentials for the Django admin panel are as follows:

***Username***: user

***Password***: user

## Dependencies

The server uses the following dependencies:

Django

stripe

Python 3.7+
