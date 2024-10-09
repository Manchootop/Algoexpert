def runLengthEncoding(string):
    if not string:
        return None
    result = []
    count = 1
    last_char = string[0]
    for char in string[1:]:
        if char == last_char and count < 9:
            count += 1
        else:
            result.append(str(count) + last_char)
            last_char = char
            count = 1
    result.append(str(count) + last_char)
    return "".join(result)


# string = "AAAAAAAAAAAAABBCCCCDD"
# expected = "9A4A2B4C2D"
