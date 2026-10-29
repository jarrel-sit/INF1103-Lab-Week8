from Product import Product


class Inventory:
    def __init__(self):
        self.inventory = []

    #Adds Product Object into existing inventory
    def add_product(self, product):
        self.inventory.append(product)

    #Displays all product Objects in the inventory by printing them to terminal
    def display_all(self):
        for item in self.inventory:
            print(item)

    def search_product(self,searchid):
        for product in self.inventory:
            if searchid == product.itemid:
                print(product)
            else:
                print("Unable to find product, ensure that you have entered product ID in the correct format.")




product = Product       

