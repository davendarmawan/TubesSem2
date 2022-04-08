# Fungsi untuk split list
def splitlist(a,b):
    count = 1
    for i in a:
        if (i == b):
            count += 1 

    # split
    data = ["" for i in range (count)]

    j = 0
    for i in a:
        if (i != b):
            data [j] += i

        elif (i == b):
            j += 1

    return data

# Fungsi untuk split csv ke array-array kecil
def load_data(a):
    data = ""

    # Reading and copying file
    f = open (a, 'r')

    for i in f:
        data += i

    f.close()

    # Split data
    data_count = 0

    data1 = splitlist(data, "\n")

    for j in data1:
        data_count += 1

    data_organized = ["" for i in range (data_count)]

    k = 0
    while (k <= data_count - 1):
        for j in data1:
            data_organized[k] = splitlist(j, ";")
            k += 1

    return data_organized