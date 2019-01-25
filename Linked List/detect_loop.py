# This program explains the program to find loop in the given linked list.

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
      # condition to check loop and print values 
      if temp_node is self.head:
        print("Repeat", end=' ')
        break

    print('\b]')
  
  # Module to create a loop 
  def create_loop(self):
    """
    This function is used to update the next of the node to head. so that the linked list can have a circle/loop like structure.

    e.g. 
    ->1 -> 2 -> 4 -> 5 -> 6
      ^                   |
      |___________________| 
    
    """
    current_node = self.head
    while current_node.next != None:
      current_node = current_node.next
    # update next of last node
    current_node.next = self.head
    
  def is_having_loop(self):
    """
    This module is used to find loop in linked list
    """
    slow_pointer = self.head 
    fast_pointer = self.head

    while fast_pointer.next != None and slow_pointer != None:
      # If Fast and Slow Pointer meets, It means there is loop present in linked list

      fast_pointer = fast_pointer.next.next
      slow_pointer = slow_pointer.next

      if fast_pointer is slow_pointer:
        return True
    
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
  ll_obj.insert(2)
  ll_obj.insert(5)
  ll_obj.insert(6)
  ll_obj.insert(2)
  ll_obj.create_loop()

  # Print the list
  print("3. Linked List 1") 
  ll_obj.print_list()

  # Check if loop is present in linked list
  result = ll_obj.is_having_loop()
  print("4. Loop Detected : %s" % result)


  # Negative Scenario when linked list is not having any loop 
  print("\n Negative Scenario when linked list is not having any loop.")
  print("1. Create Linked List 2 Object")
  ll_obj_2 = linked_list()
  

  # Update head of the linked list 
  print("2. Insert Elements in Linked list 2")
  ll_obj_2.insert(4)
  ll_obj_2.insert(5)
  ll_obj_2.insert(6)
  ll_obj_2.insert(2)
  ll_obj_2.insert(8)
  ll_obj_2.insert(9)
  ll_obj_2.insert(3)

  # Print the list
  print("3. Linked List 2") 
  ll_obj_2.print_list()

  # Check if loop is present in linked list
  result = ll_obj_2.is_having_loop()
  print("4. Loop Detected : %s" % result)
