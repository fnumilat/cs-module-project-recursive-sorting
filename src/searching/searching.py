# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # Make sure that the Array has a length
    if start <= end:
        # Setting up the middle element of the Array
        mid = (start + end) // 2

        # Base Case: 
        # If target is in the middle then return the middle
        if arr[mid] == target:
            return mid
        # Recursive Case: 
        # If target is on the right side of the middle,
        # then item on the right of the middle becomes the new Start
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, end)
        # If target is on the left side of the middle,
        # then item on the left side of the middle becomes the new End
        else:
            return binary_search(arr, target, start, mid - 1)
    else:
        return - 1 # not found at all




# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

