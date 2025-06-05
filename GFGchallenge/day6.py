"""
You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.

Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.
"""


# Time Complexity: O(nlogn) due to sorting the array.
# Space Complexity: O(1) as we are using constant space for variables.

# Approach:
# 1. Sort the array.
# 2. Traverse the sorted array and count the occurrences of each element.
# 3. If the count of an element is greater than n/3, add it to the result list.

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        
        arr.sort()
        count = 1
        final_result = []
        for i in range(len(arr)):
            if i == len(arr) - 1:
                if count > n/3:
                    final_result.append(arr[i])
                break
                        
            if arr[i] == arr[i+1]:
                count += 1
            elif arr[i] != arr[i+1] and count > 1:
                if count > n/3:
                    final_result.append(arr[i])
                count = 1
            elif arr[i] != arr[i+1] and count == 1:
                if count > n/3:
                    final_result.append(arr[i])
                count = 1
                
                
        return final_result


# Time Complexity: O(n)
# Space Complexity: O(n) for storing the count of each element in a dictionary.
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        
        arr.sort()
        count = 1
        count_dict = {}
        final_result = []
        for i in arr:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1

        for key, value in count_dict.items():
            if value > n / 3:
                final_result.append(key)
                
        ## why are we swapping the first two elements?: because the arr at most can have two elements that are greater than n/3, and we want to return them in increasing order. 
        if len(final_result) == 2 and final_result[0] > final_result[1]:
            final_result[0], final_result[1] = final_result[1], final_result[0]
        return final_result
    

# Approach 3: Moore's Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    
    def findMajority(self, arr):
        n = len(arr)
        ele1, ele2 = float('inf'), float('inf')
        count1, count2 = 0, 0
        
        final_result = []
        for i in arr:
            if ele1 == i:
                count1 += 1
                continue
            
            if ele2 == i:
                count2 += 1
                continue
            
            if i != ele1 and count1 == 0:
                ele1 = i
                count1 = 1
                
            if i != ele2 and count2 == 0:
                ele2 = i
                count2 = 1
                
            if i != ele1 and i != ele2 and count1 > 0 and count2 > 0:
                count1 -= 1
                count2 -= 1
                
        count1, count2 = 0, 0
        
        for i in arr:
            if i == ele1:
                count1+=1
                
            if i == ele2:
                count2+=1
                
        if count1 > n/3:
            final_result.append(ele1)
        
        if count2 > n/3:
            final_result.append(ele2)
            
        if len(final_result) == 2 and final_result[0] > final_result[1]:
            final_result[0], final_result[1] = final_result[1], final_resu;t[0]
            
        return final_result
                
        
            