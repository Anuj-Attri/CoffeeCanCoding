'''
345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

'''
Gist:
Caution: Beautiful solution incoming!
Using two pointers (left, right) that move from the edges towards each other, traverse the array in linear time.
Move these pointers until both of them have found a vowel. Then swap these vowels with each other.
Check for vowel in constant time by using Python's "in" operator.
ByteArray is a mutable data structure, which can be used for ASCII characters only. It provides us with constant space and time.

The stop condition is always that the left index pointer should be less than the right index pointer.

Time: O(N)
Space: O(N)

Limitation: will throw issues if characters outside ascii are used. Can be resolved by increasing the vowels set.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = bytearray(s, 'utf-8')    # Converting to byteArray for constant space
        left, right = 0, (len(s_list) - 1)
        vowels = b'AEIOUaeiou'           # Constant time vowel check

        while left < right:             # Left < Right is a stop condition (prevents infinite loop)
            while left < right and s_list[left] not in vowels:  # Moves the left pointer till a vowel is found
                left += 1

            while left < right and s_list[right] not in vowels: # Moves the right pointer till a vowel is found
                right -= 1

            s_list[left], s_list[right] = s_list[right], s_list[left]   # When both pointers are at vowels, swaps them

            # Pointers must move inwards
            left += 1
            right -= 1
        
        return s_list.decode('utf-8')