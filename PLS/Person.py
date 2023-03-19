#from Library import Library
from Settings import searchButton, goBack , nextButton, previousButton, clear
from colorama import Fore

class Person:
    def __init__(self, library, username, password ):
        self.library : Library  = library #defining types does nothing at runtime, but while wrinting it helps with autocomplete
        self.username : str = username
        self.password : str = password
    
    def __eq__(self, other): #default equals override
        if isinstance(other, Person):
            return self.username == other.username
        return False


    #checkCatalog
    #=================
    #a method that shows 
    #(self, page, message)
    #       page > a number that represents at what page you are currently looking at
    # opt   message > a message thats beeing displayed above this interface (like all other interfaces)
    def checkCatalog(self, page, message = f"{Fore.YELLOW}Checking the Catalog"):
        clear() #clearing console to make it better to shee where the i
        print(f"{Fore.YELLOW}Page {page}{Fore.RESET} | {message}{Fore.RESET}")
        print(f"====================")
        print(f"{Fore.YELLOW}[{searchButton}]{Fore.RESET} Search Book\n") #it will show an option to search a book before showing a list of books inside the catalog

        booklist = self.library.catalog.books #getting the catalog booklist from the library
        index = 1 + page*9 #calculating from what index it should count from (pure cosmetics)
        for book in booklist[page*9 : (page+1)*9]: #taking the part of the list thats supose to be displayed (from thispage untill the start of the next page)
            print(f"{index}. {book}")
            index += 1
        
        print("")
        if len(booklist)-page*9 > 9: #if there are more books with a higher index then shown on the page
            print(f"{Fore.YELLOW}[{nextButton}]{Fore.RESET} To go to the next page")
        if page > 0: #if there are more books with a lower index then shown on the page
            print(f"{Fore.YELLOW}[{previousButton}]{Fore.RESET} To go to the previous page")
        print(f"{Fore.RED}[{goBack}]{Fore.RESET} Go back")

        x = input("What will you do: ").upper()
        #check if the user pressed go back
        if x == goBack: 
            self.start()
        #check if the user pressed search        
        elif x == searchButton:
            print(f"{Fore.GREEN}epic{Fore.RESET}, but Search doesnt exist yet, thats a bummer")
        #check if the user pressed next
        elif x == nextButton:
            if len(booklist)-page*9 > 9:
                self.checkCatalog(page + 1)
            else:
                self.checkCatalog(page, f"{Fore.RED}There arent any pages afther.")
        #check if the user pressed previous
        elif x == previousButton:
            if page > 0:
                self.checkCatalog(page - 1)
            else:
                self.checkCatalog(page, f"{Fore.RED}There arent any pages before.")
        #if not, then its a invalied input
        else:
            self.checkCatalog(page, f"{Fore.RED}Invalid input, please try again.")


    #this start function is here for testing purposes
    #this will be deleted (or at least not used anymore) when we inherit the person as a User and/or Admin
    #then they will both have there own start method baked in 
    def start(self, message = f"{Fore.YELLOW}Home Page"):
        clear()
        print(f"{message}{Fore.RESET}")
        print(f"====================")
        print(f"[1] Catalog")
        print(f"[2] Library\n")
        print(f"{Fore.RED}[{goBack}]{Fore.RESET} Log Out")
        x = input("What will you do: ")
        if x == goBack: 
            print(f"{Fore.GREEN}epic{Fore.RESET}, but Log Out doesnt exist yet, thats a bummer")
        elif x == "1":
            self.checkCatalog(0)
        elif x == "2":
            print(f"{Fore.GREEN}epic{Fore.RESET}, but Library command doesnt exist yet, thats a bummer")
        else:
            self.start(f"{Fore.RED}Invalid input, please try again.")

