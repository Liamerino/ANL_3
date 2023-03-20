from Library import Library
from Settings import buttons, clear, colors

def __init__(self, library):
    self.library : Library = library
    self.username = "Admin"
    self.password = "Admin123"

def edit_book(self, library, book, message = f"{colors.YELLOW}Editing book: "):
    clear()
    print(f"{message}{book}{colors.WHITE}")
    print(f"====================")
    