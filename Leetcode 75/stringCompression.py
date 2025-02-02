'''
443. String Compression
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
'''

'''
Gist:
Using two pointers (rx, wx) for traversing and in-place changes respectively, we count the consecutive occurences of each character.
Pointer rx is updated when consecutive characters are found, whereas wx is updated when the character changes.
If count of character occurences is more than one, count is casted to string and inserted at index 'wx'.
Pointer 'wx' is updated accordingly.
A dry run with example is the best explanation for this problem.

Time: O(N)
Space: O(1)
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        rx, wx = 0, 0

        while rx < len(chars):
            char = chars[rx]
            count = 0

            while rx < len(chars) and chars[rx] == char:
                rx += 1
                count += 1

            chars[wx] = char
            wx += 1

            if count > 1:
                for i in str(count):
                    chars[wx] = i
                    wx += 1

        return wx