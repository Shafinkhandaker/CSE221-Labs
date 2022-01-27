def read():
    file = open('problem1_input1.txt', 'r')
    array = []
    for line in file:
        array.append(line.split())
    for i in range(len(array[1])):
        array[1][i] = int(array[1][i])
    arr1 = array[1]
    file.close()

    file = open('problem1_input2.txt', 'r')
    array = []
    for line in file:
        array.append(line.split())
    for i in range(len(array[1])):
        array[1][i] = int(array[1][i])
    arr2 = array[1]
    file.close()
    return arr1, arr2


def write(arr1, arr2):
    file = open('problem1_output1.txt', 'w')
    file.write(str(arr1))
    file = open('problem1_output2.txt', 'w')
    file.write(str(arr2))


def bubbleSort(arr):
    for i in range(len(arr)-1):
        do_Swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                do_Swap = True
                temporary = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temporary
        if do_Swap == False:
            break
    print(arr)


arr1, arr2 = read()
bubbleSort(arr1)
bubbleSort(arr2)
write(arr1, arr2)

# while im iterating the array in outer loop i am kepping a track
# whaether there is occuring any swap or not.
# Becuase if the array is already sorted it will not swap any element .
#  So if i found that there is no swapping is occur then
# i do break the outer loop in the code .
# then the best case is O(n).
