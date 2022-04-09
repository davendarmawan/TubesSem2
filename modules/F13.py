import primitif

def riwayat ():
    f = primitif.load_data("riwayat.csv")
    n = primitif.count_list (f)
    view = ["" for i in range (n-1)]

    j = 0
    for x in f:
        if (x[0] != "game_id"):
            view[j] = x
            j += 1

    if (view == []):
        bold = '\033[1m' + 'beli_game' + '\033[0m'
        print ("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah " + bold + " untuk membeli.")

    else:
        print ("Daftar game:")
        view = primitif.print_padding(view)
        no = 1
        for x in view:
            print (str(no) + ". " + x[0] + " | " + x[1] + " | " + x[2] + " | " + x[3] + " | " + x[4] + " | ")
            no += 1

riwayat()