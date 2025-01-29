'''
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
 of the characters without disturbing the relative positions of the remaining characters. 
 (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

'''
Gist:
Running two pointers, where ptr of 's' only increments when it finds a match in the string 't'.
The traversal only happens once for every character, and checked if it is equal to the length of substring.
Edge cases such as s = '' and t = '' are handled separately.
To prevent infinite loops, the above check is performed for every interation of i.

Time: O(N)
Space: O(1)
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        flag = 0
        if not s:           # if s = '', its a substring
            return True

        if not t:           # non-zero 's' cannot be a substring of an empty 't'
            return False

        for i in t:
            if s[flag] == i:
                flag += 1

            # Avoid out-of-index when the check is already satisfied
            if flag == len(s):
                return True

            
        return flag == len(s)