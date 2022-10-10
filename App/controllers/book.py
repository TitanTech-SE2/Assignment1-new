from App.models import Book, Author
from App.database import db

def add_book(isbn, title, authorName, publiYear, coAuthor):
    newbook = Book(isbn = isbn, title = title, authorName = authorName, publiYear = publiYear, coAuthor = coAuthor)
#  for arg in coAuthor:
#     newbook = Book(coAuthor =  arg)
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


def get_all_author_book_by_Year(publiYear, authorName):
    books = Book.query.all()
    if not books:
        return []
    haul = Book.query.filter(Book.publiYear == publiYear, Book.authorName == authorName).first()
    return ("Title: " + haul.title + "\n" + "ISBN: " + str(haul.isbn) + "\n" + "Author: " + haul.authorName + "\n" + "Co-Author/s: " + haul.coAuthor)


def get_all_authors_json():
    books = Book.query.all()
    dump = []
    if not books:
        return []
    for book in books:
        haul = [book.authorName] #working now
        dump.append(haul)
    return dump

def add_coAuthor(coAuthor, isbn):
    change = Book.query.filter_by(isbn = isbn).first()
    change.coAuthor = coAuthor
    db.session.commit()


#Not too sure about how to implement
def update_book(ISBN):
    book = get_book(ISBN)
    if book:
        book.ISBN = ISBN
        db.session.add(book)
        return db.session.commit()
    return None
