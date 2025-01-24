'''
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''

'''
Gist: 
The issue with this problem lies in its edge cases. 
Once all the boundaries are identified, we only need to add workflows that handle those edge cases. 

Time: O(N)
Space: O(1)

P.s.: 
There is a method of solving this problem using virtual boundaries. 
The idea is to create dummy edges around the array and use only one loop for traversal without worrying about edge cases.
This method focuses on maintainability of code but compromises on space complexity (Linear space).
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            # non-adjunct condition check
            if flowerbed[i] == 0 and \
               (i == 0 or flowerbed[i - 1] == 0) and \
               (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                
                flowerbed[i] = 1  # Plant the flower
                n -= 1  # Decrease the number of required flowers
                if n == 0:  # Stop early if all flowers are planted 
                    return True
                i += 2  # Skip the next position
            else:
                i += 1  # Move to the next position
        
        return n <= 0