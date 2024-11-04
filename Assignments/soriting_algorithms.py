def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1): 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
import random
need_sort = [random.randint(1, 100) for _ in range(10)]
print("Unsorted", need_sort)
sorted_arr = bubble_sort(need_sort)
print("Sorted", sorted_arr)


def merge(left, right):
    sorted_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
if __name__ == "__main__":
    import random
    need_sort = [random.randint(1, 100) for _ in range(10)]
    print("Unsorted array:", need_sort)
    sorted_arr = merge_sort(need_sort)
    print("Sorted array:", sorted_arr)