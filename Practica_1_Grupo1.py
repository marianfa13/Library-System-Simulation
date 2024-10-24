import threading
import time
import random

# Class to represent a Library
class Library():
    # Class attribute to hold the books
    shelf = {}

    def __init__(self, name):
        self.name = name
        self.shelf = {}
        self.lock = threading.Lock()  # Lock for mutual exclusion

    # Method to remove a book from the library
    def remove_book(self, book):
        with self.lock:
            if book in self.shelf:
                del(self.shelf[book])  # Remove the book from the shelf
                print(f"The book '{book}' has been removed from the library '{self.name}'.")

    # Method to add a book to the library
    def add_book(self, book):
        with self.lock:
            self.shelf[book] = 1  # 1 indicates the book is available

    # Method to change the status of a book (available or borrowed)
    def change_book_status(self, status, book):
        if book in self.shelf:
            self.shelf[book] = status

    # Method to display the current state of the library
    def show_status(self):
        with self.lock:
            print(f" ----------- Status of the library '{self.name}': {self.shelf} ----------- ")

# Class to represent a Book
class Book():
    title, publisher, publication_date = "", "", ""

    def __init__(self, title, publisher, publication_date):
        self.title = title
        self.publisher = publisher
        self.publication_date = publication_date

    # Method to return book details as a string
    def get_details(self):
        return f"Title: {self.title}, Publisher: {self.publisher}, Date: {self.publication_date}"

# Class to represent a Reader
class Reader(threading.Thread):
    def __init__(self, name, libraries):
        super().__init__()
        self.name = name
        self.libraries = libraries
        self.borrowed_books = []  # List to keep track of borrowed books

    def run(self):
        borrow_return = 0  # 0 means borrow, 1 means return

        for i in range(15):  # Each reader will perform 15 iterations

            # High-level locking: even iterations for borrowing, odd for returning
            if i % 2 == 1:  # Odd iteration
                borrow_return = 1
            else:  # Even iteration
                borrow_return = 0

            if borrow_return == 0:
                # Select a random library and book
                library = random.choice(self.libraries)
                if library.shelf:  # Check if there are books in the library
                    book_title = random.choice(list(library.shelf.keys()))

                    # Try to borrow the book
                    print(f"{self.name}: tries to borrow the book '{book_title}' from the library '{library.name}'.")
                    self.borrow_book(library, book_title)
                    time.sleep(random.uniform(0.5, 2.0))  # Simulate time of usage

            else:
                # Try to return a book
                self.return_book()
                time.sleep(random.uniform(0.5, 1.0))

    def borrow_book(self, library, book_title):
        with library.lock:
            if library.shelf.get(book_title) == 1:  # Check if the book is available
                print(f"{self.name} has borrowed the book '{book_title}'.")
                library.change_book_status(0, book_title)  # Change book status to borrowed
                self.borrowed_books.append({"book_title": book_title, "library": library})  # Add to borrowed list
                return True
            else:
                print(f"{self.name} tried to borrow the book '{book_title}' from the library '{library.name}', but it was already borrowed.")
                return False

    def return_book(self):
        if len(self.borrowed_books) > 0:  # Check if there are borrowed books to return
            book_to_return = self.borrowed_books.pop()  # Get the last borrowed book
            book_title = book_to_return["book_title"]
            library = book_to_return["library"]
            print(f"{self.name}: tries to return the book '{book_to_return['book_title']}' to the library '{book_to_return['library'].name}'.")
            with library.lock:
                if book_title in library.shelf:  # Check if the book is in the library's collection
                    library.change_book_status(1, book_title)  # Change book status to available
                    print(f"{self.name} has returned the book '{book_title}' to the library '{library.name}'.")
                else:
                    print(f"{self.name} tried to return the book '{book_title}', but it was already in the library.")

    def remove_permanent(self, library, book_title):
        with library.lock:
            if library.shelf.get(book_title) == 1:  # Check if the book is available
                library.remove_book(book_title)  # Permanently remove the book from the library
                print(f"{self.name} has permanently taken the book '{book_title}' from the library '{library.name}'.")
            else:
                print(f"{self.name} tried to take the book '{book_title}', but it was already borrowed.")

# Main function to run the simulation
def main():
    M = 3  # Number of libraries
    N = 5  # Number of readers

    # Create N libraries dynamically
    libraries = [Library(f"Library {i + 1}") for i in range(M)]

    # Add books to each library
    base_books = ["Book1", "Book2", "Book3", "Book4", "Book5"]
    for library in libraries:
        for book in base_books:
            library.add_book(book)

    # Show the initial state of each library
    print("\n Initial state of the libraries:")
    for library in libraries:
        library.show_status()

    # Create N readers that share the libraries
    readers = [Reader(f"Reader {i + 1}", libraries) for i in range(N)]

    # Start the threads for each reader
    for reader in readers:
        reader.start()

    # Wait for all threads to finish
    for reader in readers:
        reader.join()

    # Show the final state of each library
    print("\n Final state of the libraries:")
    for library in libraries:
        library.show_status()

# Entry point of the program
if __name__ == '__main__':
    main()  # Run the main function
