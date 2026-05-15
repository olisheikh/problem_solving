from add_two_numbers import LinkedList

class MergeTwoList(LinkedList):
    def merge_two_sorted_list(self,l2):
        l3 = LinkedList()
        
        current1 = self.head
        current2 = l2.head
         
        while current1 or current2:
            if current1 and (not current2 or current1.data <= current2.data):
                l3.append(current1.data)
                current1 = current1.next
            else:
                l3.append(current2.data)
                current2 = current2.next
            
        return l3
            
l1 = MergeTwoList()
l2 = MergeTwoList()

l1.append_list([1,2,4])
l2.append_list([1,3,4])

l3 = l1.merge_two_sorted_list(l2)

l3.display_list()