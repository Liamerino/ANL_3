from Settings import colors

class Book:
    def __init__(self, author, country, imageLink, language, link, pages, title, ISBN, year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.title = title
        self.ISBN = ISBN
        self.year = year
    
    
    def __eq__(self, other): #default equals override
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author and self.ISBN == self.ISBN
        return False
    
    def __str__(self): #default to string override
        return f"{self.title} - {self.author}"
    
    def details(self):
        print(f"{colors.WHITE}{self.title}{colors.GRAY} by{colors.WHITE} {self.author}")
        print(f"====================")
        print(f"{colors.GRAY}pages:{colors.WHITE} {self.pages}   {colors.GRAY}language:{colors.WHITE} {self.language}")
        print(f"{colors.GRAY}publication country: {self.country}   publication year: {self.year} {colors.WHITE}")
        print(f"{colors.GRAY}image source: {colors.CYAN}{self.imageLink} {colors.WHITE}")
        print(f"{colors.GRAY}book source: {colors.BLUE}{self.link} {colors.WHITE}")
        print(f"{colors.GRAY}ISBN: {colors.WHITE}{self.ISBN}")
