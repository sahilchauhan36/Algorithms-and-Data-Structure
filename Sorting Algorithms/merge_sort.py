# This program explains the functionality of Merge Sort
def merge_sort(a):
  length_of_array = len(a)
  if length_of_array > 1:

    # divide the array into two parts 
    mid = length_of_array//2
    left_array = a[:mid]
    right_array = a[mid:]

    # apply merge sort on both the sub-arrays
    merge_sort(left_array)
    merge_sort(right_array)   

    # intialize 3 pointer, i for left array, j for right array and k for final merged array
    i=0
    j=0
    k=0
    
    # sort and merge left and right array
    while i < len(left_array) and j < len(right_array):
      if left_array[i] < right_array[j]:
        a[k] = left_array[i]
        i = i + 1
      else:
        a[k] = right_array[j]
        j = j + 1
      k = k + 1
    
    # if length or left array is more than right array 
    while i < len(left_array):
      a[k] = left_array[i]
      k = k + 1
      i = i + 1
    
    #if length of right array is more than left array
    while j < len(right_array):
      a[k] = right_array[j]
      k = k + 1
      j = j + 1

  return a

a = [10,6,2,4,9,1,3,5,7,8]

print("Array Before Sorting :")
print(a)

merge_sort(a)

print("Array After Sorting :")
print(a)
