class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def append_to_tail(self, data):
        node = Node(data)
        current = self
        while current.next:
            current = current.next
        current.next = node

    def delete_node(self, data):
        node = self

        if node.data == data:
            return node.next

        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                return self
            node = node.next

        return self
