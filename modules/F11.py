import primitif

def filterdata (a,l,c):
    count = 0
    for x in a:
        if (x[l] == c):
            count += 1

    if (count != 0):
        new = ["" for i in range (count)]
    
        j = 0
        for x in a:
            if (x[l] == c):
                new[j] = x
                j += 1

        return new

    else:
        return []

def search_game_at_store():
    f = primitif.load_data("game.csv")
    n = primitif.count_list (f)
    view = ["" for i in range (n-1)]

    j = 0
    for x in f:
        if (x[0] != "id"):
            view[j] = x
            j += 1

    # [0]:ID, [1]:nama, [2]:kategori, [3]:tahun_rilis, [4]:harga, [5]:stok
    data = ["" for i in range (5)]
    check = [False for i in range (5)]

    # Input data and validating input
    data[0] = input("Masukkan ID Game: ")
    if (data[0] != ""):
        check[0] = True

    data[1] = input("Masukkan Nama Game: ")
    if (data[1] != ""):
        check[1] = True

    data[4] = input("Masukkan Harga Game: ")
    if (data[4] != ""):
        check[4] = True

    data[2] = input("Masukkan Kategori Game: ")
    if (data[2] != ""):
        check[2] = True

    data[3] = input("Masukkan Tahun Rilis Game: ")
    if (data[3] != ""):
        check[3] = True

    print("Daftar game pada inventory yang memenuhi kriteria:")
    for i in range (5):
        if (check[i]):
            view = filterdata(view, i, data[i])

    if (view == []):
        print ("Tidak ada game pada inventory-mu yang memenuhi kriteria")

    else:
        # [0]:ID, [1]:nama, [2]:kategori, [3]:tahun_rilis, [4]:harga, [5]:stok
        view = primitif.print_padding(view)
        no = 1
        for x in view:
            print (str(no) + ". " + x[0] + " | " + x[1] + " | " + x[4] + " | " + x[2] + " | " + x[3] + " | " + x[5])
            no += 1

    return

search_game_at_store()