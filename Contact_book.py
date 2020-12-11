import os
import sys
from methods.add import add_contact
from methods.search import search_contact
from methods.list import list_contacts

class Contact_book(object):

    # contact book available options
    options = {
        0: "exit_app",
        1: "add_contact",
        2: "search_contact",
        3: "list_contacts"
    }

    # setup contact book methods
    def __init__(self):
        self.add_contact = add_contact
        self.search_contact = search_contact
        self.list_contacts = list_contacts


    def dynamic_call(self, method_name):
        """
        This function is used to dinamically select a method from
        the contact book class. This is used in the main menu where
        we do not know which option the user will select.
        """
        return getattr(self, method_name)()


    # close appplication
    def exit_app(self):
        os.system("clear")
        return sys.exit()
