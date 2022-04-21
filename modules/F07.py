# Desainer : 16521106
# Coder : 16521142
# Tester : 16521322

# Akses: User dan Admin
# Agar pengguna dapat melihat game-game yang ada di toko, toko harus bisa memberikan daftar game yang dimiliki. 
# Beberapa pengguna mungkin merupakan gamer yang up-to-date terhadap perkembangan game, sehingga ingin melihat 
# game yang terbaru, sedangkan beberapa di antaranya merupakan gamer yang suka mengoleksi game klasik. Selain 
# itu juga ada pengguna yang merupakan gamer dengan budget pas-pasan, sehingga perlu berpikir dua kali ketika 
# membeli Fifa 22.

# Oleh karena itu, selain menyediakan daftar game, toko juga harus bisa melakukan sorting terhadap game berdasarkan 
# harga dan tahun rilisnya. Pengguna bisa memberikan inputan berupa skema sorting dari daftar game yang ingin dilihat 
# ke dalam aplikasi. Terdapat 2 skema sorting, yaitu berdasarkan tahun rilis atau harga (satu saja, tidak ada kasus 
# di sort berdasarkan dua attribut), urutan bisa ascending atau descending. Pastikan skema sorting tervalidasi. 
# Parsing input skema sorting dibebaskan. Jika skema sorting dikosongkan, akan di sort berdasarkan ID ascending.

# load data
import primitif
data = primitif.load_data("data_game.csv")

# fungsi definisi baris dan data game.csv efektif
def game_eff(inp_data):
    baris, kolom = primitif.dimensi_arr("data_game.csv")
    baris_eff = baris - 1
    data_eff = [[0 for j in range(kolom)] for i in range(baris_eff)]
    for i in range(baris_eff):
        for j in range(kolom):
            data_eff[i][j] = inp_data[i+1][j]
    return baris_eff, data_eff

# fungsi sort ascending
def sortasc(inp_sort, inp_baris, inp_data):
    if inp_sort == "tahun+":
        j = 3
    else:
        j = 4
    for Pass in range(inp_baris-1):
        IMin = Pass
        for i in range(Pass+1, inp_baris):
            if inp_data[IMin][j] > inp_data[i][j]:
                IMin = i
        Temp = inp_data[IMin]
        inp_data[IMin] = inp_data[Pass]
        inp_data[Pass] = Temp
    return inp_data

# fungsi sort descending
def sortdsc(inp_sort, inp_baris, inp_data):
    if inp_sort == "tahun-":
        j = 3
    else:
        j = 4
    for Pass in range(inp_baris-1):
        IMax = Pass
        for i in range(Pass+1, inp_baris):
            if inp_data[IMax][j] < inp_data[i][j]:
                IMax = i
        Temp = inp_data[IMax]
        inp_data[IMax] = inp_data[Pass]
        inp_data[Pass] = Temp
    return inp_data

# fungsi print data berdasarkan masukan sort
def print_view(inp_data, inp_baris):
    view = primitif.print_padding(inp_data)
    for i in range(inp_baris):
        print(f"{i+1}. {view[i][0]} | {view[i][1]} | {view[i][2]} | {view[i][3]} | {view[i][4]} | {view[i][5]}")

# fungsi mengurutkan list game
def list_toko(inp_data):
    baris_eff, data_eff = game_eff(inp_data)
    sort = input("Skema sorting: ")
    if sort == "tahun+":
        data_sort = sortasc(sort, baris_eff, data_eff)
        print_view(data_sort, baris_eff)
        # tahun rilis ascending (menaik)
    elif sort == "tahun-":
        data_sort = sortdsc(sort, baris_eff, data_eff)
        print_view(data_sort, baris_eff)
        # tahun rilis descending (menurun)
    elif sort == "harga+":
        data_sort = sortasc(sort, baris_eff, data_eff)
        print_view(data_sort, baris_eff)
        # harga ascending (menaik)
    elif sort == "harga-":
        data_sort = sortdsc(sort, baris_eff, data_eff)
        print_view(data_sort, baris_eff)
        # harga descending (menurun)
    elif sort == '':
        print_view(data_eff, baris_eff)
        # id ascending (menaik)
    else:
        print("Skema sorting tidak valid!")

# uji coba kode
list_toko(data)