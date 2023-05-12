def semordnilap(array):
    words_set = set(array)
    pairs = []
    words_set_copy = words_set.copy()

    for word in words_set:
        reversed_word = word[::-1]
        if reversed_word in words_set_copy:
            pairs.append([word, reversed_word])
            words_set.remove(word)
            words_set.remove(reversed_word)

    return pairs

# print(semordnilap(['repaid', 'abc', 'diaper', 'cba', 'test']))

def semordnilap2(words):
    seen_words = set([])
    result = []
    for original in words:
        flipped = original[::-1]

        if flipped in seen_words:
            result.append([ original, flipped ])
        seen_words.add(original)
    return result

print(semordnilap2(['repaid', 'abc', 'diaper', 'cba', 'test']))
