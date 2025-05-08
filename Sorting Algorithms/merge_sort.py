D = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def merge_sort(arr):
    n  = len(arr)

    if n == 0 or n==1:
        return arr
    
    m = len(arr)//2

    L = arr[:m] # due to this we get space complexity of O(n) because we are creating a new array
    R = arr[m:]

    L = merge_sort(L)
    R = merge_sort(R)
    l, r = 0, 0

    L_len = len(L)
    R_len = len(R) 

    sorted_arr = [0] * n
    i = 0

    while l < L_len and r < R_len: # works when both arrays dont go out of bounds
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1

    while l < L_len: # works when L array is not out of bounds
        sorted_arr[i] = L[l]
        l += 1
        i += 1
    
    while r < R_len: # works when R array is not out of bounds
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    return sorted_arr

sorted_arr = merge_sort(D)
print(sorted_arr)
