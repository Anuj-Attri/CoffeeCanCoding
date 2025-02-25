'''
746. Min Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''
'''
Gist:
Initialize the cost of first two steps, and iterate over the remaining steps.
Find the minimum of the last two costs, and add the current cost to it.
Return the minimum of previous and current step.

The optimized formula to use is defined as:
next cost = min(previous cost, current cost) + current step

Time: O(N)
Space: O(1)
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = cost[0], cost[1]

        for i in range(2, len(cost)):
            next_cost = min(prev, curr) + cost[i]
            prev, curr = curr, next_cost

        return min(prev, curr)