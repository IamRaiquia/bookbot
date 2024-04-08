
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_word_count(text)
    lettercount = get_letter_count(text)
    sorted_lettercount = sort_dict(lettercount)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document\n")

    for d in sorted_lettercount:
        print(f"The '{d['char']}' character was found {d['num']} times.")
    print("--- End report ---")

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

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    d = []
    for key in dict:
        d.append({"char": key, "num": dict[key]})
    d.sort(reverse=True, key=sort_on)
    return d

main()