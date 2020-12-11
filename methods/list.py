import os
import utils
import time
import app
import json

def list_contacts():
    os.system("clear")
    print("\nList contacts by\n")
    print("1. First name (Ascending)")
    print("2. First name (Descending)")
    print("3. Surname (Ascending)")
    print("4. Surname (Descending)\n")
    print("0. Return\n")

    # all the possible options a user can take
    available_options = {"0", "1", "2", "3", "4"}

    # get user input
    user_input = input(utils.user_input_str)

    # validate user input
    if user_input not in available_options:
        return utils.invalid_input(list_contacts)

    # convert user input into an integer
    user_input = int(user_input)

    # user wants to go back
    if user_input == 0:
        return app.start()

    os.system("clear")

    # temporary dictionary that stores all the
    # contacts contained in the text file
    users_dictionary = {}

    # open contacts text file (database)
    with open(utils.CONTACTS_DATABASE, "r") as f:
        # read first line in the database and store its content in a variable
        user_details = f.readline()

        # loop through all users stored in the file
        while user_details:
            # convert current user string into a dictionary
            user = json.loads(user_details)

            # append user to users dictionary
            if user_input == 1 or user_input == 2:
                users_dictionary[f"{user['first_name']}_{user['surname']}"] = user

            # append user to users dictionary
            if user_input == 3 or user_input == 4:
                users_dictionary[f"{user['surname']}_{user['first_name']}"] = user

            # get the next user
            user_details = f.readline()

        # close file after operation
        f.close()

    # sort contacts in ascending order
    if user_input == 1 or user_input == 3:
        for user in sorted(users_dictionary, reverse=False):
            utils.print_contact_details(users_dictionary[user])

    # sort contacts in descending order
    if user_input == 2 or user_input == 4:
        for user in sorted(users_dictionary, reverse=True):
            utils.print_contact_details(users_dictionary[user])

    # print number of existing contacts
    print(f"\nCONTACTS: {utils.number_of_entries(users_dictionary)}")

    # call to action
    utils.press_enter()
