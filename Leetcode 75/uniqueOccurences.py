'''
1207. Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
'''

'''
Gist:
Using the 'Counter' function, we can create a dictionary that counts the occurences of unique elements within an array.
Extracting the values of the dictionary (hash map) 'count' and coverting them to set gives us all the unique counts.
Comparing the length of unique counts with the original value returns if two elements appear the same number of times or not.

Time: O(N)
Space: O(N)

Note: 
Dynamically checking the frequency of unique values may reduce the space complexity to constant space, but affects the readability of code.
'''

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        return len(set(count.values())) == len(count.values())