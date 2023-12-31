#Python Program to Find the maximum number in an array.

def max(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max

arr=[1,2,7,3,8]
n=len(arr)
ans=max(arr,n)
print("The maximum number is ",ans)




# SELECTION SORT: A sorting algorithm that compares two values and swaps them in increasing or decreasing order based on your code.

def selectionsort(array,length):
    for i in range(length):
        min_index = i
        for j in range(i+1,length):
            if array[j] < array[min_index]:
                min_index = j
                (array[i], array[min_index]) = (array[min_index], array[i])

arr = [1,4,3,5,2,6]
length= len(arr)
selectionsort(arr,length)
print(arr)




# Prime Numbers are the numbers that are only divisible by themselves. i.e. 2,3,5,7,11,13,17...
