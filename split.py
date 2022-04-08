def splitlist(a):
    count = 1
    for i in a:
        if (i == ";"):
            count += 1 

    # split
    data = ["" for i in range (count)]

    j = 0
    for i in a:
        if (i != ";"):
            data [j] += i

        elif (i == ";"):
            j += 1

    return data