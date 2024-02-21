class Solution(object):
    def permute(self, nums):
        result = []
        tempArr = []
        markArr = [False] * len(nums)
        n = len(nums)
        def formPermuations(nums,tempArr,markArr,result,n):
            if len(tempArr) == n:
                copyArr = tempArr.copy()
                result.append(copyArr)
                return
            for i in range(n):
                if not markArr[i]:
                    markArr[i] =  True
                    tempArr.append(nums[i])
                    formPermuations(nums,tempArr,markArr,result,n)
                    markArr[i] =  False
                    tempArr.pop()
        formPermuations(nums,tempArr,markArr,result,n)
        return result

s = Solution()
numArr = [3,1,2]
print(s.permute(numArr))
