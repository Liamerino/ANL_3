from Catalog import Catalog
from Book import Book
from Library import Library
from BookItem import BookItem
from Person import Person
from Settings import clear

def main():
    print("starting the program")


    book1 = Book("Chinua Achebe","Nigeria","images/things-fall-apart.jpg","English", "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",209, "Things Fall Apart", "9781234534597", 1958)
    book2 = Book("Random Autor","Netherlands","nope.jpg","English", "https://google.com\n",209, "Random Title", "1234567890", 2018)
    book3 = Book("Kurt Vonnegut", "United States", "nope.jpg", "English", "https://google.com\n", 320, "Welcome to the Monkey House", "123457891", 1967)
    book4 = Book("Kurt Vonnegut", "United States", "nope.jpg", "English", "https://google.com\n", 320, "Welcome to the Monkey Hwouse", "123457892", 2967)
    book5 = Book("Kurat Vaonanegut", "United States", "nope.jpg", "English", "https://google.com\n", 3201, "Welcome to the Monkey Heouse", "123457893", 3967)
    book6 = Book("Kurt Vonnaegut", "United States", "nope.jpg", "English", "https://google.com\n", 3202, "Welcome to the Monkey Hourse", "123457881", 4967)
    book7 = Book("Kuart aVonaaaanegut", "United States", "nope.jpg", "English", "https://google.com\n", 3230, "Welcome to the Monkey Houwse", "123457871", 5967)
    book8 = Book("Kurt Voannegut", "United States", "nope.jpg", "English", "https://google.com\n", 3240, "Welcome to the Monkey Housee", "123457899", 6967)
    book9 = Book("Kurata aVoannegut", "United States", "nope.jpg", "English", "https://google.com\n", 3520, "Welcome to the Monkey Housee", "123457842", 7967)
    book10 = Book("Kurt Vonnegut", "United States", "nope.jpg", "English", "https://google.com\n", 3260, "Welcome to the Monkey Housed", "1234578941", 8967)
    book11 = Book("Kaurt Vonneagut", "United States", "nope.jpg", "English", "https://google.com\n", 3620, "Welcome to the Monkey Houses", "12342891", 9967)
    book12 = Book("Kurat Vonanaeguat", "United States", "nope.jpg", "English", "https://google.com\n", 3720, "Welcome to the Monkey Housea", "123427891", 10967)

    
    MyAwesomeLibrary = Library()
    MyAwesomeLibrary.add_book_item(book1)
    MyAwesomeLibrary.add_book_item(book2, book3, book4, book6, book5, book7, book8, book9, book10, book11, book12)
    clear()
    
    
    #reech1950 - fgr5d4
    MyAwesomeLibrary.load_members("Members.csv")
    MyAwesomeLibrary.run()
    
    


if __name__ == "__main__":
    main()

#Book("Chinua Achebe","Nigeria","images/things-fall-apart.jpg","English", "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",209, "Things Fall Apart", "9781234534597", 1958) 
#Book("Random Autor","Netherlands","nope.jpg","English", "https://google.com",209, "Random Title", "1234567890", 2018) 
