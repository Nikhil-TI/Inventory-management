import json
#Path of our data stored in the json file
filePath = "./Storage/data.json"

#verify that the quantity is not negative
def quantityValidator(quantity):
    if(quantity < 0):
        print("Quantity cannot be negative!")
        print("Returning to main menu.")
        return False
    return True

#verify that the name is not null
def nameValidator(name):
    if name == "":
        print("Name or Brand cannot be empty!")
        print("Returning to main menu.")
        return False
    return True

class Product:
    #all product data obtained from the file
    __allProducts = []

    __productData = {
        "SKU": None,
        "name": None,
        "brand": None,
        "quantity": None
    }

    #load all the products from the json file
    def __init__(self):
        dataFile = open(filePath)
        data = json.load(dataFile)
        self.__allProducts = data

    #save the current list of all products in the json file
    def __saveProduct(self):
        if(self.__productData["SKU"] != None):
            self.__allProducts.append(self.__productData)
        with open(filePath, 'w') as file:
            json.dump(self.__allProducts, file)
    
    #display the products in the terminal
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
                #check if the provided product name is valid or not
                for product in self.__allProducts:
                    if(product["name"] == name):
                        print(product)
                        flag = True
                if flag == False:
                    print("No product with name", name, " found")
            case 3:
                brand = input("Enter product brand: ")
                flag = False
                #check if the provided brand is valid or not
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
                    #print the data in ascending order
                    newlist = sorted(self.__allProducts, key=lambda d: d['quantity'])
                    for product in newlist:
                        print(product)
                else:
                    #print the data in descending order
                    newlist = sorted(self.__allProducts, key=lambda d: d['quantity'], reverse=True)
                    for product in newlist:
                        print(product)



    #check the SKU is valid or not ie. it is unique
    def SKUValidator(self, SKU):
        for product in self.__allProducts:
            if product["SKU"] == SKU:
                return False
        return True
    
    #add the product to the object instance
    def addProduct(self):
        SKU = input("Enter the SKU: ")
        self.__productData["SKU"] = SKU
        #velidte the SKU
        if self.SKUValidator(SKU) == False or SKU == "":
            print("SKU must be unique!")
            print("Returning to main menu.")
            return
        
        name = input("Enter the name of the product: ")
        self.__productData["name"] = name
        #check if provided name is not null
        if nameValidator(name) == False:
            return
        
        brand = input("Enter the brand of the product: ")
        self.__productData["brand"] = brand
        #check if provided brand is not null
        if nameValidator(brand) == False:
            return
        
        quantity = int(input("Enter the quatity of the product: "))
        #verify that the quantuty is not negative
        if quantityValidator(quantity) == False:
            return
        self.__productData["quantity"] = quantity
        self.__saveProduct()
    
    #check if the product exists or not
    def checkIfProductExists(self, SKU):
        for products in self.__allProducts:
            if(products["SKU"] == SKU):
                return True
        return False
    
    #update the product data
    def updateProduct(self):
        SKU = input("Enter the SKU of the product: ")
        #check if the product with the provided SKU exists or not
        if(self.checkIfProductExists(SKU) == False):
            print("Product doesn't exist!")
            return
        #find the produc twith the given SKU in AllProduct list
        for product in self.__allProducts:
            if product["SKU"] == SKU:
                #get the value that the user wants to update
                print("what do you want to update?")
                print("1. Name of the product")    
                print("2. Brand of the product")    
                print("3. Quantity of the product")
                selection = int(input())
                match selection:
                    case 1:
                        #update product name
                        print("Current name:", product["name"])
                        name = input("Enter the new name: ")
                        product["name"] = name
                    case 2:
                        #update product brand
                        print("Current brand:", product["brand"])
                        brand = input("Enter the new brand: ")
                        product["brand"] = brand
                    case 3:
                        #update the quantity oh the product
                        print("Current name:", product["name"])
                        quantity = input("Enter the new quantity: ")
                        product["quantity"] = quantity
                    case _:
                        #invalid input handeling
                        print("Invalid input!")
                        print("You will will send back to main menu!")
                break
        #save the data in the file
        self.__saveProduct()
    
    #delete the product
    def deleteProduct(self):
        SKU = input("Enter the SKU of the product: ")
        #validate SKU
        if(self.checkIfProductExists(SKU) == False):
            print("Product doesn't exist!")
            return
        #remove the item from the all priduct list
        for product in self.__allProducts:
            if product["SKU"] == SKU:
                self.__allProducts.remove(product)
        #save product to file
        self.__saveProduct()