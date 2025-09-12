from book import Book
from member import Member
from loan import Loan
from datetime import datetime

class Library:
    def __init__(self):
        self.books=[]
        self.active_loans=[]
        self.members=[]

    def add_book(self, book_id, title, author, isbn, genre):

        for book in self.books:
            if book.book_id==book_id:
                return False

        new_book=Book(book_id,title,author,isbn,genre)
        self.books.append(new_book)
        return True

    def register_member(self, member_id, name, contact_info, membership_type):
        for member in self.members:
            if member.member_id == member_id:
                return False

        new_member=Member(member_id,name,contact_info,membership_type)
        self.members.append(new_member)
        return True

    def issue_book(self, book_id, member_id):
        # Find the book
        book = None
        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        #find the member
        member=None
        for m in self.members:
            if m.member_id==member_id:
                member=m
                break

        # Check if both exist
        if not book or not member:
             return False  # Book or member not found

        # Check if book is available
        if not book.is_available():
             return False  # Book is already borrowed

        # Check if member can borrow more
        if not member.can_borrow_book():
            return False  # Member has reached borrowing limit


        # Create loan and update book status
        loan = Loan(f"L{len(self.active_loans)+1}", book, member, datetime.now())
        self.active_loans.append(loan)
        book.borrow_book()
        member.borrow_book(book)

        return True

# Test the Library class
if __name__ == "__main__":
    library = Library()
    
    # Add some books
    library.add_book("B001", "Python Guide", "Author1", "123456", "Programming")
    library.add_book("B002", "Java Basics", "Author2", "789012", "Programming")
    
    # Register a member
    library.register_member("M001", "John Doe", "john@email.com", "Student")
    
    # Issue a book
    result = library.issue_book("B001", "M001")
    print(f"Book issued successfully: {result}")
    
    # Try to issue same book again (should fail)
    result2 = library.issue_book("B001", "M001")
    print(f"Same book issued again: {result2}")
    
    print(f"Total books: {len(library.books)}")
    print(f"Total members: {len(library.members)}")
    print(f"Active loans: {len(library.active_loans)}")
