def generate_document(characters, document):

    letter_storage = {}
    is_generatable = True

    for char in characters:
        if char not in letter_storage:
            letter_storage[char] = 0
        letter_storage[char] += 1

    for char in document:
        if char in letter_storage and letter_storage[char] > 0:
            letter_storage[char] -= 1
        else:
            is_generatable = False
            break

    return is_generatable


print(generate_document("aheaolabbhb", "hello"))