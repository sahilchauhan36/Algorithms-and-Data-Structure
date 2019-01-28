# This program explains reversal of a linked list

class node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class linked_list:
  def __init__(self):
    self.head = None

  # Module to insert an element in the linked list 
  def insert(self, data):
    Node = node(data)
    if self.head == None:
      self.head = Node
    else:
      temp_node = self.head
      while temp_node.next != None: 
        temp_node = temp_node.next
      temp_node.next = Node

  # Module to print the linked list
  def print_list(self):
    print('\t[', end=' ')
    temp_node = self.head
    while temp_node != None:
      print("%s" % temp_node.data, end=' ,')
      temp_node = temp_node.next
    print('\b]')

  # Module to reverse a linked list
  def reverse(self):
    current = self.head
    prev = None  # Variable to keep record of previous node 
    while current != None:
      next = current.next # Variable to keep record of next node 
      # update pointer of current pointer from next to previous
      current.next = prev
      prev = current
      current = next

    # update head to last traversed element
    self.head = prev
    

if __name__=='__main__':
  # Create a linked list
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  

  # Update head of the linked list 
  print("2. Insert Elements in Linked list")
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(5)
  ll_obj.insert(6)

  # Print the list
  print("3. Linked List before reverse") 
  ll_obj.print_list()

  # Print the list
  print("3. Reverse the Linked List") 
  ll_obj.reverse()

  # Print the list
  print("4. Linked List after reversal") 
  ll_obj.print_list()
