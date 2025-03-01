from stats import get_num_words, get_book_text,count_characters, sort_character_counts
import sys 
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)

    book_path = book_path = sys.argv[1]


    text = get_book_text(book_path)
    num_words = get_num_words(text)

    char_counts = count_characters(text)
    print(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...\n")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words\n")
    print("--------- Character Count -------")

    char_counts = count_characters(text)
    sorted_counts = sort_character_counts(char_counts)

    for char, count in sorted_counts:
        print(f"{char}: {count}")

    print("============= END ===============")



if __name__ == "__main__":
    main()