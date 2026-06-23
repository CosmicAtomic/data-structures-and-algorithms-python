# Merge Sort Algorithm
#
# Merge-Sort (A, p, r) Pseudocode (1-based indexing as in CLRS):
#   1. If p < r
#   2.     q = (p + r) / 2
#   3.     MERGE-SORT(A, p, q)
#   4.     MERGE-SORT(A, q+1, r)
#   5.     MERGE(A, p, q, r)
#
# Merge(A, p, q, r) Pseudocode:
#   1.  n1 = q - p + 1
#   2.  n2 = r - q
#   3.  Let L[1 .. n1 + 1] and R[1 .. n2 + 1] be new arrays
#   4.  for i = 1 to n1
#   5.      L[i] = A[p + i - 1]
#   6.  for j = 1 to n2
#   7.      R[j] = A[q + j]
#   8.  L[n1 + 1] = ∞
#   9.  R[n2 + 1] = ∞
#   10. i = 1
#   11. j = 1
#   12. for k = p to r
#   13.     if L[i] ≤ R[j]
#   14.         A[k] = L[i]
#   15.         i = i + 1
#   16.     else A[k] = R[j]
#   17.         j = j + 1
#
# How it works:
#   Merge sort is a divide-and-conquer algorithm. It recursively splits
#   the array into two halves, sorts each half, then merges the two
#   sorted halves back into a single sorted array.
#
#   The key insight is that merging two already-sorted arrays is O(n):
#   just walk both arrays simultaneously with two pointers, always
#   picking the smaller of the two current elements.
#
# Time Complexity:
#   Best case:    O(n log n) — always divides and merges regardless of input
#   Worst case:   O(n log n)
#   Average case: O(n log n)
#
# Space Complexity: O(n) — requires extra arrays for the left and right halves
#
# Stability: Stable — the condition left[i] <= right[j] ensures equal elements
#            from the left half are placed before those from the right half


def merge_sort(arr):
    # Base case: an array of length 0 or 1 is already sorted
    if len(arr) > 1:
        mid = len(arr) // 2          # Find the midpoint to divide the array
        left_half = arr[:mid]        # Left subarray (indices 0 to mid-1)
        right_half = arr[mid:]       # Right subarray (indices mid to end)

        merge_sort(left_half)        # Recursively sort the left half
        merge_sort(right_half)       # Recursively sort the right half

        # Merge the two sorted halves back into arr
        merge(arr, left_half, right_half)


def merge(arr, left, right):
    i = 0  # Pointer for the left half
    j = 0  # Pointer for the right half
    k = 0  # Pointer for the main array (tracks where to place next element)

    # Compare the current elements of each half and place the smaller one into arr.
    # This replaces the ∞ sentinel trick from CLRS — we simply stop when one half
    # is exhausted and handle the remainder in the loops below.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= preserves stability for equal elements
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # If left half still has elements, copy them (right half is exhausted)
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # If right half still has elements, copy them (left half is exhausted)
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
