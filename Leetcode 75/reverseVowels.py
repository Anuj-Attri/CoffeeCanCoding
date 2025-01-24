'''
345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''
'''
Gist:
General solution to the problem. Can be used for all characters. 
Has the same complexity as ASCII solution, but proves slower than ASCII during test cases.

Time: O(N)
Space: O(N)
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")      # Constant time check
        indices = [i for i, char in enumerate(s) if char in vowels]  # Collect vowel indices
        s = list(s)  # Convert to list for mutability

        # Use two pointers to swap vowels
        left, right = 0, len(indices) - 1
        while left < right:
            i, j = indices[left], indices[right]
            s[i], s[j] = s[j], s[i]
            left += 1
            right -= 1

        return ''.join(s)  
