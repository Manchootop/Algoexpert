# def is_palindrome(string):
#     string_len = 0
#     for _ in string:
#         string_len += 1
#
#
#     if string_len % 2 == 0:
#
#
#     first_part = string[:string_len // 2]
#     second_part = string[:-string_len // 2]
#
#     if first_part == second_part:
#         return True
#     return False
#
#
# print(is_palindrome('ab'))


def is_palindrome(string):
    reversed_string = ''
    for i in reversed(range(len(string))):
        reversed_string += string[i]

    return string == reversed_string

is_palindrome('abccba')