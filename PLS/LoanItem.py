from BookItem import BookItem
import time


class LoanItem(BookItem):
    def __init__(self, book, loanDate = int(time.time()) ):
        BookItem.__init__(self, book)
        self.loanDate = loanDate
    
    def days_left(self):
        return 60 - int(((((time.time() - self.loanDate)/60)/60)/24)*10)/10