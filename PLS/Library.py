from Settings import  buttons, colors, clear
from Catalog import Catalog
from BookItem import BookItem
from Book import Book
from Person import Person
from Member import Member
import csv
import json
import os

class Library:
    def __init__(self):
        self.catalog = Catalog()
        self.members : list[Person] = []     #defining types does nothing at runtime, but while wrinting it helps with autocomplete
        self.bookItems : list[BookItem] = []
    
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






    #####################################
    # BOOKS  (library)
    #####################################
    def load_books(self, path):
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
        self.bookItems.sort(key=self.sort_by_title)
        self.catalog.books.sort(key=self.sort_by_title)

    def add_book_item(self, *books):
        for book in books:
            if isinstance(book, BookItem):
                self.bookItems.append(book)
                self.bookItems.sort(key=self.sort_by_title)


    def delete_book_item(self, bookItem):
        if isinstance(bookItem, BookItem):
            if bookItem in self.bookItems:
                self.bookItems.remove(bookItem)
                #you dont have to sort a list at removal, it will still be sorten even afther removing a thing

    def sort_by_title(self,book):
        return book.title
    
    # where = "catalog" or "library" or nothing to do both
    def sort_books(self, where =""):
        if where == "library":
            self.bookItems.sort(key=self.sort_by_title)
        elif where == "catalog":
            self.catalog.books.sort(key=self.sort_by_title)
        else: 
            self.bookItems.sort(key=self.sort_by_title)
            self.catalog.books.sort(key=self.sort_by_title)

    
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