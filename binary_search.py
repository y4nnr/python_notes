def binary_search(arr, target):
    # This function performs binary search on a sorted list 'arr' to find the target value.
    # If the target is found, it returns its index. Otherwise, it returns -1.

    left, right = 0, len(arr) - 1
    # Initialize two pointers:
    # 'left' points to the start of the list.
    # 'right' points to the end of the list.

    while left <= right:
        # Continue searching as long as the search space is valid (left <= right).

        mid = (left + right) // 2
        # Calculate the middle index of the current search space.
        # Use integer division to avoid decimals.

        if arr[mid] == target:
            # Check if the middle element is the target.
            return mid
            # If found, return the index of the target.

        elif arr[mid] < target:
            # If the middle element is less than the target,
            # narrow the search space to the right half.
            left = mid + 1

        else:
            # If the middle element is greater than the target,
            # narrow the search space to the left half.
            right = mid - 1

    return -1
    # If the target is not found, return -1.
print(binary_search([1,2,3,4,5,6,7,8,9], 8))