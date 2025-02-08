'''
1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
'''

'''
Gist:
Using sliding window defined by two pointers, flip "0's" till k == 0. 
If k < 0, revert the last flip and move the sliding window towards left.
The final length of longest consecutive ones is (right - left + 1).

Time: O(N)
Space: O(1)
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0      
        
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1