from Catalog import Catalog
from Book import Book
from Library import Library
from BookItem import BookItem
def main():
    print("starting the program")


    book1 = Book("Chinua Achebe","Nigeria","images/things-fall-apart.jpg","English", "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",209, "Things Fall Apart", "9781234534597", 1958)
    book2 = Book("Random Autor","Netherlands","nope.jpg","English", "https://google.com",209, "Random Title", "1234567890", 2018)
    book3 = Book("Kurt Vonnegut", "United States", "nope.jpg", "English", "https://google.com", 320, "Welcome to the Monkey House", "123457891", 1967)
    MyAwesomeLibrary = Library()
    MyAwesomeLibrary.addBookItem(book1)
    MyAwesomeLibrary.addBookItem(book2)
    MyAwesomeLibrary.addBookItem(book1)
    MyAwesomeLibrary.addBookItem(1)
    print("--=--")
    MyAwesomeLibrary.deleteBookItem(MyAwesomeLibrary.bookItems[0])
    MyAwesomeLibrary.deleteBookItem(MyAwesomeLibrary.bookItems[3])
    MyAwesomeLibrary.deleteBookItem(BookItem(book3))
    #MyCoolCatalog = Catalog()

    #MyCoolCatalog.add_book(book1)
    #MyCoolCatalog.show_books()
    #print("--=--")
    #MyCoolCatalog.add_book(book1)
    #MyCoolCatalog.add_book(book2)
    #MyCoolCatalog.show_books()
    #print("--=--")
    #MyCoolCatalog.remove_book(book2)
    #MyCoolCatalog.show_books()


if __name__ == "__main__":
    main()

#Book("Chinua Achebe","Nigeria","images/things-fall-apart.jpg","English", "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",209, "Things Fall Apart", "9781234534597", 1958) 
#Book("Random Autor","Netherlands","nope.jpg","English", "https://google.com",209, "Random Title", "1234567890", 2018) 
