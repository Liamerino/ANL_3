#from Library import Library
from Settings import buttons, clear, colors
from Person import Person

class Member(Person):
    def __init__(self, library, number, givenName, surname, streetAddress, zipCode, city, emailAddress,username, password, telephoneNumber):
        Person.__init__(self, library, number, givenName, surname, streetAddress, zipCode, city, emailAddress,username, password, telephoneNumber)
        self.loaned = []

    def show_book_details(self,book, interface = "catalog", message = ""):
        clear()
        if message != "" : print(message)
        book.details()
        copies = self.library.amount_of_copies(book)
        print(f"{colors.WHITE}There are{colors.CYAN} {copies} {colors.WHITE} copies of this book in the library")
        print("")
        if copies: print(f"{colors.YELLOW}[{buttons.search}]{colors.WHITE} Loan a coppy")
        else: print(f"{colors.GRAY} There are no copies, therefore you cant loan this book {colors.WHITE}")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")
        y = input("What will you do: ").upper()
        if y == buttons.search:
            if not copies:
                self.show_book_details(book,interface,f"{colors.RED}No copies left{colors.WHITE}")
            elif len(self.loaned) >= 3:
                self.show_book_details(book,interface,f"{colors.RED}You are already on the maximum loaned items{colors.WHITE}")
            else: 
                self.library.loan_book_to(book, self)
                if interface == "library":
                    self.check_library(0)
                else: 
                    self.check_catalog(0)
        elif y == buttons.goBack:
            if interface == "library":
                self.check_library(0)
            else: 
                self.check_catalog(0)
        else: self.show_book_details(book,interface,f"{colors.RED}Invalid Input{colors.WHITE}")