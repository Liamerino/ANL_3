from Library import Library
from Admin import Admin

def main():
    MyAwesomeLibrary = Library()
    #reech1950 - fgr5d4
    MyAwesomeLibrary.load_books("Books.json")
    MyAwesomeLibrary.load_members("Members.csv")
    MyAwesomeLibrary.members.append(Admin(MyAwesomeLibrary, 1, "admin", "admin", "library road", "3000 LB", "Rotterdam", "library@gmail.com", "0612345678"))
    MyAwesomeLibrary.run()

if __name__ == "__main__":
    main()