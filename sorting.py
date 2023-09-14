#Design an application to create a list of TV channels (minimum 10) that includes the numbers of viewers and viewing time. 
#Rate the channels based on the number of viewers (1 High - 6 low). 
#Plot graphs to analyze the running times of different sorting algorithms.

import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt

def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0
        
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1 
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quickSort(array, low, high):
  if low < high:

    pi = partition(array, low, high)   
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

def selectionSort(array, size):

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
           
            if array[i] < array[min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])

def read_Input():
  a=[]
  n=int(input("Enter the number of TV Channels:"))
  print("enter the number of viewers")
  for i in range(0,n):
    l=int(input())
    a.append(l)
  return a;

elements = list()
times = list()
global labeldata
while True:
  print("1. Merge sort 2. Quick Sort 3. Selection Sort")
  ch=int(input("Enter the Choice"))
  if (ch == 1):
    array=read_Input()
    mergeSort(array)
    labeldata="MergeSort"
    print('Sorted Array is:')
    print(array)
  elif(ch==2):
    array=read_Input()
    size = len(array)
    labeldata="QuickSort"
    quickSort(array,0, size-1)
    print('Sorted Array is:')
    print(array)
  if (ch == 3):
    array=read_Input()
    size = len(array)
    labeldata="SelectionSort"
    selectionSort(array, size)
    print('Sorted Array is:')
    print(array)
  print("******************Running Time Analysis******************* ")
  for i in range(1, 10):
    array = randint(0, 1000 * i, 1000 * i)

    start = time.time()

    if ch==1:
       mergeSort(array)

    elif ch==2:
        size=len(array)
        quickSort(array, 0, size - 1)
    else:
        size=len(array)
        selectionSort(array,size)

    end = time.time()

    print(len(array), "Elements Sorted by", labeldata,end-start)
    elements.append(len(array))
    times.append(end-start)
  plt.xlabel('List Length')
  plt.ylabel('Time Complexity')

  plt.plot(elements, times, label=labeldata)
  plt.grid()
  plt.legend()
  plt.show()
