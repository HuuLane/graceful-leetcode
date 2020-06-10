# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# idea: fixed-length FIFO
from collections import deque


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        q = deque([], k)
        node = head
        while node:
            q.append(node)
            node = node.next
        return q.popleft()
