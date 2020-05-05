def positive_sum(arr):
    return sum(n for n in arr if n >= 0)


print(positive_sum([1,-2,3,4,5]))