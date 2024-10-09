def firstNonRepeatingCharacter(string):
    nums = {}
    for ch in string:
        if ch not in nums:
            nums[ch] = 0
        nums[ch] += 1
    index = -1
    for ch in string:
        index += 1
        if nums[ch] == 1:
          return index
    return -1
            
   


def firstNonRepeatingCharacter2(string):
    chars = {}
    for char in string:
        chars[char] = chars.get(char, 0) + 1
        
    for idx, char in enumerate(string):
        if chars[char] == 1:
            return idx
    return -1

print(firstNonRepeatingCharacter2("abcdcaf"))