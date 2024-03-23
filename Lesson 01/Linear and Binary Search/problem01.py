
# Linear Search (Bruteforce method) => O(n)
# def locate_card(cards, target):
#     for i in cards:
#         if i == target:
#             return True

#     return False

# Binary Search => O(logn)
def locate_card(cards, target):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        if mid_number == target:
            return True
        elif mid_number < target:
            hi = mid - 1
        elif mid_number > target:
            lo = mid + 1

    return False

arr = [10, 9, 8, 7, 6, 5, 4, 3]
print(locate_card(arr, 11))
