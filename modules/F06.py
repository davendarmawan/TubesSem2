# Desainer : 16521106
# Coder : 16521142
# Tester : 16521322

# Akses: Admin
# Mengubah stok sebuah game pada toko dilakukan melalui input ID dan besar perubahan
# stok yang ingin dilakukan. Saat dilakukan pengubahan stok suatu game, perlu dilakukan
# validasi untuk memastikan stok game tersebut tetap valid setelah pengubahan (tidak
# negatif). Bila stok suatu game bernilai nol setelah pengubahan, tidak perlu dihapus dari
# sistem.

# load data
import primitif
data = primitif.load_data("data_game.csv")

# fungsi mencari ID game yang sesuai dengan input
def find_game(inp_baris, inp_data):
    ID_game = input("Masukkan ID game: ")
    found = False
    game = []
    for i in range(inp_baris):
        if ID_game == inp_data[i][0]:
            found = True
            game = inp_data[i]
    return found, game

# fungsi mengubah stok
def ubah_stok(inp_data):
    baris, kolom = primitif.dimensi_arr("data_game.csv")
    found, game = find_game(baris, inp_data)
    if found:
        change = int(input("Masukkan jumlah: "))
        initial = game[5]
        final = int(game[5]) + change
        game[5] = final
        if (final >= 0):
            if (change > 0):
                print(f"Stok game", game[1], "berhasil ditambahkan. Stok sekarang:", final)
            if (change < 0):
                print(f"Stok game", game[1], "berhasil dikurangi. Stok sekarang:", final)
        else:
            print(f"Stok game {game[1]} gagal dikurangi karena stok kurang. Stok sekarang: {initial} (< {abs(change)})")
    else:
        print("Tidak ada game dengan ID tersebut!")

# uji coba kode
ubah_stok(data)