def binary_search(sorted_array: list, goal: int):
    res = None
    # 0 1 2 3 4 5
    lo = 0
    hi = len(sorted_array) - 1

    while lo <= hi:
        mid = lo + (hi-lo)//2
        cur = sorted_array[mid]

        if cur == goal:
            return mid
        elif cur < goal:
            lo = mid + 1
        else:
            hi = mid - 1

    return res


if __name__=="__main__":
    a = [1,3,7,10,11,13,25,35,36,38,41,43,49,51,52]
    a = [1,2,4,5,6,8] # len is 6, hi = 6
    aim = 1
    print(binary_search(a, aim))



