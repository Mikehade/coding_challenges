# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def pl(llist):
            l = []
            if llist.next == None:
                l.append(llist.val)
                return l
            while llist.next != None:
                print(llist.val)
                l.append(llist.val)
                llist = llist.next
            print(llist.val)
            l.append(llist.val)
            return l
        
        def al(llist):
            #ll = ListNode()
            #ll.val = llist[0]
            temp = head = ListNode(llist[0])
            for i in range(1, len(llist)):
                #ll.next = llist[i]
                #ll = ll.next
                #ListNode(llist[i])
                temp.next = ListNode(llist[i])
                #print(llist[i])
                
                temp = temp.next
            return head
            
        
        if list2 is None and list1 is None:
            return list1
        elif list2 is None and list1 is not None:
            return list1
        elif list1 is None and list2 is not None:
            return list2
        else:
            l1 = pl(list1)
            l2 = pl(list2)
            l3 = sorted(l1 + l2)
            #print(l3)

            ml = al(l3)
            l = pl(ml)
            return ml
        
