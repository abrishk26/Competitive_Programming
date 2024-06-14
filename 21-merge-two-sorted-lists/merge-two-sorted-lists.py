# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = None
        if list2 == None and list1 != None:
            return list1
        elif list1 == None and list2 != None:
            return list2
        elif list1 == None and list2 == None:
            return None
        else:
            if list1.val <= list2.val:
                list3 = list1
                list1 = list1.next
            else:
                list3 = list2
                list2 = list2.next

            temp = list3

            while list1 != None and list2 != None:
                if list1.val <= list2.val:
                    temp.next = list1
                    temp = temp.next
                    list1 = list1.next
                else:
                    while list1.val > list2.val and list2 != None:
                        temp.next = list2
                        temp = temp.next
                        list2 = list2.next

                        if list2 == None:
                            break

                    temp.next = list1
                    temp = temp.next
                    list1 = list1.next

            while list2 != None:
                temp.next = list2
                temp = temp.next
                list2 = list2.next

            while list1 != None:
                temp.next = list1
                temp = temp.next
                list1 = list1.next

            return list3