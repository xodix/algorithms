arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 13, 15, 15, 16, 17, 18]


def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1


print(linear_search(arr, 13))
