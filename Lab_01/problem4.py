# problem 4
def read():
    file_A = open('problem_4_input_A.txt', 'r')
    A = []
    for line in file_A:
        row_of_A = line.split(' ')
        new_row_of_A = row_of_A[0:len(row_of_A)-1]
        new_row_of_A = [int(i) for i in new_row_of_A]
        A.append(new_row_of_A)
    file_A.close()

    file_B = open('problem_4_input_B.txt', 'r')
    B = []
    for line in file_B:
        row_of_B = line.split(' ')
        new_row_of_B = row_of_A[0:len(row_of_B)-1]
        new_row_of_B = [int(i) for i in new_row_of_B]
        A.append(new_row_of_B)
    file_B.close()
    return A, B


def write(C):
    file = open("problem_4_output.txt", "w")
    for line in C:
        file.write(str(line) + "\n")
    file.close()


def Multiply_matrix(A, B):
    n = len(B)
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                c[i][j] += A[i][k]*B[k][j]
    return c


A, B = read()
C = Multiply_matrix(A, B)
print(C)
write(C)
