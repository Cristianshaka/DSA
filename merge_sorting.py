def merge_sort(list):
    """
    Sorts a list in ascending order
    returns a new sorted list

    divide: midpoint of the list and divides into sublists
    conquer: recursively sort the sublists created in previous step
    combine: Merge the sorted sublists created in previous step
    """
    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    divide the unsorted list at midpoint into sublists
    return two sublists left and right

    Takes O(log n) time
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    merges to lists (arrays), sorting them in the process
    returns a new merged list

    Takes O(n log n) time
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verif_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verif_sorted(list[1:])
alist = [45, 67, 32, 98, 56, 43, 87]
l = merge_sort(alist)
print(verif_sorted(alist))
print(verif_sorted(l))
print(l)
