# Library Management System

A comprehensive Library Management System built using Object-Oriented Programming (OOP) principles in Python. This project demonstrates key OOP concepts including classes, objects, encapsulation, composition, and aggregation.

## 🎯 Project Overview

This Library Management System allows librarians to:
- Manage book inventory
- Register library members
- Issue and track book loans
- Monitor borrowing limits and overdue books
- Calculate fines for overdue books

## 🏗️ System Architecture

The system is built using four main classes that work together:

### Core Classes

1. **Book Class** (`book.py`)
   - Represents individual books in the library
   - Manages book availability status
   - Handles borrowing and returning operations

2. **Member Class** (`member.py`)
   - Represents library members
   - Tracks borrowed books
   - Enforces borrowing limits based on membership type

3. **Loan Class** (`loan.py`)
   - Represents book loan transactions
   - Calculates due dates and fines
   - Tracks loan status and return dates

4. **Library Class** (`library.py`)
   - Main system controller
   - Manages collections of books, members, and loans
   - Coordinates operations between all classes

## 🚀 Features

### Book Management
- Add new books to the library
- Track book availability
- Search and view all books
- Monitor book status (available/borrowed)

### Member Management
- Register new members
- Support different membership types (Student, Faculty, Regular)
- Enforce borrowing limits per membership type
- Track member's borrowed books

### Loan Management
- Issue books to members
- Track due dates (14-day loan period)
- Calculate fines for overdue books ($10 per day)
- Prevent duplicate borrowing
- Validate borrowing limits

### User Interface
- Interactive menu-driven system
- Clear user prompts and feedback
- Error handling for invalid operations
- Easy-to-use command-line interface

## 📋 OOP Concepts Demonstrated

### 1. **Classes and Objects**
- Each class represents a real-world entity
- Objects are instances created from classes
- Example: `Book` class → `"Harry Potter"` object

### 2. **Encapsulation**
- Private attributes using underscore convention (`_is_borrowed`)
- Public methods for controlled access
- Data hiding and protection

### 3. **Composition**
- Loan class contains references to Book and Member objects
- Objects working together to represent relationships

### 4. **Aggregation**
- Library class manages collections of other objects
- System-level coordination and control

### 5. **Method Design**
- Single responsibility principle
- Clear method names and purposes
- Proper error handling and validation

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Running the System

1. **Clone or download the project files**
2. **Navigate to the project directory**
   ```bash
   cd "Library Management System(OOPs self-made)"
   ```

3. **Run the main program**
   ```bash
   python main.py
   ```

4. **Follow the menu prompts to interact with the system**

## 📁 Project Structure

```
Library Management System(OOPs self-made)/
├── book.py          # Book class implementation
├── member.py        # Member class implementation
├── loan.py          # Loan class implementation
├── library.py       # Library class implementation
├── main.py          # Main menu system
└── README.md        # Project documentation
```

## 🎮 Usage Guide

### Main Menu Options

1. **Add Book** - Add new books to the library
2. **Register Member** - Register new library members
3. **Issue Book** - Issue books to members
4. **View All Books** - Display all books and their status
5. **View All Members** - Display all registered members
6. **Exit** - Close the application

### Example Workflow

1. **Add Books:**
   - Book ID: B001
   - Title: Python Programming
   - Author: John Smith
   - ISBN: 1234567890
   - Genre: Programming

2. **Register Member:**
   - Member ID: M001
   - Name: Jane Doe
   - Contact: jane@email.com
   - Membership Type: Student

3. **Issue Book:**
   - Book ID: B001
   - Member ID: M001

## 🔧 Technical Details

### Membership Types & Borrowing Limits
- **Student**: 3 books maximum
- **Faculty**: 10 books maximum
- **Regular**: 5 books maximum

### Loan Period & Fines
- **Loan Period**: 14 days
- **Fine Rate**: $10 per day overdue
- **Fine Calculation**: Automatic based on due date

### Data Validation
- Prevents duplicate book IDs
- Prevents duplicate member IDs
- Validates borrowing limits
- Checks book availability before issuing

## 🧪 Testing

Each class includes built-in test cases. Run individual files to test specific functionality:

```bash
python book.py      # Test Book class
python member.py    # Test Member class
python loan.py      # Test Loan class
python library.py   # Test Library class
```

## 🎓 Learning Outcomes

This project teaches:
- **Object-Oriented Programming** fundamentals
- **Class design** and **method implementation**
- **Data encapsulation** and **access control**
- **System architecture** and **class relationships**
- **Error handling** and **validation**
- **User interface design** principles

## 🔮 Future Enhancements

Potential improvements for advanced learning:
- Database integration for persistent storage
- GUI interface using tkinter or PyQt
- Advanced search and filtering capabilities
- Book reservation system
- Email notifications for overdue books
- Statistical reporting features
- Multi-library support

## 📝 Code Quality

The project follows Python best practices:
- Clear and descriptive variable names
- Proper code documentation
- Consistent formatting and style
- Modular design with separated concerns
- Comprehensive error handling

## 🤝 Contributing

This is an educational project. Feel free to:
- Add new features
- Improve existing functionality
- Fix bugs or issues
- Enhance the user interface
- Add more comprehensive testing

## 📄 License

This project is created for educational purposes and is open for learning and experimentation.

---

**Happy Coding! 🚀**

*This Library Management System demonstrates the power of Object-Oriented Programming in creating real-world applications.*