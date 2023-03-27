#from Library import Library
from Settings import buttons, clear, colors, maxLoanedBooks
from Person import Person
from LoanItem import LoanItem
from BookItem import BookItem

class Member(Person):
    def __init__(self, library, number, givenName, surname, streetAddress, zipCode, city, emailAddress,username, password, telephoneNumber):
        Person.__init__(self, library, number, givenName, surname, streetAddress, zipCode, city, emailAddress, username, password, telephoneNumber)
        self.loaned : list[LoanItem] = []


    def loan_book_item(self, book):
        if not isinstance(book, BookItem):
            book = BookItem(book)
        self.loaned.append(LoanItem(book))
        self.library.delete_book_item(book)
        self.library.system_save_members()

    def turn_in_loan_item(self, loanedBook):
        self.loaned.remove(loanedBook)
        self.library.add_book_item(BookItem(loanedBook))
        self.library.system_save_members()


    def show_book_details(self,book, interface = "catalog", message = ""):
        clear()
        if message != "" : print(message)
        book.details()
        copies = self.library.amount_of_copies(book)
        print(f"{colors.WHITE}There are{colors.CYAN} {copies} {colors.WHITE}copies of this book in the library")
        print("")
        if copies: print(f"{colors.YELLOW}[{buttons.search}]{colors.WHITE} Loan a copy")
        else: print(f"{colors.GRAY} There are no copies, therefore you cant loan this book {colors.WHITE}")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back  {colors.GRAY}({interface}){colors.WHITE}")
        y = input("What will you do: ").upper()
        if y == buttons.search:
            if not copies:
                self.show_book_details(book,interface,f"{colors.RED}No copies left{colors.WHITE}")
            elif len(self.loaned) >= maxLoanedBooks:
                self.show_book_details(book,interface,f"{colors.RED}You are on the maximum loaned books{colors.WHITE}")
            else: 
                self.loan_book_item(book)
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


    #by defailt the maximum pages are 3, so pages are not needed at all.
    #they are only here because we already made them in for example the catalog, 
    # it was an easy coppy now it is really easy for a potential library manager to resise the amount of loanable books
    def check_loaned_books(self, page, message = f"{colors.YELLOW}Checking your loaned books"):
        clear() #clearing console to make it better to shee where the i
        print(f"{colors.GRAY}Page {page}{colors.WHITE} | {message}{colors.WHITE}")
        print(f"====================")
      
        booklist = self.loaned #getting the catalog booklist from the library
        print(f"{colors.GRAY}[{colors.WHITE}{len(booklist)}{colors.GRAY}/{colors.WHITE}{maxLoanedBooks}{colors.GRAY}]{colors.WHITE}") #[0/3]  # [ book you have loaned  /  max loanable ]
        if len(booklist): print(f"Enter one of the numbers to turn the book in\n")

        index = 1
        for book in booklist[page*9 : (page+1)*9]: #taking the part of the list thats supose to be displayed (from thispage untill the start of the next page)
            daysLeft = book.days_left()
            extraText = f"{colors.YELLOW}{daysLeft} days left"
            if daysLeft < 0:
                extraText = f"{colors.RED}{daysLeft} to late"
            print(f"{colors.YELLOW}[{index}]{colors.WHITE} {book} {colors.GRAY}| {extraText}{colors.WHITE}")
            index += 1
        
        print("")
        if len(booklist)-page*9 > 9: #if there are more books with a higher index then shown on the page
            print(f"{colors.YELLOW}[{buttons.next}]{colors.WHITE} To go to the next page")
        if page > 0: #if there are more books with a lower index then shown on the page
            print(f"{colors.YELLOW}[{buttons.previous}]{colors.WHITE} To go to the previous page")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")

        x = input("What will you do: ").upper()
        #check if the user pressed go back
        if x == buttons.goBack: 
            self.start()
        #check if the user pressed next
        elif x == buttons.next:
            if len(booklist)-page*9 > 9:
                self.check_loaned_books(page + 1)
            else:
                self.check_loaned_books(page, f"{colors.RED}There arent any pages after.")
        #check if the user pressed previous
        elif x == buttons.previous:
            if page > 0:
                self.check_loaned_books(page - 1)
            else:
                self.check_loaned_books(page, f"{colors.RED}There arent any pages before.")
        #if not, then its a invalied input
        elif x.isdigit() and int(x) < 10 and int(x) >= 0:
            if (int(x) - 1 + 9*page) < len(booklist):
                self.turn_in_loan_item(booklist[int(x) - 1 + 9*page])
                self.check_loaned_books(page)
            else: 
                self.check_loaned_books(page, f"{colors.RED}Invalid input, please try again.")

        else:
            self.check_loaned_books(page, f"{colors.RED}Invalid input, please try again.")


    def start(self, message = f"{colors.YELLOW}Home Page"):
        clear()
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        print(f"[1] Check Catalog")
        print(f"[2] Check Library")
        print(f"[3] Check Loaned Books\n")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Log Out")
        x = input("What will you do: ")
        if x == buttons.goBack: 
            self.library.run()
        elif x == "1":
            self.check_catalog(0)
        elif x == "2":
            self.check_library(0)
        elif x == "3":
            self.check_loaned_books(0)
        else:
            self.start(f"{colors.RED}Invalid input, please try again.")

