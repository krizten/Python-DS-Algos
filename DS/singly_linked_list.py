class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f"Data: {self.data} | Next: {self.next_node.data if self.next_node is not None else None}"


class SinglyLinkedList:
    def __init__(self):
        self.head_node = None


# ======== TEST ===========
list_1 = SinglyLinkedList()
list_1.head = Node(13)
node_2 = Node(21)
node_3 = Node(34)
node_4 = Node(55)
node_5 = Node(89)

list_1.head.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4
node_4.next_node = node_5

print(str(node_5))
# ======== TEST ===========