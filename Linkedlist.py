# Define a Node class
class Node:
    def __init__(self, data=None):
        self.data = data  # Stores the data
        self.next = None  # Pointer to the next node (initially None)

# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the linked list with an empty head
    
    # Method to insert a node at the end
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If the list is empty, set the head to the new node
            self.head = new_node
            return
        # Traverse the list and find the last node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node  # Set the next of the last node to the new node

    # Method to print the linked list
    def print_list(self):
        current = self.head
        while current:  # Traverse through the list
            print(current.data, end=" -> ")  # Print the data
            current = current.next
        print("None")  # Indicate the end of the listx
    def reverse_list(self):
        prev,curr = None,self.head
        while curr:
            nextq = curr.next
            curr.next = prev

            prev = curr
            curr = nextq
        self.head = prev
        
# Example usage of LinkedList
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()
ll.reverse_list()
ll.print_list() 