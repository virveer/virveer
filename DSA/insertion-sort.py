'''
Time Complexity: O(N^2)
Spce Complexity: O(1)
Can be Online
Is Stable
'''
def insertion_sort(array: list):
    length = len(array)

    for i in range(length):
        # insert 1 element to the right position at a time
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                # swap the position
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            print(array)
        print("iteration ends")
    return array

if __name__=="__main__":
    a = [1,2,4,5,6,8] # len is 6, hi = 6
    a = [2,5,1,8,3,9]
    print(insertion_sort(a))