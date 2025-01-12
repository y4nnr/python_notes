def bubble_sort(arr):
    # This function sorts a list 'arr' in ascending order using the Bubble Sort algorithm.
    # Bubble Sort works by repeatedly swapping adjacent elements that are in the wrong order.

    n = len(arr)
    # Get the number of elements in the list.
    # Example: If arr = [5, 3, 8, 6, 2], then n = 5.

    for i in range(n):
        # Outer loop runs 'n' times to ensure the list is fully sorted.
        # 'i' represents the current pass number, starting from 0.
        # On each pass, the largest unsorted element is moved to its correct position at the end.

        for j in range(0, n - i - 1):
            # Inner loop runs from index 0 to (n - i - 2) on each pass.
            # For the first pass (i = 0), this becomes range(0, 4) → [0, 1, 2, 3].
            # This avoids comparing already sorted elements at the end of the list.

            if arr[j] > arr[j + 1]:
                # Compare the current element (arr[j]) with the next element (arr[j + 1]).
                # If the current element is greater than the next, swap them.

                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Swap the two elements to place them in the correct order.
                # Example: If arr = [5, 3, 8, 6, 2], after the first swap it becomes [3, 5, 8, 6, 2].

        # After each pass of the outer loop, the largest unsorted element is moved to its correct position.
        # Example (after Pass 1): arr = [3, 5, 6, 2, 8] (8 is sorted).
    return arr
    # When all passes are complete, the list is fully sorted.
    # Example (final result): arr = [2, 3, 5, 6, 8]
print(bubble_sort([1,2,5,7,4,9,]))
