class Book:
    def __init__(self,book_id, title, author, isbn, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self._is_borrowed = False

    def is_available(self):
        return not self._is_borrowed

    def borrow_book(self):
        self._is_borrowed = True

    def return_book(self):
        self._is_borrowed = False


# Test the Book class
if __name__ == "__main__":
    # Create a book object
    book1 = Book("B001", "Harry Potter", "J.K. Rowling", "978-1234567890", "Fantasy")
    
    # Test the methods
    print(f"Book: {book1.title} by {book1.author}")
    print(f"Is available: {book1.is_available()}")
    
    # Borrow the book
    book1.borrow_book()
    print(f"After borrowing - Is available: {book1.is_available()}")
    
    # Return the book
    book1.return_book()
    print(f"After returning - Is available: {book1.is_available()}")