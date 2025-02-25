def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    # Clean the text of any extra whitespace
    text = text.strip()
    words = text.split()
    return len(words)


def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts