# https://leetcode.com/problems/symmetric-tree/
# Ideas: recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        elif left is None or right is None or left.val != right.val:
            return False
        return self.helper(left.left, right.right) \
            and self.helper(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.helper(root.left, root.right)
