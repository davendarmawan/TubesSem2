import os
import things as ts


def save(user=None, game=None, riwayat=None, kepemilikan=None):
    folder = input("Masukkan nama folder penyimpanan: ")
    abs_path = os.getcwd() + "\\" + folder
    print("Saving...")

    if not os.path.exists(abs_path):
        os.makedirs(abs_path)

    if user is not None:
        ts.write_csv("user.csv", user)
    if game is not None:
        ts.write_csv("game.csv", game)
    if riwayat is not None:
        ts.write_csv("riwayat.csv", user)
    if kepemilikan is not None:
        ts.write_csv("kepemilikan.csv", kepemilikan)

    # for (root, dirs, files) in os.walk(abs_path, topdown=True):
    #     print(root)
    #     print(dirs)
    #     print(files)
    print("Data telah disimpan di " + folder + "!")