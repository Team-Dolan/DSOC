# My Solutions

""""
Q1. Balanced Array Sum

Passed Test Cases: 10/13
""""

def balancedSum(arr):
    n = len(arr) #size of arr
    pivot = 0
    
    for i in range(1,n-1):
        if sum(arr[:i]) == sum(arr[i+1:n]):
                pivot = i
                break
    return pivot

""""
Q2. Reaching Points

Passed Test Cases: 10/11
""""

def canReach(x1, y1, x2, y2):
  if x1 == x2 and y1 == y2:
    return 'Yes'

  if x1 > x2 or y1 > y2:
    return 'No'

  if canReach(x1+y1, y1, x2, y2) == 'Yes' or canReach(x1, y1+x1, x2, y2) == 'Yes':
    return "Yes"
  return "No"