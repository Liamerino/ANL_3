import os
maxLoanedBooks = 3


class colors:
    WHITE = '\033[97m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    GRAY = '\033[90m'

class buttons: #1, 2, 3, 4, 5, 6, 7, 8, 9 are not allowed, those are buttons for a list of items
    goBack = "0"
    previous = "A"
    next = "D"
    delete = "X"
    edit= "E"
    search = "S"


def clear():#making space in the console so people understand what is relevant
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")