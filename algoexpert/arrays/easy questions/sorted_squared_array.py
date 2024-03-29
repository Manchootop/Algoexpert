def sortedSquaredArray(array):
    array = sorted(array, key=lambda x: abs(x))
    return [x * x for x in array]


print(sortedSquaredArray([-50, -13, -2, -1, 0, 0, 1, 1, 4, 2, 3, 19, 20]))


def sortedSquaredArrayInline(array):
    return [x * x for x in sorted(array, key=lambda x: abs(x))]
