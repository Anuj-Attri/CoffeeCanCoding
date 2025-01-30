'''
724. Find Pivot Index
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
'''
'''
Gist:
The total sum of the array = left_sum + right_sum + nums[i]; 
where i is the index of an element during iteration,
left_sum is the sum of all elements left of 'i' and 
right_sum is sum of all elements right of 'i'.

For i to be pivot index, left_sum = right_sum.
Thus, equation becomes:
total = 2*left + nums[i] 
=> left = total - left - nums[i] 
=> Above check returns True only if 'i' is the pivot index.

Time: O(N)
Space: O(1)
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:       # Function returns an integer
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:  # Checking for pivot index
                return i
            left_sum += nums[i]                         # Updating left_sum
        return -1 