def commonCharacters(strings):
    common_chars = set(strings[0])
 
    for string in strings[1:]:
        common_chars &= set(string)  

    return list(common_chars)


def commonCharacters2(strings):
    strings_len = len(strings)
    word_dict = {}
    common_chars = []

    for string in strings:
        for ch in set(string):
            if ch not in word_dict:
                word_dict[ch] = 0
            word_dict[ch] += 1

    for word,word_count in word_dict.items():
        if word_count == strings_len:
            common_chars.append(word)
    
        
    return common_chars


# Test case
print(commonCharacters(["aa", "ab", "ba"]))  # Output: ['a']
# Test case
print(commonCharacters2(["aa", "ab", "ba"]))  # Output: ['a']