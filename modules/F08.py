# Desainer : 16521106
# Coder : 16521142
# Tester : 16521322

# Akses: User
# User dapat membeli Game dengan menggunakan prosedur ini. Game yang telah dibeli akan masuk ke list Game yang dimiliki User. 
# Game hanya dapat dibeli user yang sama sebanyak satu kali. Terdapat 1 parameter yang wajib diisi pada prosedur ini, 
# yaitu ID Game yang akan dibeli user.

# catatan: modul ini perlu informasi user login jadi ini baru contoh implementasi saja

# load data
import primitif
data_game = primitif.load_data("data_game.csv")
data_riwayat = primitif.load_data("data_riwayat.csv")
data_user = primitif.load_data("data_user.csv")

# fungsi definisi baris dan data game.csv efektif
def game_eff(inp_data):
    baris, kolom = primitif.dimensi_arr("data_game.csv")
    baris_eff = baris - 1
    data_eff = [[0 for j in range(kolom)] for i in range(baris_eff)]
    for i in range(baris_eff):
        for j in range(kolom):
            data_eff[i][j] = inp_data[i+1][j]
    return baris_eff, data_eff

# fungsi menentukan game yang dimiliki
def game_list(inp_game, inp_riwayat, inp_user):
    my_id = inp_user[1][0]
    my_games = []
    my_baris = 0
    baris_riwayat, kolom_riwayat = primitif.dimensi_arr("data_riwayat.csv")
    baris_eff, data_eff = game_eff(inp_game)
    for i in range(baris_riwayat):
        found = False
        if my_id == inp_riwayat[i][3]:
            found = True
            owned_ID = inp_riwayat[i][0]
        if found:
            for j in range(baris_eff):
                if owned_ID == data_eff[j][0]:
                    owned_game = data_eff[j]
                    my_games += owned_game
                    my_baris += 1
    return my_games, my_baris

# fungsi membeli game
def beli_game(inp_game, inp_riwayat, inp_user):
    ID_game = input("Masukkan ID Game: ")
    my_games, my_baris = game_list(inp_game, inp_riwayat, inp_user)
    found = False
    for i in range(my_baris):
        if ID_game == my_games[i][0]:
            found = True
            print("Anda sudah memiliki Game tersebut!")
    if not(found):
        baris_eff, data_eff = game_eff(inp_game)
        for i in range(baris_eff):
            if ID_game == data_eff[i][0]:
                game = data_eff[i]
        stok = int(game[5])
        saldo = int(inp_user[1][5])
        harga = int(game[4])
        if stok > 0:
            if saldo >= harga:
                print(f"Game \"{game[1]}\" berhasil dibeli!")
                saldo -= harga
                inp_user[1][5] = str(saldo)
                stok -= 1
                game[5] = str(stok)
            else:
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
        else:
            print("Stok Game tersebut sedang habis!")

# uji coba kode
beli_game(data_game, data_riwayat, data_user)