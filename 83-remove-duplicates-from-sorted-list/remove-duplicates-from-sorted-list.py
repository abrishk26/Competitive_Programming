# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        table = []
        temp = head
        temp2 = None

        while temp != None:
            if temp.val in table:
                temp2.next = temp.next
                temp = temp.next
            else:
                table.append(temp.val)
                temp2 = temp
                temp = temp.next

        return head
                
        