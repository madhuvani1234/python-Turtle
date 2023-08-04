#BINARY SEARCH
#blundr mistake is 1st i have given the arrya which is not soreted
#so i am not getting answer after long obs i found
#binary search means array shuld be given in sorted order
#Sorted array apply binary search
arr = [3, 12, 35, 78, 91]


def binarySearch(arr, ele):
  l = 0
  h = len(arr) - 1
  mid = 0
  while (l <= h):
    mid = (l + h) // 2
    if ele < arr[mid]:
      h = mid - 1
    elif ele > arr[mid]:
      l = mid + 1
    else:
      return mid

  return -1


se = binarySearch(arr, 3)
print(se)
