#from Library import Library
from Settings import buttons, clear, colors
from Person import Person

class Admin(Person):
    def __init__(self, library, number, givenName, surname, streetAddress, zipCode, city, emailAddress,username, password, telephoneNumber):
        Person.__init__(self, library, number, givenName, surname, streetAddress, zipCode, city, emailAddress,username, password, telephoneNumber)


    def show_book_details(self,book,interface = "catalog", message = ""):
        clear()
        if message != "" : print(message)
        book.details()
        copies = self.library.amount_of_copies(book)
        print(f"{colors.WHITE}There are{colors.CYAN} {copies} {colors.WHITE}copies of this book in the library")
        print("")
        print(f"{colors.YELLOW}[{buttons.edit}]{colors.WHITE} Edit book")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back  {colors.GRAY}({interface}){colors.WHITE}")
        y = input("What will you do: ").upper()
        if y == buttons.goBack:
            if interface == "library":
                self.check_library(0)
            else: 
                self.check_catalog(0)
        elif y == buttons.edit:
            self.edit_book(book, interface)
        else: self.show_book_details(book,interface,f"{colors.RED}Invalid Input{colors.WHITE}")
    
    def edit_book(self, book, interface = "catalog", message = f"{colors.YELLOW}Editing book: "):
        clear()
        print(f"{message}{book}{colors.WHITE}")
        print(f"====================")
        #all parts that can be edited
        print(f"{colors.YELLOW}[{buttons.delete}]{colors.WHITE} Delete Book\n")
        editValues = [("1", "Author", book.author), 
                      ("2", "Publication country", book.country), 
                      ("3", "Image source", book.imageLink),
                      ("4", "Language", book.language), 
                      ("5", "Book source", book.link), 
                      ("6", "Amount of pages", book.pages),
                      ("7", "Title", book.title), 
                      ("8", "ISBN", book.ISBN), 
                      ("9", "Publication date", book.year)]
        for i in editValues:
            print(f"[{i[0]}] {i[1]}: {i[2]}")
        print("")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Stop editing")

        x = input("What will you do: ").upper()
        #check if the user pressed go back
        if x == buttons.goBack: 
            self.show_book_details(book,interface)
        #user chooses what value to edit
        elif x.isdigit():
            intX = int(x) - 1
            while True:
                clear()
                print(f"{message}{book}{colors.WHITE}")
                print(f"====================")
                print(f"Current {editValues[intX][1]}: {editValues[intX][2]}")
                newValue = input(f"New {editValues[intX][1]}: ")
                #if user needs to edit an integer they are forced to enter a whole number                
                if (x == "6" or x == "9") and not newValue.isdigit():
                    print(f"{colors.GRAY}You must enter a whole number to edit {editValues[intX][1]}")
                    input(f"Enter any key to try again{colors.WHITE}")
                    continue
                break

            if x == "1":
                book.author = newValue
            elif x == "2":
                book.country = newValue
            elif x == "3":
                book.imageLink = newValue
            elif x == "4":
                book.language = newValue
            elif x == "5":
                book.link = newValue
            elif x == "6":
                book.pages = newValue
            elif x == "7":
                book.title = newValue
            elif x == "8":
                book.ISBN = newValue
            elif x == "9":
                book.year = newValue
            self.library.sort_books(interface)
    
            self.edit_book(book, interface, f"{colors.YELLOW}{editValues[intX][1]} edited\nEditing book: ")
        elif x == buttons.delete:
            self.library.catalog.remove_book(book)
            if interface == "library":
                self.check_library(0)
            else: 
                self.check_catalog(0)
        else:
            self.edit_book(book,interface, f"{colors.RED}Invalid input, please try again\nEditing book: ")
    
    def check_members(self, page, message = f"{colors.YELLOW}Checking the list of members"):
        clear()
        print(f"{message}{colors.WHITE}")
        print(f"====================")

        memberList = self.library.members
        index = 1
        for member in memberList[page*9 : (page+1)*9]:
            print(f"[{index}] {member}")
            index += 1
        
        print("")
        if len(memberList)-page*9 > 9:
            print(f"{colors.YELLOW}[{buttons.next}]{colors.WHITE} To go to the next page")
        if page > 0:
            print(f"{colors.YELLOW}[{buttons.previous}]{colors.WHITE} To go to the previous page")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")

        x = input("What will you do: ").upper()
        #check if the user pressed go back
        if x == buttons.goBack: 
            self.start()
        #check if the user pressed next
        elif x == buttons.next:
            if len(memberList)-page*9 > 9:
                self.check_members(page + 1, f"{colors.YELLOW}Checking the list of members")
            else:
                self.check_members(page, f"{colors.RED}There arent any pages after.")
        #check if the user pressed previous
        elif x == buttons.previous:
            if page > 0:
                self.check_members(page - 1, f"{colors.YELLOW}Checking the list of members")
            else:
                self.check_members(page, f"{colors.RED}There aren't any pages before.")
        #check user details
        elif x.isdigit():
            clear()
            if (int(x) - 1 + 9*page) < len(memberList):
                memberList[int(x) - 1 + 9*page].details()
                input(f"\n{colors.GRAY}Enter anything to go back{colors.WHITE}")
                self.check_members(page)
            else:
                self.check_members(page, f"{colors.RED}Invalid input, please try again.")
        #invalid input by user
        else:
            self.check_members(page, f"{colors.RED}Invalid input, please try again.")
    
    def start(self, message = f"{colors.YELLOW}Home Page"):
        clear()
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        print(f"[1] Check Catalog")
        print(f"[2] Check Library")
        print(f"[3] Check members\n")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Log Out")
        x = input("What will you do: ")
        if x == buttons.goBack: 
            self.library.run()
        elif x == "1":
            self.check_catalog(0)
        elif x == "2":
            self.check_library(0)
        elif x == "3":
            self.check_members(0)
        else:
            self.start(f"{colors.RED}Invalid input, please try again.")