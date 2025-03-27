import sys
from stats import get_num_words, character_count, report

def get_book_text(file_path):
    with open(file_path) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    
    text = get_book_text(file_path)
    print(text)
    
    report(file_path)

main()