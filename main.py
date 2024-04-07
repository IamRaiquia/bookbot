
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_word_number(text)
    print(text)
    print(f"total number of words: {wordcount}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_number(text):
    words = len(text.split())
    return words

main()