def caesarCipherEncryptor(string, key):
    key = key % 26
    new_string = []

    for ch in string:
        new_ch = chr(((ord(ch) - ord('a') + key) % 26) + ord('a'))
        new_string.append(new_ch)
        
    return ''.join(new_string)



def caesarCipherEncryptor2(string, key):
    new_string = ""
    key = key % 26
    for ch in string:
        ch_av = ord(ch) + key
        if ch_av > ord('z'):
            ch_av = ch_av - ord('z') + ord('a') - 1
        
        new_string += chr(ch_av)

    return new_string

print(caesarCipherEncryptor("xyz", 2))  # Output: "zab"
print(caesarCipherEncryptor2("xyz", 2))  # Output: "zab"
