# https://leetcode.com/problems/regular-expression-matching/
# DP: top down memorization
from functools import lru_cache


class Solution:
    @lru_cache
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0

        firstMatch = len(s) > 0 and (s[0] == p[0] or p[0] == '.')

        if len(p) >= 2 and p[1] == '*':
            # firstMatch is true, may match once or many times
            # and later, we can always ignore it at an appropriate time
            # by treat 'x*' as '', so pass on the intact p

            # we also need try that just treat 'x*' as ''
            # e.g.  'abcd' 'a*abcd'
            return (firstMatch and self.isMatch(s[1:], p)) \
                or self.isMatch(s, p[2:])
        else:
            # normal case
            return firstMatch and self.isMatch(s[1:], p[1:])
