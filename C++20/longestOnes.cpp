/*
1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int left = 0, right = 0, max_len = 0, count = 0;

        while (right < nums.size()) {
            if (nums[right] == 0) count++;

            while (count > k) {  
                if (nums[left] == 0) count--;
                left++; 
            }

            max_len = max(max_len, right - left + 1); 
            right++; 
        }

        return max_len;
    }
};