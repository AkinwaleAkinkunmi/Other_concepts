# Insertion sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        value_to_sort = arr[i]
        while arr[i-1] > value_to_sort and i>0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i=i-1

arr = [2, 6, 3, 7, 4, 1]
insertion_sort(arr)
print(arr)