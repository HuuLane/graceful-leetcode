# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        ans = [
            [root]
        ]
        while True:
            next_level = []
            for i, node in enumerate(ans[-1]):
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
                # replace to value
                ans[-1][i] = node.val
            if next_level:
                ans.append(next_level)
            else:
                break
        return ans
