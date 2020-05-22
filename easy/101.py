# https://leetcode.com/problems/symmetric-tree/
# Ideas: queue, iteration
# TODO: very slow

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def test(self, nodes) -> bool:
        left = 0
        right = len(nodes) - 1
        while left < right:
            if nodes[left] and nodes[right]:
                # two non-None
                if nodes[left].val != nodes[right].val:
                    return False
            elif nodes[left] or nodes[right]:
                # one None, one non-None
                return False
            else:
                # two None
                pass
            left += 1
            right -= 1
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        cur_level = [root]
        while True:
            next_level = []
            for n in cur_level:
                if n is None:
                    next_level.append(None)
                    next_level.append(None)
                else:
                    next_level.append(n.left)
                    next_level.append(n.right)
            if all(n is None for n in next_level):
                # all nodes are None
                return True
            if not self.test(next_level):
                return False
            cur_level = next_level
