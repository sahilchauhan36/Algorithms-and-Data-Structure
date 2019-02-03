# This program explains the Search Functionality of the Linked List

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

  # Module to delete a linked list 
  def delete_list(self):
    current_node = self.head
    while current_node != None:
      next_node = current_node.next
      del current_node.data
      current_node = next_node 
    self.head = None 

  def is_element_present(self, value):
    """
    Function to check if an element is present in the linked list or not.
    """
    current_node = self.head
    while current_node != None:
      if current_node.data == value:
        return True
      current_node = current_node.next
    return False
    

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
  print("3. Linked List") 
  ll_obj.print_list()

  # Check if the Element is present in the list
  element_to_search = 4
  result = ll_obj.is_element_present(element_to_search)
  print("4. Element %s present in list : %s" % (element_to_search, result))

  # Check if the Element is present in the list
  element_to_search = 9
  result = ll_obj.is_element_present(element_to_search)
  print("4. Element %s present in list : %s " % (element_to_search, result))
