'''334. Increasing Triplet Subsequence
Given an integer array nums, 
return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
'''

'''
Gist:
We initialize the first and second number (num[i] and num[j]) to infinite, and traverse the array.
The series for i < j < k and nums[i] < nums[j] < nums[k] can be solved using checks for only the first two values.
A single traversal loop sets the complexity to O(N) where the values of nums[i] and nums[j] are stored if they satisfy the if-elif check.
Since the traversal is forward sweep, we need not store the indices.
If nums[i] is smaller than the current element, nums[i] is updated.
If the current element lies between nums[i] and nums[j], nums[j] is updated.
If a number greater than nums[j] is found, it becomes nums[k], completing the increasing triplet sequence.
If the loop exits without satisfying any of the conditions, 'False' is returned.
There is no need for storing any sequence, giving us a constant space complexity.

Time: O(N)
Space: O(1)

Note: For robustness, '>=' and '<=' operators are recommended. However, this solution assumes strictly increasing order only.
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float('inf')
        second_num = float('inf')

        for i in range(len(nums)):

            if first_num > nums[i]:
                first_num = nums[i]

            elif first_num < nums[i] and nums[i] < second_num:
                second_num = nums[i]

            elif second_num < nums[i]:
                return True
       
        return False