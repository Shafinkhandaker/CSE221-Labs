def read(filename):
    input_file = open(filename, "r")
    lst = []
    n = int(input_file.readline())
    for line in input_file:
        time = line.split(" ")
        lst.append([int(time[1]), int(time[0])])
        lst = sorted(lst)
    return lst


def compute(lst):
    cur = 0
    ans = []
    for task in lst:
        if task[1] >= cur:
            ans.append([task[1], task[0]])
            cur = task[0]
    return ans


def write(filename, ans):
    output_file = open(filename, "w")
    output_file.write(f"{len(ans)}\n")
    for u in ans:
        output_file.write(f"{u[0]} {u[1]}\n")


lst1 = read("task1-input1.txt")
ans1 = compute(lst1)
write("task1-output1.txt", ans1)


lst2 = read("task1-input2.txt")
ans2 = compute(lst2)
write("task1-output2.txt", ans2)
