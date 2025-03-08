

def main():

    import sys

    if  len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f"""============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------""")



    print(f"{num_words} words found in the document")
    characters = character_count(text)
#    print("--- Character Counts ---")
#    for char, count in characters.items():
#         print(f"'{char}': {count}")


    print(sorted_dict(characters))



    print("============= END ===============")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

from stats import get_num_words

from stats import character_count

from stats import sorted_dict

main()

