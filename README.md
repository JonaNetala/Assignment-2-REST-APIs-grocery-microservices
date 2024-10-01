# CMSC 426 Assignment 2 REST APIs - Grocery Microservices

This project implements two microservices for a grocery shopping application: 
- **Product Service**: Handles product details like name, price, and stock quantity.
- **Cart Service**: Manages a user's shopping cart, including adding and removing products from the cart.


## Deployed Services
- Product Service: [https://product-service-tp9u.onrender.com/products](https://product-service-tp9u.onrender.com/products)
- Cart Service: [https://cart-service-jzv4.onrender.com/cart/1](https://cart-service-jzv4.onrender.com/cart/1)

- ## PLEASE REMEMBER: Users need to first add products to the cart via the POST request before retrieving them with the GET request

## API Endpoints

### Product Service
- `GET /products` : Retrieve a list of all products.
- `GET /products/{product_id}` : Retrieve a specific product by ID.
- `POST /products` : Add a new product to the inventory (name, price, and stock).

### Cart Service
- `GET /cart/{user_id}` : Retrieve the current cart for a user.
- `POST /cart/{user_id}/add/{product_id}` : Add a product to the user’s cart.
- `POST /cart/{user_id}/remove/{product_id}` : Remove a product from the user’s cart.


## Running Locally
- Clone the repository.
- Navigate to `product_service` or `cart_service` directories.
- Install the dependencies using `pip install -r requirements.txt`.
- Run the application using `python app.py`.

