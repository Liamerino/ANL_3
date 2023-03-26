from Library import Library
from Admin import Admin

def main():
    MyAwesomeLibrary = Library()
    #member: reech1950 - fgr5d4
    #admin: Admin - Admin123
    MyAwesomeLibrary.initialize("Books.json","Members.csv")
    MyAwesomeLibrary.members.append(Admin(MyAwesomeLibrary, 0, "admin", "admin", "library road", "3000 LB", "Rotterdam", "library@gmail.com", "Admin", "Admin123", "0612345678"))
    MyAwesomeLibrary.run()

if __name__ == "__main__":
    main()