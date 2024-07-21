FILEPATH = "todos.txt"
import unicodedata
import string

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r', encoding='UTF-8') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w', encoding='UTF-8') as file:
        file.writelines(todos_arg)


def sanitize_string(input_str):
    # Usuwanie znaków diakrytycznych
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    without_diacritics = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    # Usuwanie znaków interpunkcyjnych
    sanitized_string = ''.join([c for c in without_diacritics if c not in string.punctuation])
    return sanitized_string


if __name__ == "__main__":
    print("Hello")
    print(get_todos())