# Bubble Sort
def bubble_sort(arr):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(arr)- 1):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

arr = [2,5,7,3,6,4,2,8]
bubble_sort(arr)
print(arr)