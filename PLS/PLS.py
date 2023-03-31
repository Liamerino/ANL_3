import sys
sys.path.append("PLS-SourceFiles")
from Library import Library
from Admin import Admin


def main():
    MyAwesomeLibrary = Library()
    #member: othed1997 - urmhhh
    #admin: admin - admin123
    MyAwesomeLibrary.initialize()
    MyAwesomeLibrary.members.append(Admin(MyAwesomeLibrary, "0", "admin", "admin", "library road", "3000 LB", "Rotterdam", "library@gmail.com", "admin", "admin123", "0612345678"))
    MyAwesomeLibrary.run()

if __name__ == "__main__":
    main()