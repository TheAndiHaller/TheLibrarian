import requests, pprint

def search_book(title, verbose=False):
    print(f"Searching for: {title}")
    print("")
    search = requests.get(f"https://openlibrary.org/search.json?title={title}").json()

    if verbose:
        print("------------- Title Search Result ------------------------\n")
        pprint.pprint(search)
        print("----------------------------------------------------------\n")

    doc = search['docs'][0] 

    work_key = doc['key']  
    work = requests.get(f"https://openlibrary.org{work_key}.json").json()

    if verbose:
        print("------------- Work Search Result -------------------------\n")
        pprint.pprint(work)
        print("----------------------------------------------------------\n")

    hardcover_key = doc.get("cover_edition_key")
    hardcover = {}

    if hardcover_key:
        hardcover = requests.get(f"https://openlibrary.org/books/{hardcover_key}.json").json()

    if verbose:
        print("------------- Hardcover Search Result --------------------\n")
        pprint.pprint(hardcover)
        print("----------------------------------------------------------\n")

    book_data = {
    "title": doc.get("title"),
    "author": doc.get("author_name", [None])[0],
    "description": work.get("description"),
    "subjects": work.get("subjects"),
    "pages": hardcover.get("number_of_pages", None),
    "year": doc.get("first_publish_year"),
    "isbn": hardcover.get('isbn_13', hardcover.get('isbn_10', [None]))[0],
    "key": doc.get("key")
    }

    return book_data


def search_author():
    return {}