# NOTE: There may be easier methods to do some stuff(e.g. separating a list into 
# left and right sublist), but I will do the way as taught in theory, for
# learning purposes. But in practice, I recommend using much easier methods to 
# avoid mental overhead.
# 
# Sorting will be done in ascending order

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