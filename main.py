import sys
from stats import get_number_words
from stats import get_book_text
from stats import get_number_letters
from stats import sorted_letters

def main():
    if len(sys.argv) < 2:
        print("Incorrect use of program. Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        book_path = sys.argv[1]
        print(f"Analyzing book found at {book_path}...")
        text = get_book_text(book_path)
        num_words = get_number_words(text)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        num_letters = get_number_letters(text)
        sorted_num_letters = sorted_letters(text)
        print("--------- Character Count -------")
        for letter, count in sorted_num_letters.items():
            if letter.isalpha() == True:
                print(f"{letter}: {count}")
        print("============= END ===============")

main()