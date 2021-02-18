arr = [1,
       5,
       6,
       9,
       4,
       1,
       2,
       3,
       5,
       6,
       3,
       6,
       6,
       6,
       6,
       6,
       6,
       6,
       4341,
       2132,
       4650,
       0]


def selection_sort(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[m]:
                m = j
        tmp = arr[i]
        arr[i] = arr[m]
        arr[m] = tmp
    return arr


print(selection_sort(arr))