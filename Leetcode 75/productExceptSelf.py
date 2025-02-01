'''
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

'''
Gist:
The problem does not allow division, hence a different approach is taken. 
Two loops are used to calculate the product of elements right-most and left-most of an index.
Answer[i] = left_product[i] * right_product[i]; as neither of the products include the element at index 'i'.

Time: O(N)
Space: O(N)

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        answer = [1] * N

        left_product = 1
        for i in range(N):
            answer[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(N - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer