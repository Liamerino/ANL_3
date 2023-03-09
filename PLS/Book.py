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
  


# the book varables examples taken from the json
"""
    "author": "Chinua Achebe",
    "country": "Nigeria",
    "imageLink": "images/things-fall-apart.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
    "pages": 209,
    "title": "Things Fall Apart",
    "ISBN": "9781234534597",
    "year": 1958
"""