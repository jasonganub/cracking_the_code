from linked_lists.linked_list import LinkedList


def kth_to_last(ll, k):
    runner = ll.head
    current = ll.head

    # Iterate runner to the kth spot so current can push runner right
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    # Keep pushing runner to right until it hits None
    # It keeps a distance between current so it lands on
    # the kth node.
    while runner:
        current = current.next
        runner = runner.next

    return current


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 3))