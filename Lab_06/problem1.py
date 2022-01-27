input_file = open("problem1_input.txt", "r")
output_file = open("problem1_output.txt", "w")


def lcs(s1, s2):
    x = [0]
    for s in s1:
        x.append(s)
    y = [0]
    for s in s2:
        y.append(s)

    m, n = len(x), len(y)
    dp = [[0 for i in range(m)] for j in range(n)]
    t = [[None for i in range(m)] for j in range(n)]

    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                t[i][j] = "diagonal"

            elif dp[i - 1][j] >= dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                t[i][j] = "up"

            else:
                dp[i][j] = dp[i][j - 1]
                t[i][j] = "left"

    lcs_length = dp[i][j]
    correctedness = lcs_length * 100 / len(s1)

    list = []
    t1 = t[i][j]
    while t1 != None:

        if t1 == "diagonal":
            list.append(j)
            i, j = i - 1, j - 1

        elif t1 == "up":
            i -= 1
        else:
            j -= 1

        t1 = t[i][j]

    while list != []:
        i = list.pop()
        if x[i] == "Y":
            output_file.write("Yasnaya ")
        elif x[i] == "P":
            output_file.write("Pochinki ")
        elif x[i] == "S":
            output_file.write("School ")
        elif x[i] == "R":
            output_file.write("Rozhok ")
        elif x[i] == "F":
            output_file.write("Farm ")
        elif x[i] == "M":
            output_file.write("Mylta ")
        elif x[i] == "H":
            output_file.write("Shelter ")
        else:
            output_file.write("Prison ")

    output_file.write("\n")
    output_string = "Correctness of prediction: {}%".format(correctedness)
    output_file.write(output_string)


sequence_length = input_file.readline().strip()
x = input_file.readline().strip()
y = input_file.readline().strip()

lcs(x, y)

input_file.close()
output_file.close()
