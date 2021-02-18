def fibonacci_search(arr, item):
    n = len(arr)
    fibN1 = 1
    fibN2 = 0
    fibn = fibN1 + fibN2
    while fibn < n:
        fibN2 = fibN1
        fibN1 = fibn
        fibn = fibN1 + fibN2
    offset = -1

    # if fib > 1
    while fibn > 1:
        i = min(offset + fibN2, n-1)
        if arr[i] < item:
            fibn = fibN1
            fibN1 = fibN2
            fibN2 = fibn - fibN1
            offset = i
        elif arr[i] > item:
            fibn = fibN2
            fibN1 = fibN1 - fibN2
            fibN2 = fibn - fibN1
        else:
            return i
    if fibN1 and arr[n-1] == item:
        return n-1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12,
       13, 13, 13, 13, 14, 15, 16, 18, 20, 25, 125]
print(fibonacci_search(arr, 15))
