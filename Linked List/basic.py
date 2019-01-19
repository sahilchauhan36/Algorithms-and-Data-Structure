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
    print("Insert Element: %s" % data)
    Node = node(data)
    if self.head == None:
      self.head = Node
    else:
      temp_node = self.head
      while temp_node.next != None: 
        temp_node = temp_node.next

  # Module to print the linked list
  def print_list(self):
    temp_node = self.head
    while temp_node.next != None:
      print("Element in the list : " + temp_node.data)
      temp_node = temp_node.next



if __name__=='__main__':
  print("Create a Linked List Object")
  ll_obj = linked_list()
  
  # Update head of the linked list 
  ll_obj.insert(1)

  # Insert the remaining elements 
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(5)
  ll_obj.insert(6)

  # Print the list 
  ll_obj.print_list()
