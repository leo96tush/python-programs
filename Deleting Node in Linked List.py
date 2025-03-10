from copy import deepcopy

class ListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

listnode = ListNode(5)
listnode.next = ListNode(10)
listnode.next.next = ListNode(12)
listnode.next.next.next = ListNode(23)

position = 2
node = listnode
counter = 1

deletion_node = ListNode(0)

while(node and counter < position):
    counter = counter + 1
    # print(counter)
    # print(node.data)
    deletion_node = node
    node = node.next

# print(node.data)
# print(deletion_node.data)

deletion_node.next = node.next
node.next = deletion_node.next.next


temp = listnode

while(temp):
    print(temp.data)
    temp = temp.next
