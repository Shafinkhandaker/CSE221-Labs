def read():
    file = open('problem4_input1.txt', 'r')
    n = []
    for line in file:
        n.append(line.split())
    for i in range(len(n[1])):
        n[1][i] = int(n[1][i])
    arr1 = n[1]
    file.close()

    file = open('problem4_input2.txt', 'r')
    n = []
    for line in file:
        n.append(line.split())
    for i in range(len(n[1])):
        n[1][i] = int(n[1][i])
    arr2 = n[1]
    file.close()
    return arr1, arr2


def write(arr1, arr2):
    file = open('problem4_output1.txt', 'w')
    file.write(str(arr1))
    file = open('problem4_output2.txt', 'w')
    file.write(str(arr2))


def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q
    left = [0]*n1
    right = [0]*n2
    for i in range(0, n1):
        left[i] = A[p+i]
    for j in range(0, n2):
        right[j] = A[q+1+j]
    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < n1:
        A[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = right[j]
        j += 1
        k += 1


def merge_sort(A, p, r):
    if p < r:
        q = p+(r-p)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


arr1, arr2 = read()
merge_sort(arr1, 0, len(arr1) - 1)
merge_sort(arr2, 0, len(arr2) - 1)
print(arr1)
print(arr2)
write(arr1, arr2)
