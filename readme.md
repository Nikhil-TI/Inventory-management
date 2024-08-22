# Product Management System

## Overview

The Product Management System is a Python-based application that allows users to manage a list of products. It supports operations such as adding, viewing, updating, and deleting products. The product data is stored in a JSON file, which makes it easy to read and write data persistently.

## Features

- **Add a New Product:** Add new products to the inventory with unique SKU, name, brand, and quantity.
- **View Products:** View all products or filter by name, brand, or quantity. The list can be sorted in ascending or descending order based on quantity.
- **Update a Product:** Update the details of an existing product, including its name, brand, or quantity.
- **Delete a Product:** Remove a product from the inventory by its SKU.

## File Structure

- `data.json`: Stores the product information in JSON format.
- `main.py`: Contains the main application logic and user interface.
- `product.py`: Defines the `Product` class with methods for managing products.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Nikhil-TI/Inventory-management.git
   cd Inventory-management
   ```

2. **Set Up the Project**
    - Ensure you have Python 3.x installed on your machine. This project does not require any additional Python packages beyond the standard library.


## Usage

1. **Run the Application**
    - Execute the main.py script to start the application:
    ```bash
    python main.py
    ```

2. **Navigate the Menu**
    - The application will present the following menu options:

    ```bash
    What do you want to do?
    1. Add a new product
    2. View products
    3. Update a product
    4. Delete a product
    ```
    - Add a New Product: Enter the SKU, name, brand, and quantity for the new product.
    - View Products: Choose to view all products or filter by name, brand, or quantity. Sort the results in ascending or descending order based on quantity.
    - Update a Product: Provide the SKU of the product you wish to update and select which detail (name, brand, or quantity) to change.
    - Delete a Product: Enter the SKU of the product you want to remove from the inventory.

## Code Structure

### `Product` Class

- **`__init__()`**: Loads products from `data.json` and initializes the product list.
- **`__saveProduct()`**: Saves the current product list to `data.json`.
- **`viewProducts()`**: Displays products based on user selection and sorting options.
- **`SKUValidator(SKU)`**: Validates the uniqueness of a SKU.
- **`addProduct()`**: Handles adding a new product after validation.
- **`checkIfProductExists(SKU)`**: Checks if a product with the given SKU exists in the inventory.
- **`updateProduct()`**: Allows updating of product details.
- **`deleteProduct()`**: Deletes a product from the inventory.

### Helper Functions

- **`quantityValidator(quantity)`**: Ensures that the quantity is non-negative.
- **`nameValidator(name)`**: Validates that name and brand fields are not empty.

    






