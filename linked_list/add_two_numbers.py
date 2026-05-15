class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def append_list(self, data_of_list):
        for i in data_of_list:
            new_node = Node(i)

            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next 
                current.next = new_node
                
    def display_list(self):
        current = self.head
        while current:
            print(current.data, '-> ', end=" ")
            current = current.next
           
    def count_list_item(self):
        count = 0
        current =  self.head
        while current:
            count += 1
            current = current.next 
            
    def add_two_list(self, l1, l2, l3):
        sum = 0
        borrow = 0
        length = self.count_list_item(l1)
        
        for i in range(length):
            sum = l1.data + l2.data
            
            if sum >= 10:
                temp_sum = sum 
                sum -= 10
                l3.append(sum + borrow)
                borrow = temp_sum // 10
        
        
    
        
# ll = LinkedList()

# # ll.append(2)
# # ll.append(4)

# ll.append_list([2,4,3])
# ll.display_list()
# ll.append_list([5,6,4])
# ll.display_list()