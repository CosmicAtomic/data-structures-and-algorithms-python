# Quick Sort Algorithm
#
# Quicksort(A, lo, hi) Pseudocode (1-based indexing as in CLRS):
#   1. if lo < hi
#   2.     p = PARTITION(A, lo, hi)
#   3.     QUICKSORT(A, lo, p - 1)
#   4.     QUICKSORT(A, p + 1, hi)
#
# Partition(A, lo, hi) Pseudocode:
#   1. pivot = A[hi]
#   2. i = lo - 1
#   3. for j = lo to hi - 1
#   4.     if A[j] <= pivot
#   5.         i = i + 1
#   6.         exchange A[i] with A[j]
#   7. exchange A[i + 1] with A[hi]
#   8. return i + 1
#
# How it works:
#   Quicksort is a divide-and-conquer algorithm, like merge sort, but it does
#   the hard work *before* recursing instead of after. PARTITION picks a pivot
#   (here, the last element of the current subarray) and rearranges the
#   subarray so everything <= pivot ends up to its left and everything >
#   pivot ends up to its right. The pivot is now in its final sorted position,
#   so quicksort recurses on the two sides independently.
#
#   Unlike merge_sort, which slices the array into new left/right lists,
#   quicksort never creates a new array. lo and hi simply mark the boundaries
#   of the subarray currently being partitioned, so every recursive call
#   keeps swapping elements inside the one original array — that's what makes
#   it an in-place sort.
#
# Time Complexity:
#   Best case:    O(n log n) — pivot consistently splits the subarray evenly
#   Worst case:   O(n²)      — pivot is always the smallest/largest element of
#                 the subarray (e.g. already-sorted or reverse-sorted input),
#                 since the pivot here is always A[hi]; one side of the
#                 partition ends up empty every time
#   Average case: O(n log n)
#
#   Fix: choosing the pivot randomly (or via median-of-three) instead of
#   always using A[hi] makes the worst case extremely unlikely in practice,
#   pushing the expected running time to O(n log n) regardless of input order.
#
# Space Complexity: O(log n) average / O(n) worst case — no extra arrays are
#                    used, but the recursion stack depth depends on how
#                    balanced the partitions are
#
# Stability: Not stable — partition() swaps elements based on position, not
#            original order, so equal elements can be reordered


def quick_sort(arr, lo, hi):
    # Base case: a subarray with fewer than 2 elements (lo >= hi) is already sorted
    if lo < hi:
        p = partition(arr, lo, hi)   # Partition around a pivot; p is its final sorted index
        quick_sort(arr, lo, p-1)     # Recursively sort everything left of the pivot
        quick_sort(arr, p+1, hi)     # Recursively sort everything right of the pivot


def partition(arr, lo, hi):
    pivot = arr[hi]  # Always choose the last element of the subarray as the pivot
    i = lo - 1        # i tracks the last index of the "<= pivot" zone

    # Walk the subarray, growing the "<= pivot" zone whenever we find an element
    # that belongs there.
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap arr[j] into the "<= pivot" zone

    # Everything from i+1 to hi-1 is > pivot, so place the pivot right after the
    # "<= pivot" zone — this is its final sorted position.
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i+1
