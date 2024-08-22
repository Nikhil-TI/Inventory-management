from Manager.product import Product

mainOptions = ("What do you want to do?", "1. Add a new product", "2. View products", "3. Update a product", "4. Delete a prodiuct")

def viewMainOptions():
    for option in mainOptions:
        print(option)
    selection = int(input("Enter your choice (1/2/3/4): "))
    return selection

def validateMainOptionSelection(selection):
    return not selection in range(1,5)

def performTask(selection):
    newProduct = Product()
    match selection:
        case 1: newProduct.addProduct()
        case 2: newProduct.viewProducts()
        case 3: newProduct.updateProduct()
        case 4: newProduct.deleteProduct()


def main():
    while(True):
        selection = viewMainOptions()
        if validateMainOptionSelection(selection):
           print("invalid input")
           print()
           continue
        performTask(selection)
        print()
        



if __name__ == "__main__":
    main()