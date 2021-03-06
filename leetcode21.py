# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1, l2
        temp_node = ListNode()
        head = temp_node
        while node1 is not None and node2 is not None:
            if node1 and node1.val < node2.val:
                temp_node.next = node1
                node1 = node1.next
            else:
                temp_node.next = node2
                node2 = node2.next
            temp_node = temp_node.next
        if node1:
            temp_node.next = node1
        if node2:
            temp_node.next = node2

        return head.next
