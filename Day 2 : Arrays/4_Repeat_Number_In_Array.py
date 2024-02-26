class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d =  dict()
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
            if d[i]==2:
                return i