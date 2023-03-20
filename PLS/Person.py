#from Library import Library #this import is not allowed due to circular imports, it only helps with autocomplete while writing in this file
from Settings import buttons, colors, clear

class Person:
    def __init__(self, library, number, givenName, surname,streetAddress, zipCode, city, emailAddress, username, password, telephoneNumber ):
        self.library : Library  = library #defining types does nothing at runtime, but while wrinting it helps with autocomplete
        
        self.number = number
        self.givenName = givenName
        self.surname = surname

        self.streetAddress = streetAddress
        self.zipCode = zipCode
        self.city = city

        self.emailAddress = emailAddress

        self.username : str = username
        self.password : str = password

        self.telephoneNumber = telephoneNumber
    
    def __eq__(self, other): #default equals override
        if isinstance(other, Person):
            return self.username == other.username
        return False
    
    def __str__(self): #default to string override
        return f"{self.username} - {self.library.catalog}"


    def search_catalog(self, message = f"{colors.YELLOW}Searching in the catalog"):
        clear() #clearing console to make it better to shee where the i
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        print(f"{colors.GRAY}Enter nothing to cancle search{colors.WHITE}")
        print(f"Search on Title, Author or ISBN:")
        term = input()
        if term == "":
            self.check_catalog(0)
        else:
            self.check_catalog(0, f"{colors.YELLOW}Result search catalog", self.library.catalog.search_books_by("all", term) ,term)

    #checkCatalog
    #=================
    #a method that shows 
    #(self, page, message)
    #       page > a number that represents at what page you are currently looking at
    #    ?  message > a message thats beeing displayed above this interface (like all other interfaces)
    #    ?  booklist > the list of books that should be displayed (when "default" it will just get the list from the library)
    #    ?  searchTerm > term that is used when searchiing a book
    def check_catalog(self, page, message = f"{colors.YELLOW}Checking the catalog", booklist = "default", searchTerm = ""):
        clear() #clearing console to make it better to shee where the i
        print(f"{colors.GRAY}Page {page}{colors.WHITE} | {message}{colors.WHITE}")
        print(f"====================")
        print(f"{colors.YELLOW}[{buttons.search}]{colors.WHITE} Search Book {colors.GRAY}{searchTerm}{colors.WHITE} \n") #it will show an option to search a book before showing a list of books inside the catalog

        if booklist == "default":
            booklist = self.library.catalog.books #getting the catalog booklist from the library
        index = 1
        for book in booklist[page*9 : (page+1)*9]: #taking the part of the list thats supose to be displayed (from thispage untill the start of the next page)
            print(f"[{index}] {book}")
            index += 1
        
        print("")
        if len(booklist)-page*9 > 9: #if there are more books with a higher index then shown on the page
            print(f"{colors.YELLOW}[{buttons.next}]{colors.WHITE} To go to the next page")
        if page > 0: #if there are more books with a lower index then shown on the page
            print(f"{colors.YELLOW}[{buttons.previous}]{colors.WHITE} To go to the previous page")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Go back")

        x = input("What will you do: ").upper()
        #check if the user pressed go back
        if x == buttons.goBack: 
            self.start()
        #check if the user pressed search        
        elif x == buttons.search:
            self.search_catalog()
        #check if the user pressed next
        elif x == buttons.next:
            if len(booklist)-page*9 > 9:
                self.check_catalog(page + 1)
            else:
                self.check_catalog(page, f"{colors.RED}There arent any pages afther.")
        #check if the user pressed previous
        elif x == buttons.previous:
            if page > 0:
                self.check_catalog(page - 1)
            else:
                self.check_catalog(page, f"{colors.RED}There arent any pages before.")
        #if not, then its a invalied input
        elif x.isdigit():
            clear()
            booklist[int(x) - 1 + 9*page].details()
            input(f"\n{colors.GRAY}Enter anything to go back{colors.WHITE}")
            self.check_catalog(page)

        else:
            self.check_catalog(page, f"{colors.RED}Invalid input, please try again.")


    #this start function is here for testing purposes
    #this will be deleted (or at least not used anymore) when we inherit the person as a User and/or Admin
    #then they will both have there own start method baked in 
    def start(self, message = f"{colors.YELLOW}Home Page"):
        clear()
        print(f"{message}{colors.WHITE}")
        print(f"====================")
        print(f"[1] Check Catalog")
        print(f"[2] Check Library\n")
        print(f"{colors.RED}[{buttons.goBack}]{colors.WHITE} Log Out")
        x = input("What will you do: ")
        if x == buttons.goBack: 
            self.library.run()
        elif x == "1":
            self.check_catalog(0)
        elif x == "2":
            print(f"{colors.GREEN}epic{colors.WHITE}, but Library command doesnt exist yet, thats a bummer")
        else:
            self.start(f"{colors.RED}Invalid input, please try again.")

