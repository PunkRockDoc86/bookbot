def get_num_words(text):
    words = text.split()
    length = len(words)
    return length

def character_count(text):
    char_counts = {}

    for char in text:
        char = char.lower()

        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sorted_dict(char_counts):
    dict_tuple = char_counts.items()
#    print(f"this is the tuple: {dict_tuple}")
    list_from_tuple = list(dict_tuple)
    list_from_tuple.sort(key = lambda x: x[1], reverse=True)

    new_dict = {}

    for key, value in list_from_tuple:
        new_dict[key] = value

    for key, value in new_dict.items():
        print(f"{key}: {value}")


