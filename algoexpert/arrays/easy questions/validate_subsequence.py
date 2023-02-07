def is_subsequence(array, subsequence):
    main_index = 0
    sub_index = 0
    while main_index < len(array) and sub_index < len(subsequence):
        if array[main_index] == subsequence[sub_index]:
            sub_index += 1
        main_index += 1

    return sub_index == len(subsequence)


print(is_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))

'''# To determine if a sequence of numbers is a subsequence of another list of numbers, you can use a sliding window 
approach.
You keep a pointer to the starting index of the subsequence in the main array, and move the pointer forward whenever a 
match is found. If you reach the end of the subsequence and all elements have been matched, then the subsequence is a 
part of the main array.'''
