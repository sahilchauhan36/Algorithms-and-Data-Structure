# This program explains the logic to check if a string is palindrome or not

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

  # Module to reverse a linked list from the specified node as head.
  def reverse(self, temp_head=None):

    current_pointer = temp_head
    previous_pointer = None
    next_pointer = current_pointer.next

    while current_pointer != None: 
      next_pointer = current_pointer.next
      current_pointer.next = previous_pointer
      previous_pointer = current_pointer
      current_pointer = next_pointer 
      
    # Update head
    temp_head = previous_pointer
    return temp_head
    
  
  # Module to delete kth element in linked list 
  def check_palindrome(self):
    # find middle node
    fast_pointer = self.head
    slow_pointer = self.head
    while fast_pointer != None and slow_pointer != None:
      # To handle if the list is having odd number of elements
      if fast_pointer.next != None:
        fast_pointer = fast_pointer.next.next
      else:
        fast_pointer = None
      parent_slow_pointer = slow_pointer
      slow_pointer = slow_pointer.next

    # Note: Here, slow Pointer is the last element of first half

    # Reverse the list from Middle element
    new_mid_head = self.reverse(slow_pointer)
    parent_slow_pointer.next = new_mid_head
    
    # check both the list(start to mid and mid to list are same)
    pointer_1 = self.head
    pointer_2 = new_mid_head

    while pointer_2 != None and pointer_1 != new_mid_head:
      #print("\t[%s,%s]" %(pointer_1.data, pointer_2.data))
      if pointer_1.data != pointer_2.data:
        return False
      pointer_1 = pointer_1.next
      pointer_2 = pointer_2.next
    return True
  

if __name__=='__main__':
  # Create a linked list
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  

  # Update head of the linked list 
  print("2. Insert Elements in Linked list")
  """For Demo Inserting Elements in order"""
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(5)
  ll_obj.insert(5)
  ll_obj.insert(4)
  ll_obj.insert(3)
  ll_obj.insert(2)
  ll_obj.insert(1)

  # Print the list
  print("3. Linked List") 
  ll_obj.print_list()

  print("4. Checking is the Linked List is Palindrome or not")
  result = ll_obj.check_palindrome()

  print("5. Linked List is Palindrome %s" % result)

  # For Simplicity and easy understandability I'm creating adding a new element, 
  # However you can also create a new list 
  # and check the same.

  # Create a linked list
  print("1. Create a Linked List Object")
  ll_obj.insert(2)

  # Print the list
  print("3. Linked List") 
  ll_obj.print_list()

  print("4. Checking is the Linked List is Palindrome or not")
  result = ll_obj.check_palindrome()

  print("5. Linked List is Palindrome %s" % result)
