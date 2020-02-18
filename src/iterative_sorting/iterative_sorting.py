# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(len(arr)):#create starting point 
        lowest_num = arr[i]#create my lowest number variable and assign it to my starting point
        lowest_ind = i # created a variable to hold the lowest index which is currently i
        for j in range( i + 1, len(arr) ):# now I need to check the next index in the array and compare each element in the array
            if arr[j] < lowest_num:#start your comparison of arr[j] to arr[i]
                lowest_num = arr[j]#switch the variable value if the above statement is true
    


    


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr