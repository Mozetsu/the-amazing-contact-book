import os
import time
import app

# database absolute path
CONTACTS_DATABASE = os.path.dirname(__file__) + "/database/contacts.txt"

# terminal colours setup
class Colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

# this is what we pass to every input() method in order to get the
# the same green arrow for each different interface
user_input_str = f"{Colors.GREEN}➜{Colors.END}  "

# returns the number of items in a list
def number_of_entries(list):
    return len(list)

# user call to action
def press_enter():
    input(f"\n{Colors.GREEN}Press ENTER to return... {Colors.END}")
    os.system("clear")
    return app.start()

# print contact details on the terminal
def print_contact_details(user):
    print("",)
    print(f"First name: {Colors.YELLOW}{user['first_name'].upper()}{Colors.END}")
    print(f"Surname: {Colors.YELLOW}{user['surname'].upper()}{Colors.END}")
    print(f"Email: {Colors.YELLOW}{user['email'].upper()}{Colors.END}")
    print(f"Phone number: {Colors.YELLOW}{user['phone_number'].upper()}{Colors.END}")
    print(f"Address: {Colors.YELLOW}{user['address'].upper()}{Colors.END}")

# Informs user that the input is not valid and
# returns to the presented user interface
def invalid_input(ui):
    os.system("clear")
    print(f"\n{Colors.RED}Invalid option, please try again...\n\n{Colors.END}")
    time.sleep(1.5)
    os.system("clear")
    return ui()
