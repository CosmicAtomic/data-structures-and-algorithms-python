# Counting Sort Algorithm
#
# Counting-Sort(A, B, k) Pseudocode (1-based indexing as in CLRS; B is the
# output array, k is the largest value in A):
#   1. Let C[0..k] be a new array
#   2. for i = 0 to k
#   3.     C[i] = 0
#   4. for j = 1 to A.length
#   5.     C[A[j]] = C[A[j]] + 1
#   6. // C[i] now contains the number of elements equal to i.
#   7. for i = 1 to k
#   8.     C[i] = C[i] + C[i - 1]
#   9. // C[i] now contains the number of elements less than or equal to i.
#   10. for j = A.length downto 1
#   11.     B[C[A[j]]] = A[j]
#   12.     C[A[j]] = C[A[j]] - 1
#
# How it works:
#   Counting sort doesn't compare elements at all — it counts them. Since the
#   input is known to be integers within a small range [0, k], you can count
#   how many times each value appears, then use those counts to work out
#   exactly where each value belongs in the sorted output, with no comparisons.
#
#   Three passes:
#     1. Tally — count[v] = how many times value v appears in arr.
#     2. Accumulate — turn those tallies into a running total, so
#        count[v] = how many elements are <= v. This running total doubles as
#        a map from "value" to "the last index that value should occupy in
#        the sorted output".
#     3. Place — walk the input *backwards*, placing each element at
#        count[value] - 1 in the output, then decrementing count[value] so
#        the next occurrence of that same value lands one slot earlier.
#        Walking backwards (instead of forwards) is what keeps equal elements
#        in their original relative order — see Stability below.
#
# Time Complexity: O(n + k) — one O(k) pass to zero out count, one O(n) pass
#                  to tally, one O(k) pass to accumulate, one O(n) pass to
#                  place. Only beats comparison sorts (O(n log n)) when k
#                  isn't much bigger than n.
#
# Space Complexity: O(n + k) — the count array is O(k), the output array is O(n)
#
# Stability: Stable — placing elements back-to-front means that when two equal
#            values both map to the same count[value], the one that appears
#            *later* in the input claims the higher slot first, leaving the
#            earlier one the lower slot — so their original relative order is
#            preserved in the output.
#
# Note: this assumes arr contains only non-negative integers (CLRS's [0, k]
# range). A negative value would index count[] from the end (Python wraps
# negative indices) instead of raising an error, silently producing a wrong
# result. An empty arr also breaks it immediately, since max(arr) raises
# ValueError on an empty sequence.


def counting_sort(arr):
    k = max(arr)  # Largest value in arr — count needs one slot per value 0..k
    count = [0 for i in range(0, k+1)]     # count[v] will track info about value v
    output = [0 for _ in range(len(arr))]  # Final sorted result, built up out of order

    # Pass 1 (Tally): count[v] = number of times v appears in arr
    for j in range(0, len(arr)):
        count[arr[j]] += 1

    # Pass 2 (Accumulate): turn tallies into a running total, so
    # count[v] = number of elements <= v (i.e. v's last position in the output)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Pass 3 (Place): walk arr back to front so equal values keep their
    # original relative order (see Stability above)
    for i in range(len(arr)-1, -1, -1):
        num = arr[i]
        pos = count[num] - 1   # count[num] elements are <= num, so num's last free slot is count[num]-1
        output[pos] = num
        count[num] -= 1        # Free up that slot for the next occurrence of num
    return output
