arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 13, 15, 15, 16, 17, 18]


def jump_search(arr, item, jump):
    for i in range(0, len(arr), jump):
        if arr[i] == item:
            return i
        elif arr[i] > item:
            for j in range(i-1, i-jump, -1):
                if arr[j] == item:
                    return j
    return -1


print(jump_search(arr, 2, 3))
