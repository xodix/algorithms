def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr


arr = [5, 5524, 4, 5, 4, 54, 45, 435, 544, 45,
       4, 54, 54, 54, 5, 21, 1, 21, 21, 212, 12, 1, 5]

print(bubble_sort(arr))
# zinterpretuj balladę alku chara jako zapowiedź czynu wallenroda
