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