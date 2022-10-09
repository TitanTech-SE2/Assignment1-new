from App.models import Book
from App.database import db

def add_book(isbn, title, authorName, publiYear):
    newbook = Book(isbn = isbn, title = title, authorName = authorName, publiYear = publiYear)
    db.session.add(newbook)
    db.session.commit()
    return newbook

def get_all_books():
    return Book.query.all()


def get_all_book_by_title(title):
    books = Book.query.all()
    if not books:
        return []
    haul = [book.toJSON() for title in books]
    return haul

def get_all_books_json():
    books = Book.query.all()
    if not books:
        return []
    books = [Book.toJSON() for Book in books]
    return books
                                
def get_book_by_isbn(isbn):
    return Book.query.filter_by(isbn= isbn).first()


def get_book_by_Year(publiYear):
    books = Book.query.all()
    if not books:
        return []
    haul = [book.toJSON() for authorName in books]
    authorSort = [haul.toJSON() for publiYear in haul]
    return authorSort


def get_all_author_book_by_Year(publiYear):
    books = Book.query.all()
    if not books:
        return []
    haul = [Book.toJSON() for (publiYear) in books] #Need to add author name, problems occuring when using and
    return haul


def get_all_authors_json():
    books = Book.query.all()
    dump = []
    if not books:
        return []
    for book in books:
        haul = [book.authorName] #working now
        dump.append(haul)
    return dump

#Not too sure about how to implement
def update_book(ISBN):
    book = get_book(ISBN)
    if book:
        book.ISBN = ISBN
        db.session.add(book)
        return db.session.commit()
    return None
