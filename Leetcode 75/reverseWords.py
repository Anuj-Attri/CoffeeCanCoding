'''
151. Reverse Words in a String
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.
'''

'''
Gist:
The problem can be solved by converting the string to list using 'split()' method.
Since there may be more than one space segregating the words, it is better to use split() instead of split(" ").
Reverse the list with 'reverse()' method and return the output using 'join()' method.

Time: O(N)
Spcae: O(N)

Note: In-place substitution method helps reduce space complexity down to constant space.
'''