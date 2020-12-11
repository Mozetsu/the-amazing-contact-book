import os
import utils
from Contact_book import Contact_book

# instantiate contact book object
contact_book = Contact_book()

# main menu user interface
def start():
    os.system("clear")
    print(f"\n⚡ {utils.Colors.PINK}The Amazing Contact Book{utils.Colors.END} ⚡\n")
    print("1. Add new contact")
    print("2. Search contact")
    print("3. List all contacts")
    print("\n0. Exit\n")

    # all the possible options a user can select
    available_options = {"0", "1", "2", "3"}

    # get user input
    user_input = input(utils.user_input_str)

    # validate user input
    if user_input not in available_options:
        utils.invalid_input(start)

    # convert user input to an integer
    user_input = int(user_input)

    # select desired behaviour from contact book
    book_method = contact_book.options[user_input]

    # execute selected method
    return contact_book.dynamic_call(book_method)