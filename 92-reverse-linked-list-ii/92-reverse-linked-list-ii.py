
class ListNode:
    def __init__(self, val=0, next=None):
          self.next = next
            
class Solution:
    #T(n) = O(n) and S(n) = O(1)
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        #creating a dummy node to keep track of prev of leftnode
        dummyhead = ListNode(0)
        dummyhead.next = head
        
        leftprev,curr = dummyhead,head
        
        #iterating till leftnode
        for i in range(left-1):
            leftprev = leftprev.next
            curr = curr.next
        
        prev = None
        
        #reversing nodes between left and right(std reverse of linkedlist)
        for i in range(right-left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #adjusting the pointer after rightnode
        leftprev.next.next = curr
        #adjusting the pointer before leftnode
        leftprev.next = prev
        
        return dummyhead.next