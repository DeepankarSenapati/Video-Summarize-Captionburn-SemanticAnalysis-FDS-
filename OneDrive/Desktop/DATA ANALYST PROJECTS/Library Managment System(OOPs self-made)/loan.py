from datetime import datetime, timedelta

class Loan:
    def __init__(self, loan_id, book, member, loan_date):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.loan_date = loan_date
        self.return_date=None
        
    def get_due_date(self):
        return self.loan_date + timedelta(days=14)

    def is_overdue(self):
        return datetime.now()>self.get_due_date()

    def calculate_fine(self):
        if self.is_overdue():
            return (datetime.now()-self.get_due_date()).days*10
        else:
            return 0

    def return_book(self):
        self.return_date = datetime.now()
        return self.return_date

if __name__ == "__main__":
    # We'll need to create a book and member first
    from book import Book
    from member import Member
    
    book1 = Book("B001", "Python Guide", "Author", "123456", "Programming")
    member1 = Member("M001", "John Doe", "john@email.com", "Student")
    
    # Create a loan
    loan1 = Loan("L001", book1, member1, datetime.now()-timedelta(24))
    
    print(f"Loan ID: {loan1.loan_id}")
    print(f"Book: {loan1.book.title}")
    print(f"Member: {loan1.member.name}")
    print(f"Due date: {loan1.get_due_date()}")
    print(f"Is overdue: {loan1.is_overdue()}")
    print(f"Fine: ${loan1.calculate_fine()}")


