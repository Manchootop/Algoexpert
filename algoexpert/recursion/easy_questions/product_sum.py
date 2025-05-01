# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth=1):
    return depth * sum(
        productSum(el, depth+ 1) if isinstance(el, list) else el
        for el in array
    )
            
            
if __name__ == "__main__":
    print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
