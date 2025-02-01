'''
643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
'''

'''
Gist:
Instead of computing averages, we find the sum of all elements in the first 'k' window to initialize max_sum and window_sum.
The loop is start at kth element and works towards the end of array. 
For each iteration, the leftmost element of the last window is subtracted, and the next element is added, updating the window_sum.
window_sum is compared to max_sum, and max_sum is updated accordingly.
The final average is returned by dividing the max_sum by 'k'.

Time: O(N)
Space: O(1)
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = window_sum = sum(nums[:k])
        N = len(nums)

        for i in range(k, N):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum/k