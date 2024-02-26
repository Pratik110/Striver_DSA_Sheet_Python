class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        absent = None
        duplicate = None
        max_num = max(A)
        freq_Dict = dict()
        for i in range(1,max_num+1):
            freq_Dict[i] = 0
        for element in A:
            freq_Dict[element]+=1
        print(freq_Dict)
        for i in range(1,max_num+1):
            if freq_Dict[i] == 0:
                absent = i
            if freq_Dict[i] > 1:
                duplicate = i
        return [duplicate,absent]            
s = Solution()
A = [3, 1, 2, 5, 3]
print(s.repeatedNumber(A))