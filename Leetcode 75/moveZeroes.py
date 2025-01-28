'''
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

'''
Gist:
Using the double pointer method, we traverse one ptr (i) over elements and keep the other ptr (ctr) on the last non-zero element.
Swap elements when non zero element is found.

Time: O(N)
Space: O(1)

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ctr = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[ctr] = nums[ctr], nums[i]
                ctr += 1