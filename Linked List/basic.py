# This program explains the basic Functionality of the Linked List

class node():
  def __init__(self, data):
    self.data = data
    self.next = None
  
class linked_list:
  def __init__(self):
    self.head = None

  # Module to insert an element in the linked list 
  def insert(self, data):
    print("%s" % data, end = ' ')
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
    print("\nPrint Linked List")
    temp_node = self.head
    while temp_node != None:
      print("%s" % temp_node.data, end=' ')
      temp_node = temp_node.next



if __name__=='__main__':
  print("Create a Linked List Object")
  ll_obj = linked_list()
  
  # Insert Elements in linked list 
  print("Insert elements in Linked List")
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(5)
  ll_obj.insert(6)

  # Print the list 
  ll_obj.print_list()
