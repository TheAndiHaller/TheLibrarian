import requests

  #status        Status    @default(TO_READ)
  #owned         Owned     @default(NO)
  #addedAt       DateTime  @default(now())
  #finishedAt    DateTime?
  #notes         String?

def main():
    query = "Snow Crash"
    print(f"Searching for: {query}")
    search = requests.get(f"https://openlibrary.org/search.json?title={query}").json()

    doc = search['docs'][0] 

    work_key = doc['key']  
    work = requests.get(f"https://openlibrary.org{work_key}.json").json()

    hardcover_key = doc.get("cover_edition_key")

    hardcover = {}

    if hardcover_key:
        hardcover = requests.get(f"https://openlibrary.org/books/{hardcover_key}.json").json()

    book_data = {
    "title": doc.get("title"),
    "author": doc.get("author_name", [None])[0],
    "description": work.get("description"),
    "subjects": work.get("subjects"),
    "pages": hardcover.get("number_of_pages"),
    "year": doc.get("first_publish_year"),
    "isbn": hardcover.get('isbn_13', hardcover.get('isbn_10', [None]))[0],
    "key": doc.get("key")
    }

    for k, v in book_data.items():
        print(f"{k}: {v}")





if __name__ == "__main__":
    main()