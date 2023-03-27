from Settings import  buttons, colors, clear
from Catalog import Catalog
from BookItem import BookItem
from LoanItem import LoanItem
from Book import Book
from Person import Person
from Member import Member
import datetime
import csv
import json
import os
import shutil


class Library:
    def __init__(self, systemPath = "PLS-System"):
        self.systemPath = systemPath
        self.catalogPath = f"/catalog.json"
        self.libraryPath = f"/library.json"
        self.membersPath = f"/members.json"
        self.backupFolderPath = f"{systemPath}/PLS-Backups"

        self.catalog = Catalog()
        #defining types does nothing at runtime, but while wrinting it helps with autocomplete
        self.members : list[Person] = []     
        self.bookItems : list[BookItem] = []
    

    
    #####################################
    # SYSTEM MANAGMENT
    #####################################
    def initialize(self, pathBooks = "Books.json", pathMembers = "Members.csv"):
        self.system_ceckPath()

        if not (os.path.exists(f"{self.systemPath}{self.catalogPath}") and os.path.exists(f"{self.systemPath}{self.libraryPath}")):
            self.load_books(pathBooks)
        else:
            self.load_system_library()
            self.load_system_catalog()

        if not os.path.exists(f"{self.systemPath}{self.membersPath}"):
            self.load_members(pathMembers)
        else:
            self.load_system_members()

    def system_ceckPath(self):
        if not os.path.exists(self.systemPath):
            os.makedirs(self.systemPath)
        if not os.path.exists(self.backupFolderPath):
            os.makedirs(self.backupFolderPath)

    def system_save_catalog(self):
        data = []
        for b in self.catalog.books:
            data.append({
                "author" :b.author,
                "country" :b.country,
                "imageLink" :b.imageLink,
                "language" :b.language,
                "link" :b.link,
                "pages" :b.pages,
                "title" :b.title,
                "ISBN" :b.ISBN,
                "year" :b.year
            })
        json_data = json.dumps(data, indent=2)
        with open(f"{self.systemPath}{self.catalogPath}", "w") as file:
            file.write(json_data)
    
    def system_save_library(self):
        data = []
        currentBook = {}
        first = True
        amount = 1
        for b in self.bookItems:
            newBook = {
                "author" :b.author,
                "country" :b.country,
                "imageLink" :b.imageLink,
                "language" :b.language,
                "link" :b.link,
                "pages" :b.pages,
                "title" :b.title,
                "ISBN" :b.ISBN,
                "year" :b.year
            }
            if currentBook == newBook:
                amount += 1
            else:
                if not first:
                    currentBook["copies"] = amount
                    data.append(currentBook)
                first = False
                amount = 1
                currentBook = newBook


        currentBook["copies"] = amount
        data.append(currentBook)

        json_data = json.dumps(data, indent=2)
        with open(f"{self.systemPath}{self.libraryPath}", "w") as file:
            file.write(json_data)

    def system_save_members(self):
        data = []
        for m in self.members:
            if isinstance(m, Member):
                loanedBooks = []
                for b in m.loaned:
                    loanedBooks.append({
                        "author" :b.author,
                        "country" :b.country,
                        "imageLink" :b.imageLink,
                        "language" :b.language,
                        "link" :b.link,
                        "pages" :b.pages,
                        "title" :b.title,
                        "ISBN" :b.ISBN,
                        "year" :b.year,
                        "loanDate" : b.loanDate
                    })
                data.append({
                    "Number" :m.number,
                    "GivenName" :m.givenName,
                    "Surname" :m.surname,
                    "StreetAddress" :m.streetAddress,
                    "ZipCode" :m.zipCode,
                    "City" :m.city,
                    "EmailAddress" :m.emailAddress,
                    "Username" :m.username,
                    "Password" :m.password,
                    "TelephoneNumber" : m.telephoneNumber,
                    "loaned" : loanedBooks
                })
        json_data = json.dumps(data, indent=2)
        with open(f"{self.systemPath}{self.membersPath}", "w") as file:
            file.write(json_data)


    def load_system_catalog(self, path = ""):
        returnValue = ""
        if(path == "" or not os.path.exists(path)):
            path = f"{self.systemPath}{self.catalogPath}"
            returnValue = f"\n{colors.RED}Not able to load catalog {colors.GRAY}{path}"
        
        self.catalog.books = []
        with open(path, "r") as file:
            books = json.load(file)
            for book in books:
                bookToAdd = Book(book["author"], book["country"],book["imageLink"], book["language"], book["link"], book["pages"],book["title"],book["ISBN"], book["year"])
                self.catalog.books.append(bookToAdd)
        
        self.system_save_catalog()
        return returnValue
    
    def load_system_library(self, path = ""):
        returnValue = ""
        if(path == "" or not os.path.exists(path)):
            path = f"{self.systemPath}{self.libraryPath}"
            returnValue = f"\n{colors.RED}Not able to load bookitems {colors.GRAY}{path}"
        
        self.bookItems = []
        with open(path, "r") as file:
            books = json.load(file)
            for book in books:
                bookToAdd = Book(book["author"], book["country"],book["imageLink"], book["language"], book["link"], book["pages"],book["title"],book["ISBN"], book["year"])
                for i in range(book["copies"]):
                    self.bookItems.append(BookItem(bookToAdd))
        
        self.system_save_library()
        return returnValue

    def load_system_members(self, path = ""):
        returnValue = ""
        if(path == "" or not os.path.exists(path)):
            path = f"{self.systemPath}{self.membersPath}"
            returnValue =  f"\n{colors.RED}Not able to load members {colors.GRAY}{path}"
        
        self.members = []
        with open(path, "r") as file:
            members = json.load(file)
            for mem in members:
                memToAdd = Member(self, mem["Number"], mem["GivenName"],mem["Surname"], mem["StreetAddress"], mem["ZipCode"], mem["City"],mem["EmailAddress"],mem["Username"], mem["Password"], mem["TelephoneNumber"])
                self.members.append(memToAdd)
                for book in mem["loaned"]:
                    bookToAdd = Book(book["author"], book["country"],book["imageLink"], book["language"], book["link"], book["pages"],book["title"],book["ISBN"], book["year"])
                    memToAdd.loaned.append(LoanItem(BookItem(bookToAdd), book["loanDate"]))
        
        self.system_save_members()
        return returnValue


    def load_backup(self, path):
        if(not os.path.exists(f"{self.backupFolderPath}{path}")):
            return f"{colors.RED}Invalid backup path {colors.WHITE}|{colors.GRAY} {self.backupFolderPath}{path}{colors.WHITE}"
        
        cat = self.load_system_catalog(f"{self.backupFolderPath}{path}{self.catalogPath}") #empty if good, otherwise error msg
        lib = self.load_system_library(f"{self.backupFolderPath}{path}{self.libraryPath}") #empty if good, otherwise error msg
        mem = self.load_system_members(f"{self.backupFolderPath}{path}{self.membersPath}") #empty if good, otherwise error msg
        return f"{colors.GREEN}Backup has been loaded {colors.WHITE}|{colors.GRAY} {self.backupFolderPath}{path} {cat}{lib}{mem}{colors.WHITE}"
    
    def make_backup(self):
        self.system_ceckPath()

        today = datetime.datetime.now()
        newPath = f"/{today.year}-{today.month}-{today.day}_{today.hour}-{today.minute}-{today.second}_{today.microsecond}"
        backups = self.get_backups()
        addition = 0
        while newPath in backups:
            addition += 1
            newPath = f"/{today.year}-{today.month}-{today.day}_{today.hour}-{today.minute}-{today.second}_{today.microsecond + addition}"
        
        os.makedirs(f"{self.backupFolderPath}{newPath}")
        shutil.copyfile(f"{self.systemPath}{self.catalogPath}", f"{self.backupFolderPath}{newPath}{self.catalogPath}")
        shutil.copyfile(f"{self.systemPath}{self.libraryPath}", f"{self.backupFolderPath}{newPath}{self.libraryPath}")
        shutil.copyfile(f"{self.systemPath}{self.membersPath}", f"{self.backupFolderPath}{newPath}{self.membersPath}")

    
    def get_backups(self):
        return os.listdir(self.backupFolderPath)



    #####################################
    # MEMBERS
    #####################################
    def load_members(self, path):
        if not os.getcwd() in os.path.abspath(path):
            print("cant load, file not the correct directory")
            return
        
        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            firstline = True
            for row in csv_reader:
                if firstline:
                    #print(f'Column names are {", ".join(row)}')
                    firstline = False
                else:
                   if len(row) == 10:
                    self.add_member(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    print(f"loading user:{row[0]} {row[7]}")
            print(f'loading users done.')
        
        self.members.sort(key=self.sort_by_number)
        self.system_save_members()


    def sort_by_number(self,person):
        if person.number.isnumeric():
            return int(person.number)
        else: return 99999999999999 #if its not a number it will be at the total end of the pages (unless there is something higher then this number, but that probably wont happen)

    def add_member(self, number, givenName, surname,streetAddress, zipCode, city, emailAddress, username, password, telephoneNumber):
        for p in self.members:
            if p.username == username:
                return
        self.members.append(
                Member(self, number,givenName, surname,streetAddress, zipCode, city, emailAddress, username, password, telephoneNumber)
        )
        self.members.sort(key=self.sort_by_number)
        self.system_save_members()

    def get_user_id(self):
        return str(max([int(x.number) for x in self.members]) + 1)
        
    def delete_member(self, member):
        if isinstance(member, Member):
            if member in self.members:
                self.members.remove(member)
                self.system_save_members()

    #####################################
    # BOOKS  (library)
    #####################################
    def load_books(self, path):
        if not os.path.exists(path):
            return

        with open(path, 'r') as f:
            books = json.load(f)
            for book in books:
                bookToAdd = Book(book["author"], book["country"],book["imageLink"], book["language"], book["link"], book["pages"],book["title"],book["ISBN"], book["year"])
                if bookToAdd not in self.bookItems:
                    self.add_book_item(BookItem(bookToAdd),
                                       BookItem(bookToAdd),
                                       BookItem(bookToAdd),
                                       BookItem(bookToAdd),
                                       BookItem(bookToAdd))
                else:
                    self.add_book_item(BookItem(bookToAdd))

                if bookToAdd not in self.catalog.books:
                    self.catalog.add_book(bookToAdd)
        self.sort_books()

    def add_book_item(self, *books):
        for book in books:
            if isinstance(book, BookItem):
                self.bookItems.append(book)
            if isinstance(book, Book):
                self.bookItems.append(BookItem(book))
        self.sort_books("library")


    def delete_book_item(self, bookItem):
        if isinstance(bookItem, BookItem):
            if bookItem in self.bookItems:
                self.bookItems.remove(bookItem)
                self.system_save_library()
                #you dont have to sort a list at removal, it will still be sorten even afther removing a thing

    def sort_by_title(self,book):
        return f"{book.title} - {book.author}"
    
    # where = "catalog" or "library" or nothing to do both
    def sort_books(self, where =""):
        if where == "library":
            self.bookItems.sort(key=self.sort_by_title)
            self.system_save_library()
        elif where == "catalog":
            self.catalog.books.sort(key=self.sort_by_title)
            self.system_save_catalog()
        else: 
            self.bookItems.sort(key=self.sort_by_title)
            self.catalog.books.sort(key=self.sort_by_title)
            self.system_save_catalog()
            self.system_save_library()

    
    #search book by: "author" || "title" || "all"
    def search_books_by(self, by,  term):
        sortBy = by.lower()
        termLow = term.lower()
        books : list[BookItem] = [] #type declaration does not effect run time but helps while writing
        for b in self.bookItems:
            if (sortBy == "title" and termLow in b.title.lower() 
                or sortBy == "author" and termLow in b.author.lower()
                or sortBy == "all" and (termLow in b.author.lower() or termLow in b.title.lower())
                ):
                books.append(b)
        return books
    
    def amount_of_copies(self, book):
        if isinstance(book, Book):
            count = 0
            for b in self.bookItems:
                if book.ISBN == b.ISBN: 
                    count += 1
            return count
        else: 
            return 0
        




    #####################################
    # START OF LIBRARY PROGRAM
    #####################################
    def run(self, message = f"{colors.YELLOW} Log in"):
        clear() #clearing console
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        print(f"Enter username")
        print(f"{colors.GRAY}or enter {colors.RED}[{buttons.goBack}]{colors.GRAY} to shut down the program{colors.WHITE}")
        un = input()
        if un.upper() == buttons.goBack:
            exit()
        if un == "":
            self.run(f"{colors.RED}You cant enter nothing")
            return
        clear() #clearing console
        print(f"{colors.YELLOW}{un}{colors.WHITE}")
        print(f"====================")
        print(f"Enter password")
        print(f"{colors.GRAY}or nothing to change the username{colors.WHITE}")
        pw = input()

        if pw == "":
            self.run()
            return
        
        for user in self.members:
            if user.username.upper() == un.upper() and user.password == pw:
                user.start()
                return
        
        self.run(f"{colors.RED}Wrong username or password")