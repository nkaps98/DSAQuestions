
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        while d:
            i = len(arr) - 1
            temp = None
            while i >= 0:
                if temp == None:
                    temp = arr[i-1]
                    arr[i-1] = arr[i]
                else:
                    temp2 = arr[i-1]
                    arr[i-1] = temp
                    temp = temp2
                i -= 1
            d-=1
        return arr
# Time Complexity: O(n*d)
# Space Complexity: O(1)


# Juggling Algorithm
# Approach:
# 1. Calculate the number of cycles using the GCD of n and d.
# 2. For each cycle, store the starting element.
# 3. Move elements in the cycle to their new positions until the cycle is complete.
# 4. Place the starting element in its final position.
# 5. Repeat for all cycles until the array is rotated.
# Example:
# Input: arr = [1, 2, 3, 4, 5], d = 2
# Output: [3, 4, 5, 1, 2]

import math
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        
        d %= n
        
        cycles = math.gcd(n, d)
        
        for i in range(cycles):
            
            startele = arr[i]
            
            current_index = i
            
            while True:
                next_index = (current_index + d) % n
                
                if next_index == i:
                    break
                
                arr[current_index] = arr[next_index]
                current_index = next_index
                
            arr[current_index] = startele
            
        return arr
    
# Time Complexity: O(n)
# Space Complexity: O(1)



# Approach: Reversal Algorithm
# Approach:
# 1. Reverse the first d elements.
# 2. Reverse the remaining n-d elements.
# 3. Reverse the entire array to get the final rotated array.
# 4. Return the modified array.

#User function Template for python3
import math
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        
        d %= n
        
        arr = self.reverse_algo(arr, 0, d-1)
        arr = self.reverse_algo(arr, d, n-1)
        arr = self.reverse_algo(arr, 0, n-1)
        
        return arr
    
    def reverse_algo(self, arr, start, end):
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            
            start += 1
            end -= 1
        return arr
                
# Time Complexity: O(n)
# Space Complexity: O(1)