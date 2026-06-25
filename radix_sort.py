# Radix Sort Algorithm
#
# Radix-Sort(A, d) Pseudocode (CLRS; d = number of digits in the largest
# number in A):
#   1. for i = 1 to d
#   2.     use a stable sort to sort array A on digit i
#
# How it works:
#   Radix sort never compares whole numbers against each other — instead it
#   sorts digit-by-digit, starting from the least significant digit (ones
#   place) and working up to the most significant. Each pass groups numbers
#   by a single digit using counting sort, since digits only range over 0-9
#   (a small, fixed range counting sort handles in O(n)).
#
#   The critical requirement is that each digit pass must be a *stable* sort.
#   By the time you sort on the tens digit, the array is already ordered by
#   ones digit; a stable sort on the tens digit preserves that ones-digit
#   ordering for numbers that tie on the tens digit. Do enough passes (one
#   per digit, most significant digit last) and the array ends up fully sorted.
#
#   exp tracks which digit is currently being sorted on, as a place value:
#   1 (ones), 10 (tens), 100 (hundreds), etc. (num // exp) % 10 extracts that
#   digit. The outer loop keeps going while max_num // exp > 0 — once exp has
#   grown past the most significant digit of the largest number, every digit
#   has been processed and the loop stops; this is what determines d without
#   needing to compute it separately.
#
# Time Complexity: O(d * (n + k)) — d passes, each a counting sort over n
#                  elements with a digit range of k = 10 (constant), so this
#                  simplifies to O(d * n). Beats comparison sorts (O(n log n))
#                  when d is small relative to n.
#
# Space Complexity: O(n + k) — each pass allocates a count array of fixed
#                   size 10 and an output array of size n
#
# Stability: Stable overall, and not just incidentally — counting_sort_for_radix
#            places elements back-to-front each pass (same trick as
#            counting_sort.py), and that per-digit stability is exactly what
#            makes the multi-pass result correct, not just "nice to have"


def radix_sort(arr):
    max_num = max(arr)  # Need the largest number to know how many digits to process
    exp = 1              # Place value of the digit being sorted: 1, 10, 100, ...
    while max_num//exp > 0:                      # Stop once exp passes the most significant digit
        arr = counting_sort_for_radix(arr, exp)  # Stable sort on the current digit
        exp *= 10                                # Move to the next digit (place value)
    return arr


def counting_sort_for_radix(arr, exp):
    count = [0 for _ in range(10)]          # One bucket per possible digit, 0-9
    output = [0 for _ in range(len(arr))]

    # Tally how many numbers have each digit value at this place (exp)
    for num in arr:
        index = (num // exp) % 10  # Extract the digit at the current place value
        count[index] += 1

    # Accumulate: count[d] = how many numbers have a digit <= d at this place
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place back-to-front so numbers that tie on this digit keep the relative
    # order established by previous (less significant digit) passes
    for j in range(len(arr)-1, -1, -1):
        num = arr[j]
        index = (num // exp) % 10
        pos = count[index] - 1
        output[pos] = num
        count[index] -= 1
    return output
