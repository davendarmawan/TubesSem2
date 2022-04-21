# Desainer : 16521106
# Coder : 16521142
# Tester : 16521322

# Akses: User
# Prosedur ini memberikan daftar game yang dimiliki pengguna. Tidak ada aturan khusus untuk urutan game yang ditampilkan. 
# Tampilkan pesan khusus ketika user tidak memiliki game.

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

# fungsi print data game yang dimiliki
def print_view(inp_data, inp_baris):
    view = primitif.print_padding(inp_data)
    for i in range(inp_baris):
        print(f"{i+1}. {view[i][0]} | {view[i][1]} | {view[i][2]} | {view[i][3]} | {view[i][4]} | {view[i][5]}")

# fungsi print game yang dimiliki
def lihat_game(inp_game, inp_riwayat, inp_user):
    my_games, my_baris = game_list(inp_game, inp_riwayat, inp_user)
    if my_games != []:
        print("Daftar game:")
        if my_baris > 1:
            print_view(my_games, my_baris)
        else:
            print(f"{1}. {my_games[0]} | {my_games[1]} | {my_games[2]} | {my_games[3]} | {my_games[4]} | {my_games[5]}")
    else:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")

# uji coba kode
lihat_game(data_game, data_riwayat, data_user)