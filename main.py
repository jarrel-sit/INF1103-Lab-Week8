from Product import Product
from Inventory import Inventory
import os,json

def main():
    menu()



#Menu Display and User Input    
def menu():
    while True:
        print('\tMenu\n=======================\n1. Display all products\n2. Add a product\n3. Update Stock\n4. Search for a product\n5. Save Inventory\n6. Exit\n=======================')
        option = int(input('> '))
        match(option):
            case 1:
                if not inventory:
                    print('Inventory is empty!')
                else:
                    inventory.display_all()
            case 2:
                    name = input('Name:')
                    itemid = input('ID: ')
                    price = input('Price ')
                    stock = input('Stock: ') 
                    item = Product(name, itemid, price, stock)
                    inventory.add_product(item)
            case 3:
                break
            case 4:
                searchid = input("Please enter the Product ID of the product you are looking for.")
                inventory.search_product(searchid)
            case 5:
                break
            case 6:
                #inventory.save_inventory()
                print('Records saved, exiting the program...')
                break
            case _:
                print('Invalid Response, please input a value 1-6.')
            


if __name__ == "__main__":
    inventory = Inventory()
    main()
