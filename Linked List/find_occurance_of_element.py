# This program explains how to find occurance of an element in the given list.

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
  
  def find_element_occurance(self, value):
    """
    This function is for finding occurance of particular element in the list. 
    """
    count = 0 
    current_node = self.head

    while current_node != None:
      if current_node.data == value:
        count += 1
      current_node = current_node.next
    return count
    

if __name__=='__main__':
  # Create a linked list
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  

  # Update head of the linked list 
  print("2. Insert Elements in Linked list")
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(2)
  ll_obj.insert(5)
  ll_obj.insert(6)
  ll_obj.insert(2)

  # Print the list
  print("3. Linked List") 
  ll_obj.print_list()

  # Find occurance of element which is present in list
  element_to_find = 2
  occurance = ll_obj.find_element_occurance(element_to_find)
  print("4. %s has %s occurances in the given list" % (element_to_find, occurance) )

  # Find occurance of element which is not present in list.
  element_to_find = 10
  occurance = ll_obj.find_element_occurance(element_to_find)
  print("5. %s has %s occurances in the given list" % (element_to_find, occurance) )
