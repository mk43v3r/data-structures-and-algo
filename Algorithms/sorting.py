# NOTE: There may be easier methods to do some stuff(e.g. separating a list into 
# left and right sublist), but I will do the way as taught in theory, for
# learning purposes. But in practice, I recommend using much easier methods to 
# avoid mental overhead.
# 
# Sorting will be done in ascending order
import sys

sys.path.append("../datastructures")

from heap import MinHeap

def bubble_sort(target_list):
    n = len(target_list)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if target_list[j] > target_list[j+1]:
                temp = target_list[j]
                target_list[j] = target_list[j+1]
                target_list[j+1] = temp

def insertion_sort(target_list):
    n = len(target_list)
    for i in range(1, n):
        for j in range(0, i):
            if (target_list[i-j] > target_list[i-j-1]):
                break
            temp = target_list[i-j]
            target_list[i-j] = target_list[i-j-1]
            target_list[i-j-1] = temp

def heap_sort(target_list):
    n = len(target_list)
    heap = MinHeap()

    for i in range(0, n):
        heap.insert(i)

    for i in range(0, n):
        target_list[i] = heap.deleteMin()

def _merge(target_list, start, mid, end):
    aux_list = [0 for i in range(end-start)]
    i, j, k = start, mid, 0

    while (i < mid and j < end):
        if (target_list[i] <= target_list[j]):
            aux_list[k] = target_list[i]
            i += 1
        else:
            aux_list[k] = target_list[j]
            j += 1
        k += 1
    
    if (j < end):
        while(j < end):
            aux_list[k] = target_list[j]
            k += 1
            j += 1
    else:
        while (i < mid):
            aux_list[k] = target_list[i]
            k += 1
            i += 1
    
    for i in range(end - start):
        target_list[start+i] = aux_list[i]

def _merge_sort_helper(target_list, start, end):
    if (end - start <= 1):  # List with one or less element
        return

    mid = (start + end) // 2
    _merge_sort_helper(target_list, start, mid)
    _merge_sort_helper(target_list, mid, end)
    _merge(target_list, start, mid, end)

def merge_sort(target_list):
    n = len(target_list)
    _merge_sort_helper(target_list, 0, n)

# Partition the list and returns the pivot index
def _partition(target_list, start, end):
    pivot_elem = target_list[end-1]
    i, j = start, start 
    # target_list[start:i] contains the items smaller than pivot_elem currently
    while (j < end-1):
        if target_list[j] <= pivot_elem:
            temp = target_list[j]
            target_list[j] = target_list[i]
            target_list[i] = temp
            i += 1
        j += 1
    target_list[end-1] = target_list[i]
    target_list[i]= pivot_elem

    return i
    
def _quick_sort_helper(target_list, start, end):
    if (end - start <= 1): return
    pivot = _partition(target_list, start, end)
    _quick_sort_helper(target_list, start, pivot)
    _quick_sort_helper(target_list, pivot+1, end)

def quick_sort(target_list):
    n = len(target_list)
    _quick_sort_helper(target_list, 0, n)