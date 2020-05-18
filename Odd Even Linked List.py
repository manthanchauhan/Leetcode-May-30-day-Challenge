# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        n = 0
        ptr = head
        
        while ptr is not None:
            ptr = ptr.next
            n += 1
            
        if n < 3:
            return head
        
        ptr1 = head
        ptr2 = head.next
        
        while ptr1 and ptr2 and ptr2.next:
            nd = ptr2.next
            d = nd.val   
            
            if ptr2.next is None:
                break
                
            ptr2.next = ptr2.next.next
            
            nd2 = ptr1.next
            ptr1.next = nd
            
            nd.next = nd2
            
            if (ptr1 is None) or (ptr2 is None):
                break
                
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return head
