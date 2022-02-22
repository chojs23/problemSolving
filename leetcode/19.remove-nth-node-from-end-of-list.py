# @before-stub-for-debug-begin
from python3problem19 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        time = 0
        dummy = head
        while fast and fast.next:
            fast = fast.next.next
            time += 1
        if time == 0:
            return None
        if fast:
            lastidx = time * 2
        else:
            lastidx = time * 2 - 1
        if lastidx - n >= 0:
            for _ in range(lastidx - n + 1 - 1):
                head = head.next
            head.next = head.next.next
        else:
            dummy = head.next
        return dummy


# @lc code=end
