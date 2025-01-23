# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Time: O(N)
''' 
Gist:
Let x be the GCD of str1 and str2, then length of x is equal to the GCD of lengths of str1 and str2. 
Taking a prefix of this length from any one string will give us a potential GCD.
Verify if str1 = x*x*x...x_i and str2 = x*x*x...x_j; where i is length(str1) divided by length of GCD.
'''

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # calculate the length of potential GCD string
        n = math.gcd(len(str1), len(str2))

        # Assign a substring of length n
        s = str1[:n]

        # Check for divisibility
        if str1 == s *(len(str1)//n) and str2 == s * (len(str2)//n):
            return s
        else:
            return ""