from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory product storage (for simplicity)
products = [
    {'id': 1, 'name': 'Apple', 'price': 0.50, 'stock': 100},
    {'id': 2, 'name': 'Banana', 'price': 0.30, 'stock': 150},
]

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Get product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

# Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.get_json()
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True)
