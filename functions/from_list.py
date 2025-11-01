from functions.api_search import search_book

  #status        Status    @default(TO_READ)
  #owned         Owned     @default(NO)
  #addedAt       DateTime  @default(now())
  #finishedAt    DateTime?
  #notes         String?

def get_file_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_title_list(path_to_file, verbose=False):
    result = get_file_text(path_to_file)

    item_list = []
    item_list = result.split("\n")

    title_list = []

    MAX = 10
    
    for line in item_list:
        title = line[9:].split("|")[0]
        title_list.append(title)
        if len(title_list) == MAX:
            break

    return title_list