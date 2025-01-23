'''
1431. Kids With the Greatest Number of Candies

There are n kids with candies. 
You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, 
and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, 
after giving the ith kid all the extraCandies, 
they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
'''

'''
Time: 
Space:

Gist: 
Using in-place addition, check if upon addition, the number of candies exceeds the maximum of the array. 
Iteratively append the answer to result[].
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        k = max(candies)

        for i in candies:
            if (i + extraCandies) >= k:
                result.append(True)
            else:
                result.append(False)
        
        return result
        