# Heap Sort Algorithm
#
# MaxHeapify(A, i) Pseudocode:
#   1.  l = left(i)
#   2.  r = right(i)
#   3.  if l <= heap-size[A] and A[l] > A[i]
#   4.      then largest = l
#   5.      else largest = i
#   6.  if r <= heap-size[A] and A[r] > A[largest]
#   7.      then largest = r
#   8.  if largest != i
#   9.      then exchange A[i] with A[largest]
#   10.         MaxHeapify(A, largest)
#
# BuildMaxHeap(A) Pseudocode:
#   1. heap_size = length[A]
#   2. for i = floor(length[A] / 2) down to 1
#   3.     MaxHeapify(A, i)
#
# HeapSort(A) Pseudocode:
#   1. BuildMaxHeap(A)
#   2. for i = length[A] down to 2
#   3.     exchange A[1] with A[i]
#   4.     heap_size = heap_size - 1
#   5.     MaxHeapify(A, 1)
#
# How it works:
#   Heap sort has two phases:
#     Phase 1 — BuildMaxHeap: rearranges the array into a max-heap, a binary
#               tree structure where every parent is >= its children. The largest
#               element ends up at index 0 (the root).
#     Phase 2 — Extraction: repeatedly swaps the root (current max) with the
#               last element of the heap, shrinks the heap by one, then calls
#               MaxHeapify to restore the heap property. After n-1 swaps the
#               array is sorted in ascending order.
#
#   A max-heap stored in an array uses these index relationships (0-based):
#     Parent of i:      (i - 1) // 2
#     Left child of i:  2*i + 1
#     Right child of i: 2*i + 2
#
# Time Complexity:
#   Best case:    O(n log n)
#   Worst case:   O(n log n)
#   Average case: O(n log n)
#   BuildMaxHeap runs in O(n); each of the n-1 MaxHeapify calls in HeapSort is O(log n)
#
# Space Complexity: O(1) — sorts in-place; recursion stack is O(log n)
#
# Stability: Not stable — the swap in the extraction phase can change the
#            relative order of equal elements


def max_heapify(arr, i, heap_size):
    # Compute the indices of the left and right children (0-based)
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Assume the current node is the largest; compare with children to find the true largest
    if left_child < heap_size and arr[left_child] > arr[i]:
        largest = left_child
    else:
        largest = i

    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    # If a child is larger than the current node, swap and recurse downward
    # to ensure the subtree rooted at 'largest' also satisfies the heap property
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)


def build_max_heap(arr):
    n = len(arr)
    # Start from the last non-leaf node and heapify downward to the root.
    # Leaf nodes (indices n//2 to n-1) are trivially valid heaps, so we skip them.
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n)


def heap_sort(arr):
    # Phase 1: turn the array into a max-heap so arr[0] holds the largest element
    build_max_heap(arr)

    n = len(arr)
    # Phase 2: repeatedly move the current max (root) to its final sorted position
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root (max) with the last heap element
        n -= 1                            # Shrink the heap, excluding the sorted element
        max_heapify(arr, 0, n)            # Restore heap property from the new root downward
