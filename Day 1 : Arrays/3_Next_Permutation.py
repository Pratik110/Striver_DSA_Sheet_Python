class Solution(object):
    def nextPermutation(self, nums):
        pivot = None
        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                pivot = i-1
                break
        # print(pivot)
        if pivot is None:
            n = len(nums)-1
            i = 0
            while i < n:
                nums[i],nums[n]=nums[n],nums[i]
                i+=1
                n-=1
            return
        pivotVal = nums[pivot]
        for i in range(n-1,pivot,-1):
            if nums[i] > pivotVal:
                # nextGreater = nums[i]
                ngIdx = i
                break
        ##SWAP
        nums[pivot],nums[ngIdx]=nums[ngIdx],nums[pivot]
        # print(nums)
        # print(pivot)
        ##SORT FROM PIVOT PART TO END
        ##WE'RE NOT EXACTLY SORTING, THE PART FROM PIVOT TO END IS ALREADY SORTED IN REVERSE, SO WE JUST NEED TO REVERSE IT
        n = len(nums)-1
        pivot+=1
        while pivot < n:
            nums[n],nums[pivot]=nums[pivot],nums[n]
            n-=1
            pivot+=1
            # print(nums)
        return

nums = [2,1,5,4,3,0,0]
nums = [5,4,3,0,0]
nums = [1,2,3]
nums = [3,2,1]
s = Solution()
print(s.nextPermutation(nums))