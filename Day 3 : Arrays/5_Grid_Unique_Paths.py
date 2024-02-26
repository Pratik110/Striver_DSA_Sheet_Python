#Recursive Approach
class Solution1:
    def uniquePaths(self, m: int, n: int):
        max_path = 0
        def solve(m,n,curr_x,curr_y,max_path):
            if curr_x == m-1 and curr_y == n-1:
                return 1
            if curr_x == m or curr_y == n:
                return 0
            max_path += (solve(m,n,curr_x+1,curr_y,max_path)+solve(m,n,curr_x,curr_y+1,max_path))
            return max_path
        return solve(m,n,0,0,max_path)

class Solution2:
    def uniquePaths(self, m: int, n: int):
        dp = [[-1 for i in range(n)] for j in range(m)]
        if m == n == 1:
            return 1
        def solve(curr_x,curr_y,dp):
            if curr_x == m-1 and curr_y == n-1:
                return 1
            if curr_x == m or curr_y == n:
                return 0
            if dp[curr_x][curr_y] != -1:
                return dp[curr_x][curr_y]
            else:
                dp[curr_x][curr_y] = (solve(curr_x+1,curr_y,dp)+solve(curr_x,curr_y+1,dp))
                return dp[curr_x][curr_y]
        solve(0,0,dp)
        return dp[0][0]
m = 3
n = 7

s1 = Solution1()
max_path = s1.uniquePaths(m,n)
print(max_path)

s2 = Solution2()
max_path = s2.uniquePaths(m,n)
print(max_path)