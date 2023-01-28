
#Import library yang dipakai dalam cashier.py
from tabulate import tabulate
import validation

class Transaction:
    '''Create a class and method for transaction

        Parameters:
        ===========
        data: dictionary
            contain list of name item, quantity and item price
    '''
    data = {}

    def __init__(self):
        self.items = {}

    def add_item(self):
        '''Create add item method for user add new item to the transaction and use try except to validate user input inside a while loop.
        It will stop when all of the input is correct and add the data to __init__ items.
        '''
        name, quantity, item_price = validation.validate_add()      
        self.items[name] = {"quantity": quantity, "item_price": item_price, "total_item_price": quantity * item_price}

    def delete_item(self):
        '''Create delete item method based on name item that already exists and use try except to validate if there is no matching data.
        '''
        name = input("Enter name item you want delete: ")
        try:
            del self.items[name]
            print("delete success!")
        except KeyError:
            print(f"There is item no {name} in the bucket")
        
    def reset_item(self):
        '''Create reset item method to clear all the data item and use try except to validate if there is no data 
        '''
        try:
            if(len(self.items) != 0):
                print("Clearing all item")
                self.items.clear()
                print("All item success deleted!")
            else:    
                raise ValueError
        except ValueError:
            print("There is no item to be deleted")

    def update_item_name(self):
        '''Create update name item method based on the existing name item in the transaction and use validation input to prevent ambiguity item.
        Use try except to validate if there is no item according to the input user and validate input when there is no item in the transaction
        '''
        if(len(self.items) != 0):
            try:
                old_name, new_name = validation.validate_update_name()
                if old_name in self.items:
                    self.items[new_name] = self.items.pop(old_name)
                else: 
                    raise ValueError
            except ValueError:
                print(f"There is no item name {old_name} the transaction")
        else:
            print("Please add item first")
    
    def update_item_qty(self):
        '''Create update quantity item method based on the existing name item in the transaction and use validation input to prevent ambiguity item.
        Use try except to validate if there is no item according to the input user and validate input when there is no item in the transaction.
        If all input correct it will auto calculate total item price
        ''' 
        if(len(self.items) != 0):
            try:
                name, quantity = validation.validate_update_qty()
                if name in self.items:
                    self.items[name]['quantity'] = quantity
                    self.items[name]['total_item_price'] = quantity * self.items[name]['item_price']
                else:
                    raise ValueError
            except ValueError:
                print("No item on the transaction")
        else:
            print("Please add item first")

    def update_item_price(self):
        '''Create update price item method based on the existing name item in the transaction and use validation input to prevent ambiguity item.
        Use try except to validate if there is no item according to the input user and validate input when there is no item in the transaction.
        If all input correct it will auto calculate total item price
        ''' 
        if(len(self.items) != 0):
            try:
                name, price = validation.validate_update_price()
                if name in self.items:
                    self.items[name]['item_price'] = price
                    self.items[name]['total_item_price'] = price * self.items[name]['quantity']
                else:
                    raise ValueError
            except ValueError:
                print("No item on the transaction")
        else:
            print("please add item first")

    def total_price(self):
        '''Create calculate total price method for all of the item and will got discount if the total price meet the term and condition of discount.
        It will print the price before and after, if there is no items it will print no item to be calculate.
        '''
        total_price = 0
        discount = 0
        if(len(self.items) != 0):
            for keys, _ in self.items.items():
                total_price += int(self.items[keys]["total_item_price"])
            
            if total_price > 200_000 and total_price <= 300_000:
                discount = int(0.05 * total_price)
            elif total_price > 300_000 and total_price <= 500_000:
                discount = int(0.08 * total_price)
            elif total_price > 500_000:
                discount = int(0.1 * total_price)
            else:
                pass
            self.check_order()
            print(f"Your price before discount {total_price}, you got discount {discount} and total price is {total_price - discount}")
        else:
            print('No item to calculate the price')

    
    def check_order(self):
        '''Create a table to show all of the items input by the user and it will print no items if the data is empty. Using tabulate module
        so the display tidier.
        ''' 
        item_to_attribute = {}
        list_item = []

        for keys_1, keys_2 in self.items.items():
            item_to_attribute['product name'] = keys_1
            item_to_attribute['quantity'] = keys_2['quantity']
            item_to_attribute['item_price'] = keys_2['item_price']
            item_to_attribute['total_item_price'] = keys_2['total_item_price']

            #need to append a copy, otherwise it just adding references to the same dictionary over and over again
            list_item.append(item_to_attribute.copy())

        if(len(list_item) != 0):
            print('=' * 10,"List of items in this transaction",'=' * 10)
            print(tabulate(list_item,headers="keys", tablefmt="simple_grid"))
        else:
            print("There is no items in the bucket")