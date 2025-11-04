MAX = 10

def get_file_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_title_list(path_to_file, verbose=False):
    result = get_file_text(path_to_file)

    item_list = []
    item_list = result.split("\n")

    title_list = []

    
    for line in item_list:
        title = line[9:].split("|")[0]
        title_list.append(title)
        if len(title_list) == MAX:
            break

    return title_list