# Given a singly linked list and an integer k, remove the kth last 
# element from the list. k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.

class Node(object):

    def __init__(self, value: str):
        self.value: str = value
        self.next = None

    def string_representation_of_linked_list(self) -> str:
        values = [self.value]

        if self.next is not None:
            values.append(self.next.string_representation_of_linked_list())

        return ' -> '.join(values)


def remove_element_from_linked_list(linked_list, remove_index: int):
    current_element_index: int = 0
    previous_node: Node = None
    current_node: Node = linked_list
    while current_element_index != remove_index:
        previous_node = current_node
        current_node = current_node.next
        current_element_index += 1

    if previous_node is None:
        # First element in the linked list
        linked_list = current_node.next
    else:
        previous_node.next = current_node.next

    return linked_list


linked_list = Node("a")

linked_list.next = Node("b")

linked_list.next.next = Node("c")

linked_list.next.next.next = Node("d")

linked_list.next.next.next.next = Node("e")

print(linked_list.string_representation_of_linked_list())

updated_linked_list = remove_element_from_linked_list(linked_list, 0)

print(updated_linked_list.string_representation_of_linked_list())

updated_linked_list = remove_element_from_linked_list(linked_list, 2)

print(updated_linked_list.string_representation_of_linked_list())