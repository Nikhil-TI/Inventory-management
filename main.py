from Manager.product import Product

#Main menu options
mainOptions = ("What do you want to do?", "1. Add a new product", "2. View products", "3. Update a product", "4. Delete a prodiuct")

def viewMainOptions():
    for option in mainOptions:
        print(option)
    selection = int(input("Enter your choice (1/2/3/4): "))
    return selection


#check if options are valid or not
def validateMainOptionSelection(selection):
    return not selection in range(1,5)

#call the correcponding task from the Product Object
def performTask(selection):
    #Creating a new product ibject
    newProduct = Product()
    match selection:
        case 1: newProduct.addProduct()
        case 2: newProduct.viewProducts()
        case 3: newProduct.updateProduct()
        case 4: newProduct.deleteProduct()


def main():
    #keep asking the user for tasks to be done
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