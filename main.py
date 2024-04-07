
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_word_count(text)
    lettercount = get_letter_count(text)
    print(text)
    print(f"Count for each word in the document: {wordcount}")
    print(f"Count for each letter in the document: {lettercount}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = len(text.split())
    return words

def get_letter_count(text):
    lowercase_text = text.lower()
    count_per_letter = {}
    for letter in range(ord('a'), ord('z') + 1):
        count_per_letter[chr(letter)] = lowercase_text.count(chr(letter))
    return count_per_letter

main()