import json
filePath = "./Storage/data.json"

def quantityValidator(quantity):
    if(quantity < 0):
        print("Quantity cannot be negative!")
        print("Returning to main menu.")
        return False
    return True

def nameValidator(name):
    if name == "":
        print("Name or Brand cannot be empty!")
        print("Returning to main menu.")
        return False
    return True

class Product:
    __allProducts = []

    __productData = {
        "SKU": None,
        "name": None,
        "brand": None,
        "quantity": None
    }

    def __init__(self):
        dataFile = open(filePath)
        data = json.load(dataFile)
        self.__allProducts = data

    def __saveProduct(self):
        if(self.__productData["SKU"] != None):
            self.__allProducts.append(self.__productData)
        with open(filePath, 'w') as file:
            json.dump(self.__allProducts, file)

    def viewProducts(self):
        print("View options")
        print("1. All products")
        print("2. by product name")
        print("3. by brand name")
        print("4. by quantity")
        selection = int(input())
        match selection:
            case 1:
                for product in self.__allProducts:
                    print(product)
            case 2:
                name = input("Enter product name: ")
                flag = False
                for product in self.__allProducts:
                    if(product["name"] == name):
                        print(product)
                        flag = True
                if flag == False:
                    print("No product with name", name, " found")
            case 3:
                brand = input("Enter product brand: ")
                flag = False
                for product in self.__allProducts:
                    if(product["brand"] == brand):
                        print(product)
                        flag = True
                if flag == False:
                    print("No product with brand", brand, " found")
            case 4:
                print("1. Ascending order")
                print("2. Decending order")
                option = int(input())
                if(option == 1):
                    newlist = sorted(self.__allProducts, key=lambda d: d['quantity'])
                    for product in newlist:
                        print(product)
                else:
                    newlist = sorted(self.__allProducts, key=lambda d: d['quantity'], reverse=True)
                    for product in newlist:
                        print(product)



    
    def SKUValidator(self, SKU):
        for product in self.__allProducts:
            if product["SKU"] == SKU:
                return False
        return True

    def addProduct(self):
        SKU = input("Enter the SKU: ")
        self.__productData["SKU"] = SKU
        if self.SKUValidator(SKU) == False or SKU == "":
            print("SKU must be unique!")
            print("Returning to main menu.")
            return
        
        name = input("Enter the name of the product: ")
        self.__productData["name"] = name
        if nameValidator(name) == False:
            return
        
        brand = input("Enter the brand of the product: ")
        self.__productData["brand"] = brand
        if nameValidator(brand) == False:
            return
        
        quantity = int(input("Enter the quatity of the product: "))
        if quantityValidator(quantity) == False:
            return
        self.__productData["quantity"] = quantity
        self.__saveProduct()
    
    def checkIfProductExists(self, SKU):
        for products in self.__allProducts:
            if(products["SKU"] == SKU):
                return True
        return False
    
    def updateProduct(self):
        SKU = input("Enter the SKU of the product: ")
        if(self.checkIfProductExists(SKU) == False):
            print("Product doesn't exist!")
            return
        for product in self.__allProducts:
            if product["SKU"] == SKU:
                print("what do you want to update?")
                print("1. Name of the product")    
                print("2. Brand of the product")    
                print("3. Quantity of the product")
                selection = int(input())
                match selection:
                    case 1:
                        print("Current name:", product["name"])
                        name = input("Enter the new name: ")
                        product["name"] = name
                    case 2:
                        print("Current brand:", product["brand"])
                        brand = input("Enter the new brand: ")
                        product["brand"] = brand
                    case 3:
                        print("Current name:", product["name"])
                        quantity = input("Enter the new quantity: ")
                        product["quantity"] = quantity
                    case _:
                        print("Invalid input!")
                        print("You will will send back to main menu!")
                break
        self.__saveProduct()
        print("data updated")
                
    def deleteProduct(self):
        SKU = input("Enter the SKU of the product: ")
        if(self.checkIfProductExists(SKU) == False):
            print("Product doesn't exist!")
            return
        for product in self.__allProducts:
            if product["SKU"] == SKU:
                self.__allProducts.remove(product)
        self.__saveProduct()