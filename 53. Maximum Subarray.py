#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#A subarray is a contiguous part of an array.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf
        currSum = 0

        for i in range(0, len(nums)):
            currSum = currSum + nums[i]
            if(currSum > maxSum):
                maxSum = currSum
            if(currSum < 0):
                currSum = 0
        return maxSum
                
        
