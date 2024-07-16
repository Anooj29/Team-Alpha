class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def display_book_details(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available Copies: {self.available_copies}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        print("Library Catalog:")
        for book in self.books:
            book.display_book_details()


def main():
    library = Library()

    book1 = Book(1, "Python Programming", "John Doe", 5)
    book2 = Book(2, "Data Structures", "Jane Smith", 3)

    library.add_book(book1)
    library.add_book(book2)

    search_title = input("Enter the title of the book you want to search for: ")

    found_book = library.search_book(search_title)
    if found_book:
        print("\nBook found:")
        found_book.display_book_details()
    else:
        print("\nBook not found.")

    print("\nLibrary Catalog:")
    library.display_books()


if __name__ == "__main__":
    main()
