# # Linear Search (Bruteforce method) => O(n)
# def locate_card(cards, target):
#     for i in cards:
#         if i == target:
#             return True

#     return False

# arr = [10, 9, 8, 7, 6, 5, 4, 3]
# print(locate_card(arr, 11))

# # Binary Search => O(logn)
# def locate_card(cards, target):
#     lo, hi = 0, len(cards) - 1

#     while lo <= hi:
#         mid = (lo + hi) // 2
#         mid_number = cards[mid]

#         if mid_number == target:
#             return True
#         elif mid_number < target:
#             hi = mid - 1
#         elif mid_number > target:
#             lo = mid + 1

#     return False

# arr = [10, 9, 8, 7, 6, 5, 4, 3]
# print(locate_card(arr, 11))

# More efficient
def test_location(cards, target, mid):
    mid_number = cards[mid]

    if mid_number == target:
        if mid - 1 >= 0 and cards[mid - 1] == target:
            return 'left'
        else:
            return 'found'
    elif mid_number < target:
        return 'left'
    elif mid_number > target:
        return 'right'

def locate_card(cards, target):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, target, mid)

        if result == 'found':
            return True
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1

    return False

arr = [10, 9, 9, 9, 7, 7, 7, 7, 6]
print(locate_card(arr, 11))