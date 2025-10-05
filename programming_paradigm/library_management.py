class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """Readable string representation of the book."""
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    """A class representing a library containing multiple books."""

    def __init__(self):
        self._books = []  # private list to store Book objects

    def add_book(self, book):
        """Add a new Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark a book as checked out by title if available."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"'{book.title}' has been checked out.")
                    return
                else:
                    print(f"'{book.title}' is already checked out.")
                    return
        print(f"No book found with the title '{title}'.")

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"'{book.title}' has been returned.")
                    return
                else:
                    print(f"'{book.title}' was not checked out.")
                    return
        print(f"No book found with the title '{title}'.")

    def list_available_books(self):
        """List all books that are not currently checked out."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")
