# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_all_nodes(self, node):
        all_nodes = []

        while node != None:
            all_nodes.append(node)
            node = node.next

        return all_nodes

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_nodes = self.get_all_nodes(list1)
        list2_nodes = self.get_all_nodes(list2)

        all_nodes_sorted = sorted([] +
                                  list1_nodes + list2_nodes, key=lambda item: item.val)

        for i, node in enumerate(all_nodes_sorted[:-1]):
            node.next = all_nodes_sorted[i+1]

        return None if not all_nodes_sorted else all_nodes_sorted[0]


def create_node(val):
    return ListNode(val)


node1 = ListNode(1, ListNode(2, ListNode(4, None)))
node2 = ListNode(1, ListNode(3, ListNode(5, None)))

print(Solution().mergeTwoLists(node1, node2))
