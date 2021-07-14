from functools import reduce

arr = [1,2,3,4]
# Returns the sum of all the elements using `reduce`
result = reduce((lambda a, b: a + b), arr)
print(result)


# Returns the sum of two elements
def sumTwo(a,b):
    return a+b

result = reduce(sumTwo, [1, 2, 3, 4])
print(result)


arr2 = [5,6,7,8,9]

data = reduce((lambda a, b: a + b), arr2)

print(data)
