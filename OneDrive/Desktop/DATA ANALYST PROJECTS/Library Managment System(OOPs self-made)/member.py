class Member:
    def __init__(self, member_id, name, contact_info, membership_type):  # Fixed!
        self.member_id = member_id
        self.name = name
        self.contact_info = contact_info
        self.membership_type = membership_type
        self._borrowed_books = []

    def borrow_book(self, book):
        if self.can_borrow_book():  # Check if they can borrow more
            self._borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self._borrowed_books:  # Check if they have the book
            self._borrowed_books.remove(book)
            return True
        return False

    def get_borrowed_books(self):
        return tuple(self._borrowed_books)  # Most secure - immutable

    def can_borrow_book(self):
        if self.membership_type == "Student":
            return len(self._borrowed_books) < 3
        elif self.membership_type == "Faculty":
            return len(self._borrowed_books) < 10
        elif self.membership_type == "Regular":
            return len(self._borrowed_books) < 5
        return False  # Unknown membership type

# Test the Member class
if __name__ == "__main__":
    member1 = Member("M001", "John Doe", "john@email.com", "Student")
    print(f"Member: {member1.name}")
    print(f"Can borrow more: {member1.can_borrow_book()}")
    print(f"Borrowed books: {member1.get_borrowed_books()}")