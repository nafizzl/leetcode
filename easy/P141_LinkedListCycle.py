# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class P141_LinkedListCycle:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None or head.next == None or head.next.next == None):
            return False                # if list is small, use this to avoid errors with None
        
        slow = head
        fast = head                     # make two pointers
        
        while (fast != None):
            if (fast.next == None):     # conditional to avoid None errors
                return False
            slow = slow.next
            fast = fast.next.next       # pointers "move" at different speeds
            if (slow == fast):
                return True             # conditional for detecting loop
        return False
