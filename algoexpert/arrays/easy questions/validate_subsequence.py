def is_subsequence(array, subsequence):
    main_index = 0
    sub_index = 0
    while main_index < len(array) and sub_index < len(subsequence):
        if array[main_index] == subsequence[sub_index]:
            sub_index += 1
        main_index += 1

    return sub_index == len(subsequence)

print(is_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))