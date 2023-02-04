# def two_number_sum(array, targetSum):
#     if not array:
#         return []
#     for i in range(0, len(array) - 1):
#         for j in range(i + 1, len(array)):
#             if array[j] + array[i] == targetSum:
#                 return [array[i], array[j]]


def twoNumberSum(array, targetSum):
    for num in array:
        target = targetSum - num
        if target in array and target != num:
            return [num, target]

    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
