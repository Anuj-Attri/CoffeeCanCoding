'''
643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
'''

'''

'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = window_sum = sum(nums[:k])
        N = len(nums)

        for i in range(k, N):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum/k