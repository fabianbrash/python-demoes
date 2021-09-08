def bubble(list_a):

    indexing_len = len(list_a) - 1

    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_len):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a


print(bubble([9,3,20,50,6,19,99]))


def bubble_for():
    list = [6,5,4,3,2,1]
    print(list)
    for i in range(0, len(list)-1):
        for j in range(0,len(list)-1 - i):
            list[j], list[j+1] = list[j+1], list[j]
    print(list)

bubble_for()
