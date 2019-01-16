# This Program explains the functionality of Heap sort which is considered as one of the fastest Sort.
def max_heapify(a, n, i):
  # i is the index in the array
  # n is the number of elements 
  # a is the array to sort
  left = 2 * i + 1
  right = 2 * i + 2
  print("left: %s, right %s, mid %s" % (left, right, i))
  max_element = i
  if left < n and a[left] > a[max_element]:
    max_element = left

  if right < n and a[right] > a[max_element]:
    max_element = right

  if max_element != i: 
    a[max_element], a[i] = a[i], a[max_element]
  
    max_heapify(a, n, max_element)

def heap_sort(a):
  num = len(a)

  # build a max heap
  for i in range(num,-1,-1):
    max_heapify(a, num, i)
  # Sort the elements in max heap that first element of the
  # heap becomes last element of the array
  for i in range(num-1, 0, -1):
    a[0], a[i] = a[i], a[0]
    max_heapify(a,i,0)

# Array to sort
a = [2,10,4,5,1,9,3,7,6,8]

# Array before Sorting 
print("Array Before Sorting ")
print(a)

# Sorting 
heap_sort(a)

# Array after Sorting 
print("Array After Sorting")
print(a)
