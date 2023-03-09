class Book:
    def __init__(self, title, author, publicationYear):
        self.__title = title
        self.__author = author
        self.__publicationYear = publicationYear
    
    def get__title(self):
        return self.__title
    
    def set__title(self, value):
        self.__title = value

    def get__author(self):
        return self.__author
    
    def set__author(self, value):
        self.__author = value

    def get__publicationYear(self):
        return self.__publicationYear

    def set__publicationYear(self, value):
        self.__publicationYear = value    
