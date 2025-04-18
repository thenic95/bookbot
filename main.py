import sys

from stats import get_num_words, get_chars_dict, sort_chars_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        chars_sorted = sort_chars_dict(chars_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        # Print each character and its count
        for char_dict in chars_sorted:
            char = char_dict["char"]
            count = char_dict["count"]
            # Only print alphabetical characters
            if char.isalpha():
                print(f"{char}: {count}")
        
        print("============= END ===============")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()