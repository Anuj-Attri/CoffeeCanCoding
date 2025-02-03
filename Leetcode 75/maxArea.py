'''
11. Container With Most Water
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

'''
Gist:

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            min_height = min(height[left], height[right])
            area = max(area, (right - left) * min_height)
            
            if height[left] == min_height:
                while left < right and height[left] <= min_height:
                    left += 1
            
            else:
                while left < right and height[right] <= min_height:
                    right -= 1

        return area