#from Library import Library
from Settings import buttons, clear, colors
from Person import Person

class Member(Person):
    def __init__(self, library, number, givenName, surname, streetAddress, zipCode, city, emailAddress,username, password, telephoneNumber):
        Person.__init__(self, library, number, givenName, surname, streetAddress, zipCode, city, emailAddress,username, password, telephoneNumber)

  