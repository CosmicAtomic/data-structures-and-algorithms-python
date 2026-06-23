# Insertion Sort Algorithm
#
# Pseudocode (1-based indexing as in CLRS):
#   Insertion_sort(A)
#       for j=2 to A.length
#           key = A[j]
#           i = j - 1
#           while i > 0 and A[i] > key
#               A[i+1] = A[i]
#               i = i - 1
#           A[i+1] = key
#
# How it works:
#   Insertion sort builds a sorted subarray one element at a time.
#   At each step, it picks the next unsorted element (key) and inserts
#   it into its correct position within the already-sorted left portion
#   of the array — similar to how you sort playing cards in your hand.
#
# Time Complexity:
#   Best case:    O(n)   — array is already sorted; inner while loop never executes
#   Worst case:   O(n²)  — array is reverse sorted; maximum comparisons and shifts
#   Average case: O(n²)
#
# Space Complexity: O(1) — sorts in-place, no extra array needed
#
# Stability: Stable — equal elements preserve their original relative order
#            (the condition Arr[j] > key uses strict >, so equal elements are not moved)


def insertion_sort(Arr):
    # Outer loop: treat Arr[0..i-1] as the sorted portion, Arr[i..n-1] as unsorted.
    # Start at index 1 because a single element (index 0) is trivially sorted.
    for i in range(1, len(Arr)):

        key = Arr[i]  # The element to be inserted into the sorted portion
        j = i - 1    # Start comparing from the last element of the sorted portion

        # Shift elements of the sorted portion that are greater than key
        # one position to the right to make room for key.
        while j >= 0 and Arr[j] > key:
            Arr[j + 1] = Arr[j]  # Shift element right
            j -= 1               # Move one position left

        # j+1 is now the correct position for key:
        # either j == -1 (key is smallest so far) or Arr[j] <= key
        Arr[j + 1] = key

    return Arr  # Array is sorted in-place; returning it is a convenience
