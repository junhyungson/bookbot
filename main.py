from stats import get_num_words, get_book_text,count_characters
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    char_counts = count_characters(text)
    print(char_counts)



if __name__ == "__main__":
    main()