def read():
    file = open('problem2_input1.txt', 'r')
    array = []
    for line in file:
        array.append(line.split())
    for i in range(len(array[1])):
        array[1][i] = int(array[1][i])
    arr1 = array[1]
    m1 = int(array[0][1])
    file.close()

    file = open('problem2_input2.txt', 'r')
    array = []
    for line in file:
        array.append(line.split())
    for i in range(len(array[1])):
        array[1][i] = int(array[1][i])
    arr2 = array[1]
    m2 = int(array[0][1])
    return m1, m2, arr1, arr2
    file.close()


def write(arr1, arr2, m1, m2):
    file = open('problem2_output1.txt', 'w')
    file.write(str(arr1[0:m1]))
    file = open('problem2_output2.txt', 'w')
    file.write(str(arr2[0:m2]))


def selectionSort(arr):
    for i in range(len(arr)):
        _min = i
        for j in range(i+1, len(arr)):
            if arr[_min] > arr[j]:
                _min = j
        temporary = arr[_min]
        arr[_min] = arr[i]
        arr[i] = temporary


m1, m2, arr1, arr2 = read()
selectionSort(arr1)
selectionSort(arr2)
print(arr1[0:m1])
print(arr2[0:m2])
write(arr1, arr2, m1, m2)
