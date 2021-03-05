# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        current_node = head
        node1, node2 = l1, l2
        carry = 0

        while node1 is not None or node2 is not None:
            _sum = self.sum_2_nodes(node1, node2, carry)
            current_node.value = _sum % 10
            if _sum >= 10:
                carry = 1
            else:
                carry = 0
            current_node.next = ListNode(_sum % 10)
            current_node = current_node.next
            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next
        if carry > 0:
            current_node.next = ListNode(carry)
        return head.next
            
    def sum_2_nodes(self, node1: ListNode, node2: ListNode, carry) -> int:
        if node1 and node2:
            return node1.val + node2.val + carry
        elif node1 and node2 is None:
            return node1.val + carry
        elif node1 is None and node2:
            return node2.val + carry
        else:
            return carry
