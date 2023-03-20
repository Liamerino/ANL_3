from Library import Library

def main():
    MyAwesomeLibrary = Library()
    #reech1950 - fgr5d4
    MyAwesomeLibrary.load_books("Books.json")
    MyAwesomeLibrary.load_members("Members.csv")
    MyAwesomeLibrary.run()


if __name__ == "__main__":
    main()