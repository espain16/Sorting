# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrLeft, arrRight ):
    elements = len( arrLeft ) + len( arrRight )
    merged_arr = [0] * elements
    # TO-DO
    l = 0                           # create our  left cursor
    r = 0                           # create our right cursor

    for i in range(0, elements):
        if l >= len(arrLeft):       #if the left side is done
            merged_arr[i] = arrRight[r]   #merge with right side
            r += 1
        elif r >= len(arrRight):
            merged_arr[i] = arrLeft[l]
        elif 
    # if the right side is done 
    # if the left side is smaller 
    # if the right side is smaller 
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
