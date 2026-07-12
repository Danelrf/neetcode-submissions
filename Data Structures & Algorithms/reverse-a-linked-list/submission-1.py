# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        active = head
        jumps = []
        if not active:
            return None
        
        if not active.next:
            return active
            
        while active.next:
            # print(f"active val {active.val}, active next {active.next}")
            jumps.append(active)
            next = active.next
            active.next = None
            active = next
        
        active.next = jumps.pop()
        head = active
        active = active.next

        for el in range(len(jumps)-1,-1,-1):
            active.next = jumps.pop()
            active = active.next
        
        return head



