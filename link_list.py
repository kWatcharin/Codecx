class Node():

    def __init__(self, data):
        self.data = data
        self.next = next


class Linklist():

    def __init_(self):
        self.head = None

if __name__ == '__main__':

    fist_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)

    # Link list Node 1(head)
    link_list = Linklist()
    link_list.head = fist_node 

    # Link list Node 1 to 2'
    link_list.head.next = second_node

    # Link list Node 2 to 3
    second_node.next = third_node

