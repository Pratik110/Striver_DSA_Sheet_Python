##https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1, m, nums2, n):
        last = m+n-1
        m-=1
        n-=1
        while m >= 0 and n >= 0:
            if nums2[n] > nums1[m]:
                nums1[last] = nums2[n]
                # print(nums1)
                n-=1
            else:
                nums1[m],nums1[last] = nums1[last],nums1[m]
                m-=1
            last-=1
                # print(nums1)
        while n >= 0:
            nums1[n] = nums2[n]
            n-=1
        return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s = Solution()
print(s.merge(nums1, m, nums2, n))