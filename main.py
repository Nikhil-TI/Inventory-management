from Manager.product import Product
import sqlite3

sqliteConnection = sqlite3.connect('./Storage/storeManagementSystem.db')
print("Database connected.")

# Create the table if it doesn't exist
sqliteConnection.execute("""CREATE TABLE IF NOT EXISTS inventoryStorage (
    SKU VARCHAR(20) PRIMARY KEY,
    name VARCHAR(20),
    brand VARCHAR(20),
    quantity INTEGER
)""")
sqliteConnection.commit()

# Main menu options
mainOptions = ("What do you want to do?", "1. Add a new product", "2. View products", "3. Update a product", "4. Delete a product", "5. Get the number of unique products in the database")

def viewMainOptions():
    for option in mainOptions:
        print(option)
    selection = int(input("Enter your choice (1/2/3/4/5): "))
    return selection

# Call the corresponding task from the Product Object
def performTask(selection):
    # Creating a new product object with the database connection
    newProduct = Product(sqliteConnection)
    match selection:
        case 1: newProduct.addProduct()
        case 2: newProduct.viewProducts()
        case 3: newProduct.updateProduct()
        case 4: newProduct.deleteProduct()
        case 5: print("Number of unique products is: ", newProduct.productCount)
        case _: print("Invalid input! Try again.")

def main():
    # Keep asking the user for tasks to be done
    while True:
        selection = viewMainOptions()
        performTask(selection)
        print()

if __name__ == "__main__":
    main()

# Closing the database connection
sqliteConnection.close()
