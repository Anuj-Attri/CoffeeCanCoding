'''
2390. Removing Stars From a String
You are given a string s, which contains stars *.

In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:
The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
'''

'''
Gist:
Traverse the string to find '*' and pop the stack when found.
If not, append the character to the stack.
Return the stack using join() method.

Time: O(N)
Space: O(N)
'''
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []

        for i in s:
            if i == '*':
                ans.pop()

            else:
                ans.append(i)

        return "".join(ans)