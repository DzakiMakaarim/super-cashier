'''You have to run main.py using command python main.py in the terminal and it will run the program without need to run
validation module and cashier module
'''

#import modul yang akan digunakan
import uuid
import cashier

trnsct_123 = cashier.Transaction()

def random_trnsct_id(string_length=10):
    '''create a unique transaction id every time menu is started. Generate random id using UUID
    module with a length maximum is 10 character and it has mix character and number
    '''
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]

id_transaction = random_trnsct_id()

def main_menu():
    '''create menu for user and use every method in object trnsct_123 
    '''
    print()
    print("=" * 10, "MAIN MENU CASHIER", "=" * 18)
    print(" " * 7, "WELCOME TO SUPER CASHIER\n")
    print("=" * 3 ,f"Your transaction id is {id_transaction}", "=" * 3, "\n")
    print("=" * 5, "Please enter one of the option", "=" * 10)
    print("1. Add new item")
    print("2. Update item name")
    print("3. Update item quantity")
    print("4. Update item price")
    print("5. Delete item")
    print("6. Reset transaction")
    print("7. Check order")
    print("8. Check total price")
    print("9. Exit")
    
    while True:
        # input pilihan
        try:
            pilihan = input("Choose menu: ")

            # pilihan menu
            if pilihan == '1':
                trnsct_123.add_item()
                main_menu()
            elif pilihan == '2':
                trnsct_123.update_item_name()
                main_menu()
            elif pilihan == '3':
                trnsct_123.update_item_qty()
                main_menu()
            elif pilihan == '4':
                trnsct_123.update_item_price()
                main_menu()
            elif pilihan == '5':
                trnsct_123.delete_item()
                main_menu()
            elif pilihan == '6':
                trnsct_123.reset_item()
                main_menu()
            elif pilihan == '7':
                trnsct_123.check_order()
                main_menu()
            elif pilihan == '8':
                trnsct_123.total_price()
                main_menu()
            elif pilihan == '9':
                print("Program exit")
                exit()
            else:
                raise ValueError
        except ValueError:
            print("Input according to menu")

main_menu()