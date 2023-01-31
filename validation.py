
def validate_add():
    while True:
        try:
            #use isalpha and isspace function to validate input only contain alphabet character and spaces
            #cannot be empty
            nama = input("Please enter your item: ")
            if not nama:
                raise ValueError
            elif not all(x.isalpha() or x.isspace() for x in nama):
                raise ValueError
        except ValueError:
            print("item must only contain alphabet or with spaces and can't be empty")
        else:
            break
    while True:
        try:
            #use convert int function to validate input only contain number
            quantity = int(input("Please enter quantity of the item: "))
            if type(quantity) != int:
                raise ValueError
            elif quantity < 0:
                raise TypeError
            else: 
                pass
        except* ValueError:
            print("item must only contain number and can't be empty")
        except* TypeError:
            print("Qty tidak boleh negatif atau 0!")
        else:
            break
    while True:
        try:
            #use convert int function to validate input only contain number
            price = int(input("Please enter the price of the item: "))
            if(price < 0):
                raise ValueError
        except* TypeError:
            print("item must only contain number and can't be empty")
        except* ValueError:
            print("Qty tidak boleh negatif atau 0!")
        else:
            break
    return nama, quantity, price

def validate_update_name():
    '''Validation method for update name
    '''
    while True:
        try:
            #use isalpha and isspace function to validate input only contain alphabet character and spaces
            update = input("enter name of the item you want to update: ")
            nama = input("enter new name item: ")
            if not all(x.isalpha() or x.isspace() for x in nama):
                raise TypeError
            else:
                pass
        except TypeError:
            print("Item must only contain alphabet and can't be empty")
        else:
            break
    return update, nama

def validate_update_qty():
    '''Validation method for update quantity
    '''
    while True:
        try:
            #use convert int function to validate input only contain number
            update = input("enter name of the item you want to update:")
            quantity = int(input("enter new quantity: "))
        except ValueError:
            print("item must only contain number and can't be empty")
            continue
        else:
            break
    
    return update, quantity

def validate_update_price():
    '''Validation method for update price
    '''
    while True:
        try:
            #use convert int function to validate input only contain number
            update = input("enter name of the item you want to update:")
            price = int(input("enter new price: "))
        except ValueError:
            print("item must only contain number and can't be empty")
            continue
        else:
            break
    return update, price