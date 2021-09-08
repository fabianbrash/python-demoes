# Big O notation


def separator():

    print("===================================================")

def foo():
    arr = [1, 2, 3, 4, 5]
    sum = 0

    for i in arr:
        sum+=i
    print(sum)

separator()
foo()


def fooo():
    arr = [1, 2, 3, 4, 5]
    product = 0

    for i in arr:
        for j in arr:
            print(i, j)
            product = i*j
            print(product)

separator()
fooo()
separator()