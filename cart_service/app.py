from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# In-memory cart storage (for simplicity)
carts = {}

# Get the cart for a specific user
@app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cart = carts.get(user_id, [])
    return jsonify(cart)

# Add a product to the cart
@app.route('/cart/<int:user_id>/add/<int:product_id>', methods=['POST'])
def add_to_cart(user_id, product_id):
    product_service_url = 'http://127.0.0.1:5000/products/'  # Change to Product Service URL later
    product_response = requests.get(f'{product_service_url}{product_id}')
    
    if product_response.status_code == 200:
        product = product_response.json()
        if user_id not in carts:
            carts[user_id] = []
        carts[user_id].append(product)
        return jsonify(carts[user_id]), 201
    return jsonify({'error': 'Product not found'}), 404


# Remove a product from the cart
@app.route('/cart/<int:user_id>/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(user_id, product_id):
    if user_id in carts and product_id in [p['id'] for p in carts[user_id]]:
        # Find the product
        carts[user_id] = [p for p in carts[user_id] if p['id'] != product_id]
        return jsonify(carts[user_id]), 200
    return jsonify({'error': 'Product not in cart'}), 404


if __name__ == '__main__':
    app.run(debug=True, port = 5001)

