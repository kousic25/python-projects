def fine_checker(func):
    def wrapper(self, days):
        if days > 7:
            print("Fine Applicable")
        func(self, days)
    return wrapper
class Library:
    @fine_checker
    def return_book(self, days):
        print("Book Returned")
lib = Library()
lib.return_book(10)