def  quick_sort(arr):
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]

    left = [i for i in arr[:-1] if i <= pivot]
    right = [i for i in arr[:-1] if i > pivot]

    return quick_sort(left) +  [pivot] + quick_sort(right)

D = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
sorted_arr = quick_sort(D)
print(sorted_arr)