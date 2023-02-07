def non_constructible_change(coins):
    change = 0
    coins.sort()
    for i in range(len(coins)):
        coin = coins[i]
        if coin > change + 1:
            return change + 1
        else:
            change += coin

    return change + 1


'''
Task:
    - write a function that return the minimum amount of change you cannot create. Each num in coins is a positive int
    representing the value of the coin ex [1, 2, 5, 1007] -> 1 cent, 2 cents, 5 cents, 1007 cent, no matter what the unit is.
    - For example, if you are given coins = [1, 2, 5], the minimum amount of change you cannot create is 4. If you are 
    given no coins, the minimum amount of change that you can't create is 1,
'''

# print(non_constructible_change([5, 7, 1, 1, 2, 3, 22]))
# print(non_constructible_change([1]))
# print(non_constructible_change([1, 5, 1, 1, 1, 10, 15, 20, 100]))
