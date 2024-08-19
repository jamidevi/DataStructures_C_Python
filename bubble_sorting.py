def bubble_sort(arr):
    # Get the number of elements in the array
    n = len(arr)
    
    # Iterate over each element in the array
    for i in range(n):
        # Perform comparisons for the remaining unsorted part of the array
        for j in range(n - i - 1):
            # Compare adjacent elements
            if greater(arr[j], arr[j + 1]):
                # Swap elements if they are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

def greater(value1, value2):
    # Return True if value1 is greater than value2
    return value1 > value2

# Example array to be sorted
array = [10, 55, 89, 34, 65]

# Call the bubble_sort function to sort the array
bubble_sort(array)

# Print the sorted array
print(array)
