# https://leetcode.com/problems/regular-expression-matching/
# DP: bottom up iteration


class Solution:
    def helper(self, s, p, i, j) -> bool:
        return s[i - 1] == p[j - 1] or p[j - 1] == '.'

    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        status = [[False]*(n+1) for i in range(m+1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    status[0][0] = True
                    continue
                if i > 0 and j > 0 and status[i - 1][j - 1]:
                    status[i][j] |= self.helper(s, p, i, j)
                if j > 0 and p[j-1] == '*':
                    # Match zero times
                    status[i][j] |= status[i][j - 2]
                    # Match one time
                    # e.g. 'a' matchs 'a*'
                    status[i][j] |= status[i][j - 1]
                    # Match many times
                    status[i][j] |= i > 0 and status[i-1][j] \
                        and self.helper(s, p, i, j-1)
                    # and (s[i-1] == p[j-2] or p[j-2] == '.')
        return status[m][n]
