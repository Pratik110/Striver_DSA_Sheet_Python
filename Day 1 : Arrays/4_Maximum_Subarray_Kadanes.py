import sys
class Solution(object):
    def maxSubArray(self, nums):
        sumArr = 0
        maxSum = -sys.maxsize - 1
        n = len(nums)
        for i in range(n):
            sumArr+=nums[i]
            maxSum = max(sumArr,maxSum)
            if sumArr <= 0:
                sumArr = 0

        return maxSum
        
# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-1]
s = Solution()
print(s.maxSubArray(nums))