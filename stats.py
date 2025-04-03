def get_number_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_letters(text):
    text_lower = text.lower()
    count_letters = {}
    for letter in text_lower:
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1
    return count_letters


def sorted_letters(text):        
    num_letters = get_number_letters(text)
    sorted_dict = dict(sorted(num_letters.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict