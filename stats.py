def sort_on(characters):
    return characters["num"]

def get_word_count(book):
    words = len(book.split())
    return words

def char_counter(book):
    char_dict = {}
    for char in book.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict

def sort_dictionary(characters):
    dict_list = []
    for char in characters:
        if not char.isalpha():
            pass
        else:
            dict_list.append(
                {"char": char, "num": characters[char]}
        )
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list