class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f"Data: {self.data} | Next: {self.next_node.data if self.next_node is not None else None}"


class SinglyLinkedList:
    def __init__(self):
        self.head_node = None

    def traverse_list(self):
        if self.head_node is None:
            yield None
        else:
            value = self.head_node
            while value is not None:
                yield value
                value = value.next_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next_node = self.head_node
        self.head_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
            return
        tail_node = self.head_node
        while tail_node.next_node is not None:
            tail_node = tail_node.next_node
        tail_node.next_node = new_node

    def insert_after_item(self, item, data):
        node = self.head_node
        while node is not None:
            if node.data == item:
                break
            node = node.next_node
        if node is None:
            raise Exception('Item not found in the list')
        else:
            new_node = Node(data)
            new_node.next_node = node.next_node
            node.next_node = new_node

# ======== TEST ===========
list_1 = SinglyLinkedList()
list_1.head_node = Node(13)
node_2 = Node(21)
node_3 = Node(34)
node_4 = Node(55)
node_5 = Node(89)

list_1.head_node.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4
node_4.next_node = node_5

list_1.insert_at_start(8)
list_1.insert_at_end(233)
list_1.insert_after_item(89, 144)

for item in list_1.traverse_list():
    print(item)

# ======== TEST ===========


# print(str(node_5))
