from BookItem import BookItem
from datetime import date


class LoanItem(BookItem):
    def __init__(self, book, loanDate):
        #self.book = book
        BookItem.__init__(self, book)
        self.loanDate = date.today()
    
    def days_left(self):
        return 60 - (self.loanDate - date.today())