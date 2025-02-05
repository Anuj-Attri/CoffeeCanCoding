'''
1456. Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''

'''
Gist:
Using sliding window, we initialize the first 'k' elements of 's' as the initial sliding window.
Using a set for O(1) lookup, we add the vowels. The problem states that s is a lowercase string.
Count the vowels in the first substring, and slide the window efficiently across by removing the previous element and adding the next.
Update the max number of vowels by comparing current count to the previous count.

Time: O(N)
Space: O(1)
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        max_vowels = 0
        current_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels

        for i in range(k, len(s)):
            if s[i] in vowels:  
                current_vowels += 1
            if s[i - k] in vowels:  
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)  

        return max_vowels