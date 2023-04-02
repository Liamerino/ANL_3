from Library import Library
from Book import Book
from Settings import buttons, clear, colors, maxLoanedBooks
from Person import Person
from Member import Member
import os

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
        print(f"{colors.BLUE}[{buttons.search}]{colors.WHITE} Lend book")
        print(f"{colors.YELLOW}[{buttons.edit}]{colors.WHITE} Edit book")
        print(f"{colors.GREEN}[{buttons.next}]{colors.WHITE} Add copies to library")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back  {colors.GRAY}({interface}){colors.WHITE}")
        y = input("What will you do: ").upper()
        if y == buttons.goBack:
            if interface == "library":
                self.check_library(0)
            else: 
                self.check_catalog(0)
        elif y == buttons.edit:
            self.edit_book(book, interface)
        elif y == buttons.next:
            self.add_copies(book, interface)
        elif y == buttons.search:
            self.lend_book_item(book, interface)
        else: self.show_book_details(book,interface,f"{colors.RED}Invalid Input{colors.WHITE}")
    
    def lend_book_item(self, book, interface, message = f"{colors.YELLOW}Lending ", memberList = []):
        clear()
        print(f"{message}{colors.CYAN}{book}{colors.WHITE}")
        print(f"====================")
        print(f"{colors.YELLOW}[{buttons.search}]{colors.WHITE} Search for a member to lend book to\n")
        if memberList != []:
            print(f"{colors.WHITE}Choose member to lend {colors.CYAN}{book}{colors.WHITE} to")
            for i in range(len(memberList)): 
                if isinstance(memberList[i],Member):
                    alreadyHave = book in memberList[i].loaned
                    extra =""
                    if alreadyHave:
                        extra = f"{colors.RED} already loaned this book"
                    print(f"[{i+1}] {memberList[i]} {colors.GRAY}[{len(memberList[i].loaned)}/{maxLoanedBooks}] {extra}{colors.WHITE}")
        print("")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")
        
        x = input("What will you do: ").upper()
        if x == buttons.goBack:
            self.show_book_details(book, interface)
        elif x == buttons.search:
            clear()
            print(f"{colors.BLUE}Search for a member with username, member ID or last name{colors.WHITE}\n")
            members = self.library.find_members(input())
            if members == []:
                self.lend_book_item(book, interface, f"{colors.RED}No members found with that searchterm\n{colors.YELLOW}Lending ")
            else:
                self.lend_book_item(book, interface, f"{colors.CYAN}{len(members)}{colors.GREEN} members found\n{colors.YELLOW}Lending ", members)
        elif x.isdigit():
            x = int(x) - 1
            if x >= 0 and x < len(memberList):
                member = memberList[x]
                if not isinstance(member, Member):
                    self.show_book_details(book, interface, f"{colors.RED}something went wront trying to loan to {colors.CYAN}{member}{colors.WHITE}")
                elif book in member.loaned:
                    self.show_book_details(book, interface, f"{colors.CYAN}{member}{colors.RED} already loaned this book {colors.WHITE}")
                else: 
                    member.loan_book_item(book)
                    self.show_book_details(book, interface, f"{colors.CYAN}{book}{colors.GREEN} successfully lent to {colors.CYAN}{member}{colors.WHITE}")
            else:
                self.lend_book_item(book, interface, f"{colors.RED}Invalid input, please try again\n{colors.YELLOW}Lending ")
        else:
            self.lend_book_item(book, interface, f"{colors.RED}Invalid input, please try again\n{colors.YELLOW}Lending ")


    def edit_book(self, book, interface = "catalog", message = f"{colors.YELLOW}Editing book: "):
        clear()
        print(f"{message}{book}{colors.WHITE}")
        print(f"====================")
        #all parts that can be edited
        if interface == "catalog": print(f"{colors.YELLOW}[{buttons.delete}]{colors.WHITE} Delete Book\n")
        else: print(f"{colors.YELLOW}[{buttons.delete}]{colors.WHITE} Delete Copy of Book\n")
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
            if interface == "library":
                self.library.delete_book_item(book)
                #the library delete function autmaticly saves the file
                self.check_library(0)
            else: 
                self.library.catalog.remove_book(book)
                self.library.system_save_catalog()
                self.check_catalog(0)
        else:
            self.edit_book(book,interface, f"{colors.RED}Invalid input, please try again\nEditing book: ")
    

    def show_member_details(self, member, page=0, message = ""):
        clear()
        if message != "" : print(message)
        member.details()
        print("")
        print(f"{colors.GREEN}[{buttons.edit}]{colors.WHITE} Edit member\n{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")

        x = input("What will you do: ").upper()
        if x == buttons.goBack:
            self.check_members(page)
        elif x == buttons.edit:
            self.edit_member(member, page)
        else:
            self.show_member_details(member, page, f"{colors.RED}Invalid input, please try again.{colors.WHITE}")

    def edit_member(self, member, page=0, message = f"{colors.WHITE}Editing: "):
        clear()
        print(f"{message}{colors.YELLOW}{member}{colors.WHITE}")
        print(f"====================")
        print(f"{colors.YELLOW}[{buttons.delete}]{colors.WHITE} Delete member\n")
        valueList = [("User ID", member.number), ("First name", member.givenName),
                    ("Last name", member.surname), ("Street address", member.streetAddress),
                    ("Zip code", member.zipCode), ("City", member.city),
                    ("Email address", member.emailAddress), ("Username", member.username),
                    ("Password", self.password), ("Phone number", member.telephoneNumber)]
        for i in range(len(valueList)):
            if i == 9:
                print(f"[S] {valueList[i][0]}: {valueList[i][1]}")
            else:
                print(f"[{i+1}] {valueList[i][0]}: {valueList[i][1]}")
        print(f"\n{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")

        x = input("What will you do: ").upper()
        if x == buttons.goBack:
            self.show_member_details(member, page)
        elif x == buttons.delete:
            self.library.delete_member(member)
            self.check_members(page, f"{colors.GREEN}Member successfully deleted.{colors.YELLOW}\nChecking the list of members{colors.WHITE}") 
        elif x.isdigit():
            x = int(x) - 1
            if x >= 0 and x <= 9:
                self.edit_member_value(member, page, valueList[x][0], valueList[x][1])
            else:
                self.edit_member(member, page, f"{colors.RED}Invalid input, please try again.\n{colors.YELLOW}Editing member: ")
        else:
            self.edit_member(member, page, f"{colors.RED}Invalid input, please try again.\n{colors.YELLOW}Editing member: ")
    
    def edit_member_value(self, member, page, valueType, value):
        clear()
        print(f"{colors.YELLOW}Editing: {member}{colors.WHITE}")
        print(f"====================")
        print(f"{colors.BLUE}Current {valueType}: {value}{colors.WHITE}")
        newValue = input(f"New {valueType}: ")
        if valueType == "User ID": member.number = newValue
        elif valueType == "First name": member.givenName = newValue
        elif valueType == "Last name": member.surname = newValue
        elif valueType == "Street address": member.streetAddress = newValue
        elif valueType == "Zip code": member.zipCode = newValue
        elif valueType == "City": member.city = newValue
        elif valueType == "Email address": member.emailAddress = newValue
        elif valueType == "Username": member.username = newValue
        elif valueType == "Password": member.password = newValue
        elif valueType == "Phone number": member.telephoneNumber = newValue
        self.library.system_save_members()
        self.edit_member(member, page, f"{colors.GREEN}{valueType} successfully edited\n{colors.YELLOW}Editing member: ")

    
    def check_members(self, page, message = f"{colors.YELLOW}Viewing the list of members"):
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
                self.check_members(page + 1, f"{colors.YELLOW}Viewing the list of members")
            else:
                self.check_members(page, f"{colors.RED}There arent any pages after.")
        #check if the user pressed previous
        elif x == buttons.previous:
            if page > 0:
                self.check_members(page - 1, f"{colors.YELLOW}Viewing the list of members")
            else:
                self.check_members(page, f"{colors.RED}There aren't any pages before.")
        #check user details
        elif x.isdigit():
            if (int(x) - 1 + 9*page) < len(memberList):
                self.show_member_details(memberList[int(x) - 1 + 9*page], page)
            self.check_members(page, f"{colors.RED}Invalid input, please try again.")
        #invalid input by user
        else:
            self.check_members(page, f"{colors.RED}Invalid input, please try again.")
    
    def add_member(self, message = f"{colors.YELLOW}Adding member(s)"):
        clear()
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        print(f"[1] Add a member manually\n[2] Load a list of members\n")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")

        x = input("What will you do: ").upper()
        if x == buttons.goBack:
            self.start()
        elif x == "1":
            self.add_member_manually()
        elif x =="2":
            self.add_list_members()
        else:
            self.add_member(message = f"{colors.RED}Invalid input, please try again\n{colors.YELLOW}Adding member(s){colors.WHITE}")

    def add_member_manually(self, memberValues = None, message = f"{colors.YELLOW}Adding member manually"):
        clear()
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        if memberValues == None:
            valueList = ["User ID", "First name", "Last name", "Street address",
                         "Zip code", "City", "Email address",
                         "Username", "Password", "Phone number"]
            memberValues = {i: (value, None) for (i, value) in zip(range(1, 11), valueList)}
            memberValues[1] = (memberValues[1][0], self.library.get_user_id())
        for i, value in memberValues.items():
            if value[i][1] == None:
                if i == 10:
                    print(f"[S] {value[0]}: {colors.RED}{value[1]}{colors.WHITE}")
                else: 
                    print(f"[{i}] {value[0]}: {colors.RED}{value[1]}{colors.WHITE}")
            elif i == 10:
                print(f"[s] {value[0]}: {value[1]}")
            else:
                print(f"[{i}] {value[0]}: {value[1]}")
        print("")
        if None not in [x[1] for x in memberValues.values()]:
            print(f"{colors.GREEN}[{buttons.next}]{colors.WHITE} Add member to library")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")

        x = input("What will you do: ").upper()
        if x == buttons.goBack:
            self.add_member()
        elif x.isdigit(): 
            if int(x) in memberValues.keys():
                clear()
                x = int(x)
                memberValues[x] = (memberValues[x][0], input(f"{colors.WHITE}Editing {colors.BLUE}{memberValues[x][0]}{colors.WHITE}\n"))
                self.add_member_manually(memberValues, message = f"{colors.BLUE}{memberValues[x][0]}{colors.WHITE} edited\n{colors.YELLOW}Adding member manually{colors.WHITE}")
        elif x == buttons.next and None not in [x[1] for x in memberValues.values()]:
            self.library.add_member(memberValues[1][1], memberValues[2][1], memberValues[3][1],
                                    memberValues[4][1], memberValues[5][1], memberValues[6][1],
                                    memberValues[7][1], memberValues[8][1], memberValues[9][1], memberValues[10][1])
            self.add_member(message = f"{colors.GREEN}Member successfully added\n{colors.YELLOW}Adding member(s){colors.WHITE}")
        else:
            self.add_member_manually(memberValues, message = f"{colors.RED}Invalid input, please try again\n{colors.YELLOW}Adding member manually")

    def add_list_members(self, message = f"{colors.YELLOW}Adding list of members with CSV{colors.WHITE}"):
        clear()
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        #print(f"[1] Use standard directory at path {colors.CYAN}{get_path()}\n{colors.WHITE}[2] Provide a path to file\n")
        print(f"Provide a full path to file\n")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")

        x = input("Enter the path or 0: ").upper()
        if x == buttons.goBack:
            self.add_member()
        elif os.path.exists(x):
            print()
            self.library.load_members(x)
            input(f"{colors.GRAY}Enter anything to go back {colors.WHITE}")
            self.add_member()
        else:
            self.add_list_members(f"{colors.RED}Invalid input, please try again\n{colors.YELLOW}Adding list of books with CSV")


    def add_book(self, message = f"{colors.YELLOW}Adding book"):
        clear()
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        print(f"[1] Add a book manually\n[2] Load a list of books\n")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back to home page")
                   
        x = input("What will you do: ").upper()
        #check if the user pressed go back
        if x == buttons.goBack:
            self.start()
        #adding a book manually
        elif x == "1":
            self.add_book_manually()
        elif x == "2":
            self.add_list_books()
        else:
            self.add_book(message = f"{colors.RED}Invalid input, please try again\n{colors.YELLOW}Adding book{colors.WHITE}")
    

    def add_list_books(self, message = f"Adding list of books with JSON"):
        clear()
        print(f"{colors.YELLOW}{message}{colors.WHITE}")
        print(f"====================")
        #print(f"[1] Use standard directory at path {colors.CYAN}{os.path.dirname(__file__)}{colors.WHITE}")
        print(f"Provide a full path to file\n")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")

        x = input("Enter the path or 0: ").upper()
        if x == buttons.goBack:
            self.add_book()
        elif os.path.exists(x):
            print()
            self.library.load_books(x)
            input(f"{colors.GRAY}Enter anything to go back {colors.WHITE}")
            self.add_book()
        else:
            self.add_list_books(f"{colors.RED}Invalid input, please try again\n{colors.YELLOW}Adding list of books with JSON")

    def add_book_manually(self, bookValues = None, message = f"Adding book manually"):
        clear()
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        if bookValues == None:
            nameList = ["Author", "Publication country", "Image source",
                        "Language", "Book source", "Amount of pages",
                        "Title", "ISBN", "Publication date"]
            bookValues = {i: (name, None) for (i, name) in zip(range(1, 10), nameList)}
        for i, value in bookValues.items():
            if value[1] == None:
                print(f"[{i}] {value[0]}: {colors.RED}{value[1]}{colors.WHITE}")
            else:
                print(f"[{i}] {value[0]}: {value[1]}")
        print("")
        if None not in [x[1] for x in bookValues.values()]:
            print(f"{colors.GREEN}[{buttons.next}]{colors.WHITE} Add book to catalog")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")

        x = input("What will you do: ").upper()
        if x == buttons.goBack:
            self.add_book()
        elif x == "6" or x == "9":
            clear()
            x = int(x)
            newValue = input(f"{colors.WHITE}Editing {colors.BLUE}{bookValues[x][0]}{colors.WHITE}\n")
            if not newValue.isdigit():
                self.add_book_manually(bookValues, f"{colors.RED}Invalid input, please try again.\n{colors.WHITE}Adding book manually")
            else:
                bookValues[x] = (bookValues[x][0], newValue)
                self.add_book_manually(bookValues, f"{colors.BLUE}{bookValues[x][0]}{colors.WHITE} edited\nAdding book manually")
        elif x.isdigit():
            if int(x) in bookValues.keys():
                clear()
                x = int(x)
                bookValues[x] = (bookValues[x][0], input(f"{colors.WHITE}Editing {colors.BLUE}{bookValues[x][0]}{colors.WHITE}\n"))
                self.add_book_manually(bookValues, f"{colors.BLUE}{bookValues[x][0]}{colors.WHITE} edited\nAdding book manually")
        elif x == buttons.next and None not in [x[1] for x in bookValues.values()]:
            self.library.catalog.add_book(Book(bookValues[1][1], bookValues[2][1], bookValues[3][1],
                                               bookValues[4][1], bookValues[5][1], bookValues[6][1],
                                               bookValues[7][1], bookValues[8][1], bookValues[9][1]))
            self.library.sort_books("catalog")
            self.add_book(f"{colors.GREEN}Book: {bookValues[7][1]} has been added")
        else:
            self.add_book_manually(bookValues, f"{colors.RED}Invalid input, please try again.\n{colors.WHITE}Adding book manually")
        
    def add_copies(self, book, interface, message = f"Adding copies of "):
        clear()
        print(f"{colors.YELLOW}{message}{book}{colors.WHITE}")
        print(f"====================")
        print(f"{colors.BLUE}How many copies would you like to add. Please enter the amount")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back\n")
        
        x = input("What will you do: ").upper()
        if x == buttons.goBack:
            self.show_book_details(book, interface)
        elif x.isdigit():
            for i in range(int(x)):
                self.library.add_book_item(book)
            self.show_book_details(book, interface, f"{colors.YELLOW}{x} copies of {book} added{colors.WHITE}")
        else:
            self.add_copies(book, interface, f"{colors.RED}Invalid input, please try again.{colors.WHITE}\n Adding copies of ")


    def check_backups(self, page, message = f"{colors.YELLOW}Viewing backups"):
        clear() #clearing console to make it better to shee where the i
        print(f"{colors.GRAY}Page {page}{colors.WHITE} | {message}{colors.WHITE}")
        print(f"====================")
      
        backups = self.library.get_backups() #getting the catalog booklist from the library
        print(f"{colors.YELLOW}[{buttons.search}]{colors.WHITE} create backup")
        if len(backups): print(f"Enter one of the numbers to load that backup\n")
        else: print(f"{colors.RED}There are no backups{colors.WHITE}\n")

        index = 1
        for bup in backups[page*9 : (page+1)*9]: #taking the part of the list thats supose to be displayed (from thispage untill the start of the next page)
            print(f"{colors.YELLOW}[{index}]{colors.WHITE} {bup}")
            index += 1
        
        print("")
        if len(backups)-page*9 > 9: #if there are more books with a higher index then shown on the page
            print(f"{colors.YELLOW}[{buttons.next}]{colors.WHITE} To go to the next page")
        if page > 0: #if there are more books with a lower index then shown on the page
            print(f"{colors.YELLOW}[{buttons.previous}]{colors.WHITE} To go to the previous page")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")

        x = input("What will you do: ").upper()
        #check if the user pressed go back
        if x == buttons.search: 
            self.library.make_backup()
            self.check_backups(0, f"{colors.GREEN}backup made")
        if x == buttons.goBack: 
            self.start()
        #check if the user pressed next
        elif x == buttons.next:
            if len(backups)-page*9 > 9:
                self.check_backups(page + 1)
            else:
                self.check_backups(page, f"{colors.RED}There arent any pages after.")
        #check if the user pressed previous
        elif x == buttons.previous:
            if page > 0:
                self.check_backups(page - 1)
            else:
                self.check_backups(page, f"{colors.RED}There arent any pages before.")
        #if not, then its a invalied input

        elif x.isdigit(): 
            if int(x) < 10 and int(x) >= 0:
                if (int(x) - 1 + 9*page) < len(backups):
                    msg = self.library.load_backup(f"/{backups[int(x) - 1 + 9*page]}")
                    self.check_backups(page, msg)
                else: 
                    self.check_backups(page, f"{colors.RED}Invalid input, please try again.")

        else:
            self.check_backups(page, f"{colors.RED}Invalid input, please try again.")




    def start(self, message = f"{colors.YELLOW}Home Page"):
        clear()
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        print(f"[1] View Catalog")
        print(f"[2] View Library")
        print(f"[3] View Members")
        print(f"[4] Add Books")
        print(f"[5] Add Members")
        print(f"[6] View Backups")
        print(f"\n{colors.RED}[{buttons.goBack}]{colors.WHITE} Log Out")
        x = input("What will you do: ")
        if x == buttons.goBack: 
            self.library.run()
        elif x == "1":
            self.check_catalog(0)
        elif x == "2":
            self.check_library(0)
        elif x == "3":
            self.check_members(0)
        elif x == "4":
            self.add_book()
        elif x == "5":
            self.add_member()
        elif x == "6":
            self.check_backups(0)
        else:
            self.start(f"{colors.RED}Invalid input, please try again.")