from f15 import *
import f16


def exit_program():
    save = ""
    while save.lower() != "y" and save.lower() != "n":
        save = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    if save.lower() == "y":
        f16.save(user, game, riwayat, kepemilikan)
        exit()
    else:
        exit()