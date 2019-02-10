# This program explains the program to merge two sorted linked list.

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

  # Module to merge a linked list with another linked list 
  def merge_list(self, list_2):
    # Get Pointer of both the lists
    pointer_1 = self.head 
    pointer_2 = list_2.head
    pointer_1_parent = None

    while pointer_1 != None and pointer_2 != None:
      
      if pointer_1.data > pointer_2.data:
        if pointer_1 == self.head:
          temp = pointer_2.next
          pointer_2.next = self.head
          self.head = pointer_2.next
          pointer_2 = temp
        else:
          temp = pointer_2.next 
          pointer_1_parent.next = pointer_2
          pointer_2.next = pointer_1 
          pointer_2 = temp
          pointer_1_parent = pointer_1_parent.next
      else:
        if pointer_1.data == pointer_2.data:
          pointer_2 = pointer_2.next
        else:
          if pointer_1_parent == None:
            pointer_1_parent = self.head
          else:
            pointer_1_parent = pointer_1_parent.next
          pointer_1 = pointer_1.next
      self.print_list()
      #print("[p1: %s][p2: %s][p1_head: %s]" %(pointer_1.data, pointer_2.data, pointer_1_parent.data))
        
    # If length is different or no element left to scan in list 1, perform merge
    if pointer_1 == None:
      pointer_1.next = pointer_2

if __name__=='__main__':
  # Create linked list 1
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  

  # Update head of the linked list 1
  print("2. Insert Elements in Linked list")
  ll_obj.insert(1)
  ll_obj.insert(3)
  ll_obj.insert(5)
  ll_obj.insert(7)

  # Print the list 1
  print("3. Linked List 1") 
  ll_obj.print_list()

  # Create a linked list 2
  print("1. Create a Linked List Object 2")
  ll_obj_2 = linked_list()
  

  # Update head of the linked list 2 
  print("2. Insert Elements in Linked list 2")
  ll_obj_2.insert(2)
  ll_obj_2.insert(4)
  ll_obj_2.insert(6)

  # Print the list 2
  print("3. Linked List 2") 
  ll_obj_2.print_list()


  # Merge
  print("4. Merging Linked List")
  ll_obj.merge_list(ll_obj_2)

  # Print the list after changes
  print("3. Linked List 1 after Merge") 
  ll_obj.print_list()

