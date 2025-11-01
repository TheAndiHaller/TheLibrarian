import sys
from functions.api_search import *

def main():

    search_by_title = "--title" in sys.argv
    search_by_author = "--author" in sys.argv
    search_from_file = "--file" in sys.argv

    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)


    if not args:
        print("\n-------------------- Books ------------------------")
        print('Manual Search:  "Title | Author" [--title, --author]')
        print('Search from file: "/path/to/file.txt" [--file]\n')
        sys.exit(1)

    book_title = " ".join(args)

    if search_by_author:
        print("Searching by Author")
    elif search_from_file:
        print("Reading File")
        book_list = search_from_file()
    else:
        book_data = search_book(book_title)
        
        for k, v in book_data.items():
            print(f"{k}: {v}")




if __name__ == "__main__":
    main()