class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Informal string representation"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation"""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor: Triggered upon object deletion"""
        print(f"Deleting {self.title}")
from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)             # Uses __str__
    print(repr(my_book))       # Uses __repr__
    del my_book                # Triggers __del__

if __name__ == "__main__":
    main()
