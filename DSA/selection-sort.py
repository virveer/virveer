'''
Time Complexity: O(N^2)
Spce Complexity: O(1)
Can't be Online
Isn't Stable
'''

def selection_sort(array: list):
    length = len(array)

    for i in range(length):
        min_index = i
        for j in range(i, length):
            if array[j] < array[min_index]:
                min_index = j

        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
        
    return array

if __name__=="__main__":
    a = [1,2,4,5,6,8] # len is 6, hi = 6
    a = [2,5,1,8,3,9]
    print(selection_sort(a))