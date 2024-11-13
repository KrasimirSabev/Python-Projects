from Transaction import Transaction
from Table import Table
from Customer import Customer
from datetime import datetime

'''
1) Maybe a future implementation would be to ask the guest at what future date they would like to book.
2) There isn't a limit to how many bookings can be made. 
3) Customer ID is yet to be worked on. Core idea: customer_list should collect the data and store it in tuples of guests. Collect the first, last names, and the account number from the customer list and create a copy of the list with that tuple. Then convert the tuple into a hash value and print it for the customer to see. By entering the hash value they will be able to see whether they have an existing booking or not. Maybe will use the same method for cancelling a reservation? 
'''



customer_list = []
today = datetime.now()
current_time = today.strftime("%A %d %B %Y, %I:%M%p")

table_management = Table()


#the motherwell
def main_menu():
    welcome = input('Welcome to tablebooking.com! If you wish to book a table please type "yes". If you wish to exit, please type "exit".\n')
    if welcome.lower() == 'yes':
        while True:
            choice=get_main_menu_choice()
            if choice==1:
                reserve_table()
            elif choice==2:
                check_reservation()
            elif choice==3:
                cancel_reservation()
            elif choice==4:
                display_contact_details()
            else:
                print('Invalid choice. Please try again.')


def get_main_menu_choice():
    return int(input('Please select one of the following by typing the correct number: \n'
                     '1) If you would like to reserve a table.\n'
                     '2) If you would like to check an already existing reservation.\n'
                     '3) If you would like to cancel an existing reservation.\n'
                     '4) If you would like our contact details.\n'))

#making a reservation
def reserve_table():
    first_name=input('Please provide your first name.\n')
    last_name=input('Please provide your last name.\n')
    guest_age = int(input('Please provide your age.\n'))
    if guest_age < 18:
        print('Sorry, you are not old enough to make a booking.')
        return
# still haven't figured out the customer ID part.
    guest=Customer(1, first_name, last_name, guest_age)
    guest.set_fname(first_name)
    guest.set_lname(last_name)
    guest.set_age(guest_age)

    #allocating a table
    customer_table = int(input(f'Thank you {guest.get_fname()}. Would you like to book a table for {1} or a table for {2} people?\n'))
    if customer_table in [1,2]:
        if table_management.available_table(customer_table): #checks availability
            if customer_table==1:
                book_table_of_one(guest)
            elif customer_table==2:
                book_table_of_two(guest) #should subtract 2 from the available tables
    else:
        print('Unfortunately, we can only accommodate up to 2 people. If you still wish to book for 1 or 2 people, you can start over.')

def book_table_of_one(guest):
    print('Certainly! We have a table of 1 available.')
    guest_acc_num=int(input('If you wish to proceed please provide your account number.\n'))
    guest_s_code=int(input('Please provide your sort code.\n')) #it would be great if I figure out how to accommodate for dashes and numbers; potentially in the future?
    guest_bank_details = Transaction(guest_acc_num, guest_s_code)
    guest_bank_details.payment(40,10)
    print(f'The total will be {guest_bank_details.get_price()} pounds.')
    final_for_one = input('If you are happy with the price bellow please type "y".\n')
    if final_for_one.lower() == 'y':
        print(f'Thank you for making a reservation with us. Your booking was made on {current_time}.\n')
    customer_list.append(guest)



def book_table_of_two(guest):
    print('Certainly! We have a table of 2 available.\n')
    guest_acc_num = int(input('If you wish to proceed please provide your account number.\n'))
    guest_s_code = int(input(
        'Please provide your sort code.\n')) # it would be great if I figure out how to accommodate for dashes and numbers; potentially in the future?
    guest_bank_details = Transaction(guest_acc_num, guest_s_code)
    guest_bank_details.payment(80, 10)
    print(f'The total will be {guest_bank_details.get_price()} pounds.')
    final_for_two = input('If you are happy with the price bellow please type "y".\n')
    if final_for_two.lower()=='y':
        print(f'Thank you for making a reservation with us. Your booking was made on {current_time}\n')
    customer_list.append(guest)

def check_reservation():
    check_customer_id = input('Please provide your Customer ID.\n')


def cancel_reservation():
    pass

def display_contact_details():
    print('Contact us at tablebooking.com or call us at (012) 345 678. Have a good day!')

if __name__=='__main__':
    main_menu()
print(customer_list)

'''
        for guests in customer_list:
            print(guests.get_fname())
            print(guests.get_lname())
            print(guests.get.customer_age())
'''