class Solution(object):
    def merge(self, intervals):
        outputArr = []
        intervals.sort()
        for interval in intervals:
            if outputArr == [] or outputArr[-1][-1] < interval[0]:
                outputArr.append(interval)
            else:
                outputArr[-1][-1] = max(outputArr[-1][-1],interval[1])
        return outputArr
intervals = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
s = Solution()
result = s.merge(intervals)
print(result)