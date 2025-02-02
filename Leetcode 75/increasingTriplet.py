'''334. Increasing Triplet Subsequence
Given an integer array nums, 
return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
'''

'''
Gist:

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