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

# Verify that the quantity is not negative
def quantityValidator(quantity):
    if quantity < 0:
        print("Quantity cannot be negative!")
        print("Returning to main menu.")
        return False
    return True

# Verify that the name is not null
def nameValidator(name):
    if name == "":
        print("Name or Brand cannot be empty!")
        print("Returning to main menu.")
        return False
    return True

import sqlite3

class Product:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.loadProductsFromDB()

    def loadProductsFromDB(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM inventoryStorage")
        rows = cursor.fetchall()
        self.__allProducts = []
        for row in rows:
            self.__allProducts.append({
                "SKU": row[0],
                "name": row[1],
                "brand": row[2],
                "quantity": row[3]
            })
        self.productCount = len(self.__allProducts)

    def saveProductToDB(self, product):
        cursor = self.db_connection.cursor()
        cursor.execute("""INSERT INTO inventoryStorage (SKU, name, brand, quantity)
                          VALUES (?, ?, ?, ?)""",
                       (product["SKU"], product["name"], product["brand"], product["quantity"]))
        self.db_connection.commit()

    def updateProductInDB(self, SKU, updateData):
        cursor = self.db_connection.cursor()
        updateString = ", ".join([f"{key} = ?" for key in updateData.keys()])
        query = f"UPDATE inventoryStorage SET {updateString} WHERE SKU = ?"
        values = list(updateData.values()) + [SKU]
        cursor.execute(query, values)
        self.db_connection.commit()

    def deleteProductFromDB(self, SKU):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM inventoryStorage WHERE SKU = ?", (SKU,))
        self.db_connection.commit()

    def viewProducts(self):
        print("View options")
        print("1. All products")
        print("2. By product name")
        print("3. By brand name")
        print("4. By quantity")
        selection = int(input())
        if selection == 1:
            for product in self.__allProducts:
                print(product)
        elif selection == 2:
            name = input("Enter product name: ")
            found = False
            for product in self.__allProducts:
                if product["name"] == name:
                    print(product)
                    found = True
            if not found:
                print("No product with name", name, "found")
        elif selection == 3:
            brand = input("Enter product brand: ")
            found = False
            for product in self.__allProducts:
                if product["brand"] == brand:
                    print(product)
                    found = True
            if not found:
                print("No product with brand", brand, "found")
        elif selection == 4:
            print("1. Ascending order")
            print("2. Descending order")
            option = int(input())
            sortedProducts = sorted(self.__allProducts, key=lambda d: d['quantity'], reverse=(option == 2))
            for product in sortedProducts:
                print(product)
        else:
            print("Invalid option")

    def SKUValidator(self, SKU):
        return all(product["SKU"] != SKU for product in self.__allProducts)

    def addProduct(self):
        SKU = input("Enter the SKU: ")
        if not self.SKUValidator(SKU) or SKU == "":
            print("SKU must be unique!")
            print("Returning to main menu.")
            return

        name = input("Enter the name of the product: ")
        if not nameValidator(name):
            return

        brand = input("Enter the brand of the product: ")
        if not nameValidator(brand):
            return

        quantity = int(input("Enter the quantity of the product: "))
        if not quantityValidator(quantity):
            return

        productData = {
            "SKU": SKU,
            "name": name,
            "brand": brand,
            "quantity": quantity
        }
        self.__allProducts.append(productData)
        self.productCount += 1
        self.saveProductToDB(productData)

    def checkIfProductExists(self, SKU):
        return any(product["SKU"] == SKU for product in self.__allProducts)

    def updateProduct(self):
        SKU = input("Enter the SKU of the product: ")
        if not self.checkIfProductExists(SKU):
            print("Product doesn't exist!")
            return

        updateData = {}
        for product in self.__allProducts:
            if product["SKU"] == SKU:
                print("What do you want to update?")
                print("1. Name of the product")
                print("2. Brand of the product")
                print("3. Quantity of the product")
                selection = int(input())
                if selection == 1:
                    newName = input("Enter the new name: ")
                    if nameValidator(newName):
                        updateData["name"] = newName
                elif selection == 2:
                    newBrand = input("Enter the new brand: ")
                    if nameValidator(newBrand):
                        updateData["brand"] = newBrand
                elif selection == 3:
                    newQuantity = int(input("Enter the new quantity: "))
                    if quantityValidator(newQuantity):
                        updateData["quantity"] = newQuantity
                else:
                    print("Invalid input!")
                    print("You will be sent back to the main menu!")
                    return
                self.updateProductInDB(SKU, updateData)
                self.loadProductsFromDB()  # Reload products from DB after update
                break

    def deleteProduct(self):
        SKU = input("Enter the SKU of the product: ")
        if not self.checkIfProductExists(SKU):
            print("Product doesn't exist!")
            return

        self.deleteProductFromDB(SKU)
        self.__allProducts = [product for product in self.__allProducts if product["SKU"] != SKU]
        self.productCount -= 1
