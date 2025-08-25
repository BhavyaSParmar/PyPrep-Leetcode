class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

      
        def get_kth(start: ListNode, k: int) -> Optional[ListNode]:
            cur = start
            for _ in range(k):
                cur = cur.next
                if not cur:
                    return None
            return cur

        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

          
            prev, cur = group_next, group_prev.next
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

         
            tmp = group_prev.next         
            group_prev.next = kth         
            group_prev = tmp              

        return dummy.next