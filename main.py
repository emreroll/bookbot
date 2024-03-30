def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    harf_sayisi = count_characters(text) 

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    result = {}
    for i in text:
        lowered = i.lower()
        if lowered in result:
            result[lowered] += 1
        else:
            result[lowered] = 1
    return result


main()



    