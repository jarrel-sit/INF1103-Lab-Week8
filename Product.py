#Creating Products (Blueprint)
class Product:
    def __init__ (self, name, id, price, stock):
        self.name = name
        self.id = id
        self.price = price
        self.stock = stock

    #Displays the information
    def display_information(self):
        print(f'Product Name: {self.name}\nProduct ID: {self.id}\nPrice: {self.price}\nStock: {self.stock}')

name = input('Name:')
id = input('ID: ')
price = input('Price ')
stock = input('Stock: ') 

product = Product(name, id, price, stock)
product.display_information()