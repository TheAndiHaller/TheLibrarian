from tinydb import TinyDB, Query

db = TinyDB('books.json')

# Add a book
def save_book(book_data):
    db.insert({
        "title": book_data.get("title"),
        "author": book_data.get("author"),
        "description": book_data.get("description"),
        "subjects": book_data.get("subjects"),
        "pages": book_data.get("pages"),
        "year": book_data.get("year"),
        "isbn": book_data.get("isbn"),
        "key": book_data.get("key"),
        "status": None,       # e.g. "read", "to_read", "owned"
        "owned": False,       # whether you physically own it
        "finishedAt": None,   # date you finished reading
        "notes": None         # any notes you want to add
    })

# Query
def get_book(title):
    Book = Query()
    result = db.search(Book.title == title)
    if len(result) == 0:
        return None
    return result[0]

# Get all Books
def get_all_books():
    result = []
    for book in db.all():
        new_book = {**book, "eid": book.doc_id}
        result.append(new_book)

    if len(result) == 0:
        return None
    return result