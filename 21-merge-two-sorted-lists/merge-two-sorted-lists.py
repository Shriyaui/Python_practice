class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 and list2:
            if list1.val > list2.val:
                list1,list2=list2,list1
            list1.next=self.mergeTwoLists(list1.next,list2)
        return list1 or list2