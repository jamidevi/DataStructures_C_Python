def bubble_sort2(arr):
    swapped=1
    n=len(arr)
    for i in range(n):
        swapped=0
        for j in range(n-i-1):
            if greater(arr[j],arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def greater(value1,value2):
    return value1>value2

array=[34,98,23,45,78,35]
bubble_sort2(array)
print(array)  