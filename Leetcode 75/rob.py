'''
198. House Robber
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
'''
'''
Gist: 
Using dynamic programming, check which houses to rob.
If i is robbed, then rob the max amount up until i-1.
if i is skipped, i - 1 and all previous houses can be robbed.
Update the previous amounts with the maximum score from the above check.
Return the prev1 rob.

Time: O(N)
Space: O(1)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0  

        for num in nums:
            new_rob = max(prev1, prev2 + num)  
            prev2, prev1 = prev1, new_rob  

        return prev1