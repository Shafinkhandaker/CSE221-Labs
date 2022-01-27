def run(start=1, end=5):

    if start >= end:

        return 0

    else:

        return 1 + run(start + 2, end) + 3
