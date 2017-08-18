def match_chars(x, y):
    if len(x) == 0:
        return
    
    word_count_dict = {}
        
    for word in x:
        count = 0
        char_array = []
        for char in word:
            if char in char_array:
                continue
            else:
                count += 1
                char_array.append(char)
        if count in y:
            word_count_dict[word] = count
        else:
            continue

    for word in sorted(word_count_dict, key = word_count_dict.get, reverse=True):
        print word, word_count_dict[word]
        
    return word_count_dict


if __name__ == '__main__':
    print match_chars(["apple", "png", "jpeg", "images"], [3, 4, 5, 6])