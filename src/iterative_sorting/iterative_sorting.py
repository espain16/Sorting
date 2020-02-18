# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(len(arr)):#create starting point 
        lowest_num = arr[i]#create my lowest number variable and assign it to my starting point
        lowest_ind = i # created a variable to hold the lowest index which is currently i
        for j in range( i + 1, len(arr) ):# now I need to check the next index in the array and compare each element in the array
            if arr[j] < lowest_num:#start your comparison of arr[j] to arr[i]
                lowest_num = arr[j]#switch the variable value if the above statement is true
                lowest_ind = j #switch the variable value if the above statement is true
        temp = arr[i]# create a temp variable to hold the value that needs to be swapped so its not lost 
        arr[i] = lowest_num# arr[i] placeholder needs to be swapped with the current smallest value which is lowest_num
        arr[lowest_ind] = temp#arr[j] placeholder needs to be replaced with the proper value which is 
    return arr
    


    


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)): #going through the full length of the array 
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                tempy = arr[i]
                arr[i] = arr[j]
                arr[j] = tempy
      

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr