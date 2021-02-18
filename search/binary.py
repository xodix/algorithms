arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 13, 15, 15, 16, 17, 18]


def binary_search(sorted_arr, item):
    relative_end = len(arr)
    relative_start = 0
    while relative_start <= relative_end:
        center = relative_start + (relative_end - 1) // 2
        if sorted_arr[center] == item:
            return center
        elif sorted_arr[center] < item:
            relative_start = center + 1
        else:
            relative_end = center - 1
    return -1


print(binary_search(arr, 2))
