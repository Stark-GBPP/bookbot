def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_characters = get_sorted_chars(chars_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for char_data in sorted_characters:
        print(f"The '{char_data['char']}' character was found {char_data['num']} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_chars_dict(text):
    lowered = text.lower()
    chars = {}
    for l in lowered:
        if l in chars:
            chars[l] += 1
        else:
            chars[l] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_sorted_chars(chars_dict):
    char_list = []
    for char, count in chars_dict.items():
        if char.isalpha() == True:
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
main()