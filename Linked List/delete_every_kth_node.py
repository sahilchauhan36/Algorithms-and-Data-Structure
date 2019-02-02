# This program explains the deleting every kth node of the linked list.

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

  # Module to delete kth element in linked list 
  def delete_kth_element(self,k):
    # Decrement K for computation simplicity
    k = k-1

    current_node = self.head
    next_node = current_node.next
    while next_node != None and current_node != None:
      count=0
      while count < k-1 and next_node.next != None:
        current_node = current_node.next
        next_node = current_node.next
        count = count + 1
        # print("[Current: %s, Next: %s]" % (current_node.data,next_node.data))

      # If node to be deleted is last node
      if next_node == None:
        current_node.next = None
      
      current_node.next = next_node.next
      del next_node.data
      current_node = current_node.next 
      next_node = current_node.next
      self.print_list()

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
  ll_obj.insert(6)
  ll_obj.insert(7)
  ll_obj.insert(8)
  ll_obj.insert(9)
  ll_obj.insert(10)

  # Print the list
  print("3. Linked List before Deletion") 
  ll_obj.print_list()
  
  k=3
  print("4. Calling Linked List Deletion for every %sth Node" % k)
  ll_obj.delete_kth_element(k)

  print("5. Linked List after Deletion")
  ll_obj.print_list()
