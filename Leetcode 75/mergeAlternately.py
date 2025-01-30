'''
1768. Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

'''
Gist:
Nested for-loop can be used, but a while-loop proves to be more scalable.

Time: O(N + M) => O(K)
Space: O(N + M) => O(K)
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        if i < len(word1):
            merged.append(word1[i:])
        if j < len(word2):
            merged.append(word2[j:])

        return "".join(merged)