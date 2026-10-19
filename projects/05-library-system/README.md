# ⭐⭐⭐ Library Management System
**Do this after:** Module 08 (add tests after Module 09)

## Requirements
Classes:
- `Book`: title, author, ISBN, available
- `Member`: name, member ID, borrowed books (max 3)
- `Library`: manages books and members

Features:
- Add books and members
- Search books by title or author
- Borrow and return books (with sensible errors: already borrowed, limit reached, etc.)
- List overdue books (books are due 14 days after borrowing)
- Save everything to JSON and load it on start

## Stretch goals
- Late fees
- A waiting list (reservations) when a book is borrowed
- Full pytest test suite
- Store data in SQLite with the built-in `sqlite3` module
