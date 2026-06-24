# Bucket Sort Algorithm
#
# BucketSort(A) Pseudocode (CLRS, assumes A holds n values uniformly
# distributed over [0, 1)):
#   1. n = length[A]
#   2. Let B[0..n-1] be a new array
#   3. for i = 0 to n-1
#   4.     make B[i] an empty list
#   5. for i = 1 to n
#   6.     insert A[i] into list B[floor(n * A[i])]
#   7. for i = 0 to n-1
#   8.     sort list B[i] with InsertionSort
#   9. concatenate the lists B[0], B[1], ..., B[n-1] together in order
#
# How it works:
#   Bucket sort trades comparisons for arithmetic: it assumes the input is
#   spread roughly evenly across a known range (CLRS uses [0, 1)) and uses
#   that range to scatter elements into n buckets, where bucket i is meant
#   to hold the values in [i/n, (i+1)/n). Each bucket ends up small, so
#   sorting it individually is cheap — and because the buckets already sit
#   in order, concatenating them 0..n-1 gives back a fully sorted array.
#
#   This implementation sorts each bucket with Python's built-in .sort()
#   rather than calling insertion_sort() from insertion_sort.py — that's the
#   same step 8 from the pseudocode, just using a faster general-purpose sort
#   instead of a hand-rolled insertion sort.
#
# Time Complexity:
#   Best/Average case: O(n) — assuming input is uniformly distributed, each
#                       bucket ends up with O(1) elements, so sorting all
#                       buckets combined costs O(n)
#   Worst case:         O(n²) — if every element lands in the same bucket
#                       (e.g. clustered or badly distributed input), that one
#                       bucket holds all n elements and sorting it dominates
#
# Space Complexity: O(n) — n buckets are allocated alongside the input array
#
# Stability: Stable — elements are appended to buckets in their original
#            order, and the per-bucket sort (Python's Timsort) is itself stable
#
# Note: this assumes every element of arr is a float in [0, 1), exactly as
# CLRS specifies. A value of exactly 1.0 would map to bucket index n
# (int(n * 1.0) == n), which is out of range — valid bucket indices only go
# up to n-1 — and raises an IndexError.


def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]  # One empty bucket per element, B[0..n-1]

    # Scatter each element into the bucket matching its position in [0, 1)
    for num in arr:
        buckets[int(n * num)].append(num)

    # Sort each bucket individually (small buckets sort almost instantly)
    for bucket in buckets:
        bucket.sort()

    # Buckets are already in order, so concatenating them in order is enough
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result
