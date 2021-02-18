arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
       110, 120, 130, 140, 150, 160, 170, 180, 190, 200]


def interpolation_search(arr, item):
    hi = len(arr) - 1
    gap = arr[1] - arr[0]
    if item > arr[hi] or item < arr[0] or not item % gap == 0:
        return -1
    return (item - arr[0]) / gap


print(interpolation_search(arr, 50))
