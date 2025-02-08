'''
1493. Longest Subarray of 1's After Deleting One Element
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
'''

'''
Gist:
Using sliding window, count the number of zeroes while incrementing the right pointer. 
When the number of 0's within a subsequence exceeds 1, delete the left most element and the zero count. 
Update the window size, denoting the longest subsequence of 1's.

Time: O(N)
Space: O(1)
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        window_size = 0
        count = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1

            while count > 1:
                if nums[left] == 0:
                    count -= 1

                left += 1

            window_size = max(window_size, right - left + 1)

        return window_size - 1
