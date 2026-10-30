from lib.book import Book

def test_book_constructs():
    book = Book(1, "Dune", "Frank Herbert")
    assert book.id == 1
    assert book.title == "Dune"
    assert book.author == "Frank Herbert"

def test_books_are_equal():
    book1 = Book(1, "Dune", "Frank Herbert")
    book2 = Book(1, "Dune", "Frank Herbert")
    assert book1 == book2

def test_book_format():
    book = Book(1, "Dune", "Frank Herbert")
    assert str(book) == "Book(1, Dune, Frank Herbert)"