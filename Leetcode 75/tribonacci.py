'''
1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''

'''
Gist:

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