def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        num = arr[i]
        j = i - 1
        while j >= 0 and num < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = num
    return arr


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(insertion_sort(arr))
