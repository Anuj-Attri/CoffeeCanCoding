'''
1732. Find the Highest Altitude
There is a biker going on a road trip. 
The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). 
Return the highest altitude of a point.
'''

'''
Gist:
A direct cumsum function can solve the issue. 
Finding the maximum of cumsum will give the highest altitude.
The initial altitude is 0, so 0 is compared to the rest of cumsum.
A loop can be used to solve the problem without numpy, but numpy is more optimal as n increases.

Time: O(N)
Space: O(N)
'''

import numpy as np

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = np.cumsum(gain)
        return int(max(0, max(result)))