
def get_num_words(file_path):
    with open(file_path) as f:
        file_words = f.read()
        words_list = file_words.split()
        num_words = len(words_list)
    return num_words

def character_count(file_path):
    character_dict = {}
    with open(file_path) as f:
        file_words = f.read()   
        words_list = file_words.split()
    
    for chars in words_list:
        for c in chars:
            if c == ' ':
                key = ' '
            elif c == '!':
                key = '!'
            elif c == '.':
                key = '.'
            else:
                key = c.lower()

            if key not in character_dict:
                character_dict.update({key:0})
            character_dict[key] += 1
    return character_dict   

def sort_chars(dict):
    chars_list = []
    for char, count in dict.items():
        my_char_info = {'char': char, 'count': count} # creating new dictionary of list
        chars_list.append(my_char_info)

    # sorting the list by count
    chars_list.sort(reverse=True, key=lambda x:x['count'])
    return chars_list


def report(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    word_count = get_num_words(file_path)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_dict = character_count(file_path)
    print("--------- Character Count -------")
    my_sorted_chars = sort_chars(char_dict)

    for char_info in my_sorted_chars:
        if char_info['char'].isalpha():
            print(f"{char_info['char']}: {char_info['count']}")
    print("============= END ===============")