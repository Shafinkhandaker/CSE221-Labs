def read(filename):
    input_file = open(filename, "r")
    lst = []
    n = int(input_file.readline())
    times = input_file.readline().split(" ")
    for i in range(len(times)):
        times[i] = int(times[i])
    times = sorted(times)
    odr = input_file.readline()
    return times, odr


def compute(lst, odr):
    time1 = 0
    time2 = 0
    jack = lst
    jill = []
    seq = ""

    for o in odr:
        if o == "J":
            if len(jack):
                jill.append(jack[0])
                time1 += jack[0]
                seq += str(jack[0])
                jack.pop(0)
        else:
            if len(jill):
                time2 += jill[-1]
                seq += str(jill[-1])
                jill.pop()
    return seq, [time1, time2]


def write(filename, sq, times):
    output_file = open(filename, "w")
    output_file.write(f"{sq}\n")
    output_file.write(f"Jack will work for {times[0]} hour/s\n")
    output_file.write(f"Jill will work for {times[1]} hour/s")


lst1, odr1 = read("task3-input1.txt")
seq1, times1 = compute(lst1, odr1)
write("task3-output1.txt", seq1, times1)


lst2, odr2 = read("task3-input2.txt")
seq2, times2 = compute(lst2, odr2)
write("task3-output2.txt", seq2, times2)
