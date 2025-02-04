'''
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.
'''

'''
Gist:
We sort the nums array ascendingly, to keep the computation in linear time.
Set the two pointers (left and right) and the extremes of 'nums'.
For every 'numsum' equal to 'k', we increment the count.
Since the array is sorted, if numsum is less than k, we increment the left pointer and vice versa.
The operation continues until left > right, and returns the value of count at the end.

Time: O(N log N)
Space: O(1)

'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        count = 0
        nums_sorted = sorted(nums)
        
        while left < right:
            numsum = nums_sorted[left] + nums_sorted[right]
            if numsum == k:
                count += 1
                left += 1
                right -= 1

            elif numsum < k:
                left += 1

            elif numsum > k:
                right -= 1

        return count