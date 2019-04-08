class Node():
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def print_node(self):
        print self.value


class LinkedList():
    def __init__(self,node):
        self.node = node

    def print_linkedlist(self):
        node = self.node
        while node.next_node != None:
            node.print_node()
            node = node.next_node



def create_linkedlist():
    node1 = Node(10,None)
    node2 = Node(20,node1)
    node3 = Node(30,node2)
    node4 = Node(40,node3)
    return LinkedList(node4)


ll = create_linkedlist()
ll.print_linkedlist()

def delete_a_node(ll,node):
    first_node = ll.node

#delete first node
delete_a_node(ll,ll.node)

