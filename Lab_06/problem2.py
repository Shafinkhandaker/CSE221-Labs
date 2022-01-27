input_file1 = open("problem2_input1.txt", "r")
input_file2 = open("problem2_input2.txt", "r")
output_file1 = open("problem2_output1.txt", "w")
output_file2 = open("problem2_output2.txt", "w")


def LCS(X, Y, Z, output_file):
    x = [0]
    for char in X:
        x.append(char)
    y = [0]
    for char in Y:
        y.append(char)
    z = [0]
    for char in Z:
        z.append(char)
    m, n, o = len(x), len(y), len(z)

    dp = [[[0 for i in range(o)] for j in range(n)] for k in range(m)]
    t = [[[None for i in range(o)] for j in range(n)] for k in range(m)]

    for i in range(m):
        for j in range(n):
            for k in range(o):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                    t[i][j][k] = None

                else:
                    if x[i - 1] == y[j - 1] and x[i - 1] == z[k - 1]:
                        dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                        t[i][j][k] = "D"

                    else:
                        if dp[i - 1][j][k] >= dp[i][j - 1][k]:
                            max = dp[i - 1][j][k]
                            if max >= dp[i][j][k - 1]:
                                dp[i][j][k] = max
                                t[i][j][k] = "UUL"

                            else:
                                max = dp[i][j][k - 1]
                                dp[i][j][k] = max
                                t[i][j][k] = "LUU"

                        else:
                            max = dp[i][j - 1][k]
                            if max >= dp[i][j][k - 1]:
                                dp[i][j][k] = max
                                t[i][j][k] = "ULU"
                            else:
                                max = dp[i][j][k - 1]
                                dp[i][j][k] = max
                                t[i][j][k] = "LUU"

    output_file.write(str(dp[i][j][k]))
    output_file.write("\n")


x1 = input_file1.readline().strip()
y1 = input_file1.readline().strip()
z1 = input_file1.readline().strip()
LCS(x1, y1, z1, output_file1)

input_file1.close()
output_file1.close()

x1 = input_file2.readline().strip()
y1 = input_file2.readline().strip()
z1 = input_file2.readline().strip()
LCS(x1, y1, z1, output_file2)

input_file2.close()
output_file2.close()
