import sys
from stats import count_words
from stats import char_freq
from stats import sort_chars


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print(" BOOKBOT ".center(33, "="))
    print(f"Analyzing book found at {path}...")

    book_text = get_book_text(path)
    words = count_words(book_text)
    char_counts = char_freq(book_text)
    sorted_char_counts = sort_chars(char_counts)

    print(" Word Count ".center(33, "-"))
    print(f"Found {words} total words")
    print(" Character Count ".center(33, "-"))
    
    for item in sorted_char_counts:
        print(f"{item["char"]}: {item["num"]}")

    print(" END ".center(33, "="))


if __name__ == "__main__":
    main()