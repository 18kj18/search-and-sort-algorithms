def LinearSearch(l, arg, index=0):
    if l[index] == arg:
        return index
    else:
        return LinearSearch(l, arg, index+1)
    
print(LinearSearch([15, 4, 41, 13, 24, 14, 12, 21], 14))


def BinarySearch(l, arg, low = None, high = None):
    if low is None and high is None:
        l = sorted(l)
        low, high = 0, len(l)-1

    mid = (high + low)//2

    if l[mid] == arg:
        return mid
    elif l[mid] < arg:
        low = mid + 1
    else:
        high = mid - 1
    
    return BinarySearch(l, arg, low, high)

print(BinarySearch([2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37], 27))


def SimpleSort(l, l2 = []):
    min = l[0]
    for item in l:
        print(item)
        if item < min:
            min = item
    
    l2.append(min)
    l.remove(min)
    
    if l == []:
        return l2
    else:
        return SimpleSort(l)

print("Sorted = ",SimpleSort([9, 6, 10, 4, 8, 5, 7]))