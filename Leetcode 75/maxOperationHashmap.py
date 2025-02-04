'''
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.
'''

from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        ops = 0

        for i in nums:
            if count[i] > 0 and count[k - i] > 0:
                if i == k - i and count[i] < 2:
                    continue

                count[i] -= 1
                count[k - i] -= 1
                ops += 1

        return ops