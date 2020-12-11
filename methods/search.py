import os
import utils
import time
import app
import json

def search_contact():
    os.system("clear")
    print("\nSearch contact by\n")
    print("1. First name")
    print("2. Email address\n")
    print("0. Return\n")

    # all the possible options a user can take
    available_options = {"0", "1", "2"}

    # get user input
    user_input = input(utils.user_input_str).lower()

    # validate user input
    if user_input not in available_options:
        return utils.invalid_input(search_contact)

    # convert user input into an integer
    user_input = int(user_input)

    # user wants to go back
    if user_input == 0:
        return app.start()

    # user wants to search by first name
    if user_input == 1:
        os.system("clear")
        print("\nEnter contact's first name\n")
        print("0. Return\n")
        search_query = "first_name"
        user_input = input(utils.user_input_str)

        # user wants to go back
        if user_input == "0":
            return search_contact()

    # user wants to search by email address
    if user_input == 2:
        os.system("clear")
        print("\nEnter contact's email\n")
        print("0. Return\n")
        search_query = "email"
        user_input = input(utils.user_input_str)

        # user wants to go back
        if user_input == "0":
            return search_contact()

    # search user in database
    with open(utils.CONTACTS_DATABASE, "r") as f:
        os.system("clear")

        # read first line in the database and store its content in a variable
        user_details = f.readline()

        # loop through all users
        while user_details:
            # convert current user data into a dictionary
            user = json.loads(user_details)

            # check if user matches search query
            if user_input == user[search_query]:
                utils.print_contact_details(user)

            # get the next user
            user_details = f.readline()

        # close file
        f.close()

        # call to action
        utils.press_enter()
