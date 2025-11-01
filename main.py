import sys
from functions.api_search import *
from functions.from_list import *

def main():

    search_by_title = "--title" in sys.argv
    search_by_author = "--author" in sys.argv
    search_from_file = "--file" in sys.argv
    verbose = "--verbose" in sys.argv

    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)


    if not args:
        print("\n-------------------- Books ------------------------")
        print('Manual Search:  "Title | Author" [--title, --author]')
        print('Search from file: "/path/to/file.txt" [--file]\n')
        sys.exit(1)

    user_input = " ".join(args)

    book_list = []
    failed_search = []

    if search_by_author:
        print("Searching by Author")

    elif search_from_file:
        print("Reading File")
        title_list = get_title_list(user_input, verbose)
        print(f"Found {len(title_list)} titles\n")
        for t in title_list:
            print(f"Title: {t}")
            try:    
                book_data = search_book(t, verbose)
                book_list.append(book_data)

            except Exception as e:
                print(f"Error Searching: {t} \n {e}")
                failed_search.append(t)
                continue

    else:
        book_data = search_book(user_input)
        
        for k, v in book_data.items():
            print(f"{k}: {v}")


    print("\n----------------------- Titles found --------------------------\n")
    for book in book_list:
        for k, v in book.items():
            print(f"{k}: {v}")

        print("\n---------------------------------------------------------------\n")


if __name__ == "__main__":
    main()