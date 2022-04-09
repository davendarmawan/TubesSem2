# Fungsi implementasi split(), dengan parameter (data, pemisah)
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

# Fungsi implementasi len(x) - Untuk menghitung besar list
def count_list (a):
    count = 0
    
    for word in a:
        count += 1

    return count

# Fungsi untuk mencetak padding
def print_padding (a):
    row = count_list(a)

    column = count_list(a[0])

    max = [0 for i in range (column)]

    # Find maximum words
    for i in range (column):
        for j in range (row):
            if (count_list(a[j][i]) > max[i]):
                max[i] = count_list(a[j][i])

    view = [["" for j in range (column)] for i in range (row)]

    for i in range (column):
        for j in range (row):
            view[j][i] = a[j][i] + " " * (max [i] - count_list (a[j][i]))

    return view