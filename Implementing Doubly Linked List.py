class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        
        if not temp:
            return  # Key not found
        
        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next  # Deleting head
        
        if temp.next:
            temp.next.prev = temp.prev
        
        temp = None  # Free memory

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' <-> ' if temp.next else '')
            temp = temp.next
        print()

# Example Usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.display()  # Output: 0 <-> 1 <-> 2 <-> 3
dll.delete(2)
dll.display()  # Output: 0 <-> 1 <-> 3
