def read(filename):
    input_file = open(filename, "r")
    lst = []
    n, m = input_file.readline().split(" ")
    n, m = int(n), int(m)
    for line in input_file:
        time = line.split(" ")
        lst.append([int(time[1]), int(time[0])])
        lst = sorted(lst)
    return m, lst


def compute(lst, m):
    cur = 0
    store = [0 for _ in range(m)]
    ans = 0
    for task in lst:
        for j in range(len(store)):
            if task[1] >= store[j]:
                store[j] = task[0]
                ans += 1
                break
    return ans


def write(filename, ans):
    output_file = open(filename, "w")
    output_file.write(f"{ans}\n")


m1, lst1 = read("task2-input1.txt")
ans1 = compute(lst1, m1)
write("task2-output1.txt", ans1)


m2, lst2 = read("task2-input2.txt")
ans2 = compute(lst2, m2)
write("task2-output2.txt", ans2)
