#Creating Products (Blueprint)
class Product:
    def __init__ (self, name, itemid, price, stock):
        self.name = name
        self.itemid = itemid
        self.price = price
        self.stock = stock
        self.iteminfo = (self.name,self.price,self.stock)

    #Displays the information
    def __str__(self):
        return f"{self.itemid}: {self.iteminfo} "

# name = input('Name:')
# itemid = input('ID: ')
# price = input('Price ')
# stock = input('Stock: ') 

# product = Product(name, itemid, price, stock)
# print(product.name)
# product.itemid
# product.price
# product.stock

#product.display_information()