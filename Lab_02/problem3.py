def read():
    file = open("problem3_input1.txt", "r")
    array = []
    for line in file:
        array.append(line.split())
    for i in range(len(array[2])):
        array[2][i] = int(array[2][i])
    id1 = array[1]
    marks1 = array[2]
    file.close()

    file = open("problem3_input2.txt", "r")
    array = []
    for line in file:
        array.append(line.split())
    for i in range(len(array[2])):
        array[2][i] = int(array[2][i])
    id2 = array[1]
    marks2 = array[2]
    file.close()
    return id1, marks1, id2, marks2


def write(id1, id2):
    file = open('problem3_output1.txt', 'w')
    file.write(str(id1))
    file = open('problem3_output2.txt', 'w')
    file.write(str(id2))


def insertionSorting(A):
    for i in range(0, len(A)-1):
        temp = A[i+1]
        j = i
        while j >= 0:
            if A[j] < temp:
                A[j+1] = A[j]
            else:
                break
            j = j-1
        A[j+1] = temp


id1, marks1, id2, marks2 = read()
dictionary = {}
sorted_id1 = []
for i in range(len(marks1)):
    if marks1[i] in dictionary:
        dictionary[marks1[i]].append(id1[i])
    else:
        dictionary[marks1[i]] = [id1[i]]

insertionSorting(marks1)
for mark in marks1:
    for id1 in dictionary[mark]:
        if id1 not in sorted_id1:
            sorted_id1.append(id1)
for i in range(len(sorted_id1)):
    print(sorted_id1[i], end=' ')
print()
dictionary = {}
sorted_id2 = []
for i in range(len(marks2)):
    if marks2[i] in dictionary:
        dictionary[marks2[i]].append(id2[i])
    else:
        dictionary[marks2[i]] = [id2[i]]

insertionSorting(marks2)
for mark in marks2:
    for id2 in dictionary[mark]:
        if id2 not in sorted_id2:
            sorted_id2.append(id2)
for i in range(len(sorted_id2)):
    print(sorted_id2[i], end=' ')

write(sorted_id1, sorted_id2)
