class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

my_linked_list = LinkedList(None)
while True:
    input_num = input()
    if input_num == "":
        my_linked_list.append(1)
        break
    try:
        num = int(input_num)
        my_linked_list.append(num)
    except ValueError:
        print("IEVADITAIS NAV CIPARS")
        

print( my_linked_list.find_middle_node().value )