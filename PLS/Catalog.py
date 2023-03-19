from Book import Book

class Catalog:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            print(f"[{book}] isnt a book therefore cant be added to the catalog.")
        elif book in self.books:
            print(f"[{book.title}] is already in the catalog")
        else:
            print(f"[{book.title}] has been added to the catalog")
            self.books.append(book)
    
    def show_books(self):
        index = 1
        for b in self.books:
            print( f"[{index}] {b}" )
            index += 1

    def remove_book(self, book):
        if not isinstance(book, Book):
            return (False, f"[{book}] isnt a book therefore cant be removed from the catalog.")
        elif book not in self.books: 
            return (False, f"[{book.title}] is not in the catalog")
        else:
            self.books.remove(book)
            return (True, f"[{book.title}] has been removed from the catalog")

    #search book by: "author" || "title" || "isbn"
    def search_books_by(self, by, term):
        sortBy = by.lower()
        found : list[Book] = [] #type declaration does not effect run time but helps while writing
        for book in self.books:
            if (sortBy == "title" and term.lower() in book.title.lower() 
                or sortBy == "ibsn" and term  in book.ISBN
                or sortBy == "author" and term.lower()  in book.author.lower() ):
                found.append(book)
        return found

    """
    def search_book_by_title(self,title):
        for b in self.books:
            if b.title == title:
                return b
    """




    def edit_book(self, book):
        if not isinstance(book, Book):
            print(f"[{book}] isn't a book and therefore can't be edited")
        elif book not in self.books:
            print(f"[{book}] is not in the catalog")
        else:
            print(f"What would you like to edit? Enter the corresponding number to edit:\n[1] Author: {book.author}\n[2] Country: {book.country}\n"
                  f"[3] Image link: {book.imageLink}\n[4] Language: {book.language}\n[5] Book link: {book.link}\n[6] Amount of pages: {book.pages}\n"
                  f"[7] Title: {book.title}\n[8] ISBN: {book.ISBN}\n[9] Year of release: {book.year}\nTo go back enter [back]")
            choice = input()
            if choice == "1":
                book.author = input(f"Author:\nCurrently: {book.author}\nNew: ")
                self.edit_book(book)
            elif choice == "2":
                book.country = input(f"Country:\nCurrently: {book.country}\nNew: ")
                self.edit_book(book)
            elif choice == "3":
                book.imageLink = input(f"Image link:\nCurrently: {book.imageLink}\nNew: ")
                self.edit_book(book)
            elif choice == "4":
                book.language = input(f"Language:\nCurrently: {book.language}\nNew: ")
                self.edit_book(book)
            elif choice == "5":
                book.link = input(f"Book link:\nCurrently: {book.link}\nNew: ")
                self.edit_book(book)
            elif choice == "6":
                while True:
                    try:
                        book.pages = int(input(f"Amount of pages:\nCurrently: {book.pages}\nNew: "))
                    except:
                        print("The amount of pages needs to be a whole number")
                    else:
                        break
                self.edit_book(book)
            elif choice == "7":
                book.title = input(f"Title:\nCurrently: {book.title}\nNew: ")
                self.edit_book(book)
            elif choice == "8":
                book.ISBN = input(f"ISBN:\nCurrently: {book.ISBN}\nNew: ")
                self.edit_book(book)
            elif choice == "9":
                while True:
                    try:
                        book.year = int(input(f"Year of release:\nCurrently: {book.year}\nNew: "))
                    except:
                        print("The year of release needs to be a whole number")
                    else:
                        break
                self.edit_book(book)
            elif choice == "back":
                print("Going back to main or something")
            else:
                print("You entered an incorrect input")
                self.edit_book(book)

