# This program explains the concept of removing duplicate elements from a Doubly Linked List

class node():
  def __init__(self, data):
    self.data = data
    self.prev = None
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
      Node.prev = temp_node

  # Module to print the linked list
  def print_list(self):
    print("[", end =' ')
    temp_node = self.head
    while temp_node != None:
      print("%s" %temp_node.data , end =' ')
      temp_node = temp_node.next
    print("]")
  
  # Module to remove duplicate elements from doubly linked list
  def remove_duplicates(self):
    current_pointer = self.head
    parent_pointer = None
    bucket = set()
    while current_pointer != None:
      if current_pointer.data in bucket:
        parent_pointer.next = current_pointer.next
        current_pointer.next.prev = parent_pointer
        del current_pointer
        current_pointer = parent_pointer.next
      else:
        bucket.add(current_pointer.data)
        parent_pointer = current_pointer
        current_pointer = current_pointer.next
      
if __name__=='__main__':
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  
  # Insert Elements in linked list 
  print("2. Insert elements in Linked List")
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(4)
  ll_obj.insert(4)
  ll_obj.insert(5)
  ll_obj.insert(6)

  # Print the list 
  print("\n3. Print the Doubly Linked List")
  ll_obj.print_list()

  # Call remove_duplicates
  print("4. Remove Duplicates")
  ll_obj.remove_duplicates()

  print("5. Print Linked List after Duplicate Removal")
  ll_obj.print_list()
