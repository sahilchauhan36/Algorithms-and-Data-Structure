
###### Bubble Sort ######
a = list()
a = [2, 3, 1, 4, 5]
for i in range(0, 5):
  for j in range (i, 5):
    if a[j] < a[i]:
      a[j], a[i] = a[i], a[j]

print("Bubble Sort Output", a)

###### Insertion Sort ######
a = list()
a = [2, 3, 1, 4, 5]
for i in range(1, 5):
  temp = a[i]
  j = i-1
  while j >=0 and temp < a[j]:
    a[j+1] = a[j]
    j = j - 1
  a[j+1] = temp

print("Insertion Sort Output", a)

###### Selection Sort ###### 
a = list()
a = [2, 3, 1, 4, 5]
for i in range(0, 5):
  min_index = i
  for j in range (i, 5):
    if a[j] < a[min_index]:
      min_index = j
  if min_index != i:
    a[min_index], a[i] = a[i], a[min_index]

print("Selection Sort Output", a)

###### Heap Sort ######
def min_heapify(a, index, num):
  left = 2 * index + 1
  right = 2 * index + 2
  min_element = index
  if left < num and a[left] < a[min_element]:
    min_element = left
  if right < num and a[right] < a[min_element]:
    min_element = right
  if min_element != index:
    a[min_element], a[index] = a[index], a[min_element]
    min_heapify(a, min_element, num)

a = list()
a = [2, 3, 1, 4, 5]

# creation of heap with first element as smallest.
for i in range(4, -1, -1):
  min_heapify(a, i, 5)

# fetch the top element from top and reducte the size of heap by 1.
num = 5
for i in range(0,num):
    a[0], a[num-1] = a[num-1], a[0]
    num = num - 1
    min_heapify(a, 0, num)

print("Heap Sort Output", a)

###### Merge Sort ######  
def mergesort(a, left, right):
  mid = 0
  if left < right:
    mid = (left + right)//2
    mergesort(a, left, mid)
    mergesort(a, mid+1, right)
    merge(a, left, mid, right)
  return

def merge(a, left, mid, right):
  temp_left = a[left:mid+1]
  temp_right = a[mid+1:right+1]
  left_pt = 0
  right_pt = 0
  pt = left
  while left_pt < len(temp_left) and right_pt < len(temp_right):
    if temp_left[left_pt] < temp_right[right_pt]:
      a[pt] = temp_left[left_pt]
      left_pt += 1
    else:
      a[pt] = temp_right[right_pt]
      right_pt += 1
    pt += 1
  
  while left_pt < len(temp_left): 
    a[pt] = temp_left[left_pt]
    left_pt += 1
    pt += 1
  while right_pt < len(temp_right): 
    a[pt] = temp_right[right_pt]
    right_pt += 1
    pt += 1

a = list()
a = [2, 3, 1, 4, 5]
mergesort(a, 0, 4)

print("Merge Sort Output", a)

###### Quick Sort ######
def quicksort(a, left, right):
  if left < right:
    pivot = partition(a, left, right)
    quicksort(a, left, pivot-1)
    quicksort(a, pivot+1, right)
  return

def partition(a, left, right):
  i = left-1 
  j = left
  pivot = a[right]
  while j < right:
    if a[j] < pivot:
      a[i+1], a[j] = a[j], a[i+1]
      i += 1
    j += 1
  a[i+1], a[right] = a[right], a[i+1]
  return i + 1

a = list()
a = [2, 3, 1, 4, 5]
quicksort(a, 0, 4)
print("Quick Sort Output", a)
