# Fungsi implementasi split(), dengan parameter (data, pemisah)
def splitlist(a,b):
    # Counting number of elements in list
    count = 1
    for i in a:
        if (i == b):
            count += 1 

    # Splitting elements into an array
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

    # Splitting data into smaller arrays
    data_count = 0

    data_unorganized = splitlist(data, "\n")

    for j in data_unorganized:
        data_count += 1

    data_organized = ["" for i in range (data_count)]

    k = 0
    while (k <= data_count - 1):
        for j in data_unorganized:
            data_organized[k] = splitlist(j, ";")
            k += 1

    # Reading and purging blank data "['']"
    count_blank = 0
    for x in data_organized:
        if (x == ['']):
            count_blank += 1

    data_final = ["" for i in range (data_count - count_blank)]
    l = 0
    for x in data_organized:
        if (x != ['']):
            data_final[l] = x
            l += 1

    return data_final

# Fungsi implementasi len(x) - Untuk menghitung besar list
def count_list (a):
    count = 0
    
    for word in a:
        count += 1

    return count

# Fungsi untuk mencetak padding
def print_padding (a):
    # Counting number of rows and column in the array
    row = count_list(a)
    column = count_list(a[0])

    # Find maximum word count in a particular column
    max = [0 for i in range (column)]
    
    for i in range (column):
        for j in range (row):
            if (count_list(a[j][i]) > max[i]):
                max[i] = count_list(a[j][i])

    # Adding spaces to data in a column to match the maximum word count
    view = [["" for j in range (column)] for i in range (row)]

    for i in range (column):
        for j in range (row):
            view[j][i] = a[j][i] + " " * (max [i] - count_list (a[j][i]))

    return view