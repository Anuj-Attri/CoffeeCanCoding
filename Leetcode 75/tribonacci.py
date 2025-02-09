'''
1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''

'''
Gist:
Only the three values are needed at any given point to find the value of Tn.
Using the given general solution, substitute the variables till the loop runs out at (n+1).
The swap returns the value of of Tn+3 for given n.

Time: O(N)
Space: O(1)
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return 0

        if n == 1 or n == 2: 
            return 1

        Tn, Tn1, Tn2 = 0, 1, 1  
        for _ in range(3, n + 1):
            Tn, Tn1, Tn2 = Tn1, Tn2, Tn + Tn1 + Tn2

        return Tn2