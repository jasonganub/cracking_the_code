from linked_lists.linked_list import LinkedList


def delete_middle_node(node):
    # Set node value to be the one after
    node.value = node.next.value

    # Point node to two nodes after
    node.next = node.next.next


ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
delete_middle_node(middle_node)
print(ll)