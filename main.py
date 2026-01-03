import sys
from stats import get_word_count
from stats import char_counter
from stats import sort_dictionary

def get_book_text(path):
    with open(path) as book:
        contents = book.read()
        return contents
    
def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        count = get_word_count(text)
        print(f"Found {count} total words")
        char_dict = char_counter(text)
        sorted_list = sort_dictionary(char_dict)
        for item in sorted_list:
            print(f"{item['char']}: {item['num']}")
main()

    