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
Using two-pointers, we can calculate and compare the area contained between two lines in linear time.
Increment/decrement the pointers towards the next shorter height, so as to maximize the area contained between the two lines.
The max between current and previous area is stored in 'area' and returned at the end of the loop.
The standard approach, while linear time, performs many redundant calculation that consume CPU cycles, taking more time.
To reduce the time taken, we eliminate heights that do not increase the area using a 'while-loop'.
For example, "while left < right and height[left] <= min_height" compares if the next height is less than the previous height of the left pointer,
and increments the left pointer till we find a height higher than the previous height.
This step logically eliminates smaller areas without explicitlly calculating them, reducing the computation time to under 10% of original*.

Time: O(N)
Space: O(1)

*As checked by leetcode test cases, solutions without eliminating redundant cycles takes over 100ms whereas this solution takes less than 10ms.
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