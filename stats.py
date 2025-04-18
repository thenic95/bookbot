def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_chars_dict(chars_dict):
    # Create a list to hold our dictionaries
    chars_list = []
    
    # Convert each character and count into a dictionary and add it to our list
    for char, count in chars_dict.items():
        chars_list.append({"char": char, "count": count})
    
    # Sort the list based on the count value (in descending order)
    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list