import os
import time
import json
import app
import utils

def add_contact():
        os.system("clear")

        # create temporary dictionary to store user details
        user_details = {}

        # get contact details
        user_details["first_name"] = input("First name: ").lower()
        user_details["surname"] = input("Surname: ").lower()
        user_details["email"] = input("Email: ").lower()
        user_details["phone_number"] = input("Phone number: ")
        user_details["address"] = input("Address: ").lower()

        # write details to file
        with open(utils.CONTACTS_DATABASE, "a+") as f:
            os.system("clear")

            # convert dictionary to JSON
            f.write(json.dumps(user_details) + "\n")

            # close file
            f.close()

            # inform user of success
            print(f"\n\n{utils.Colors.GREEN}Contact added successfully!{utils.Colors.END}\n\n")
            time.sleep(1.5)

            # return to main menu
            os.system("clear")
            return app.start()
