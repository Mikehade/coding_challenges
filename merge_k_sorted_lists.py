# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
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
        
        l3 = []
        for i in range(len(lists)):
            if lists[i] is None:
                l1 = lists[i]
            else:
                l1 = pl(lists[i])
            #l2 = pl(list2)
            if i == 0 and lists[i] is not None:
                l3 = sorted(l1)
            elif i > 0 and lists[i] is not None:
                l3 = sorted(l1 + l3)
        
        if len(l3) == 0:
            return None
        print(l3)

        ml = al(l3)
        l = pl(ml)
        return ml
