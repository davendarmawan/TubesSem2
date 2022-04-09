import primitif

def search_my_game():
    f = primitif.load_data("riwayat.csv")

    check_idn = False
    check_thn = False

    idn = input("Masukkan ID Game: ")
    if (idn != ""):
        check_idn = True

    thn = input("Masukkan Tahun Rilis Game: ")
    if (thn != ""):
        check_thn = True

    count = 0

    print("Daftar game pada inventory yang memenuhi kriteria:")
    
    # Kasus untuk ID kosong, namun tahun diisi
    if (not(check_idn) and check_thn):
        for x in f:
            if (x[0] != "game_id" and x[4] == thn):
                count += 1

        view = ["" for i in range (count)]

        if (count != 0):
            j = 0
            for x in f:
                if (x[0] != "game_id" and x[4] == thn):
                    view [j] = x
                    j += 1

            view = primitif.print_padding(view)
                
            no = 1
            for i in view:
                print (str(no) + ". " + i[0] + " | " + i[1] + " | " + i[2] + " | " + i[3] + " | " + i[4])
                no += 1
                
        else:
            print ("Tidak ada game pada inventory-mu yang memenuhi kriteria")

    # Kasus untuk ID terisi, namun tahun kosong
    elif (check_idn and not(check_thn)):
        for x in f:
            if (x[0] != "game_id" and x[0] == idn):
                count += 1

        view = ["" for i in range (count)]

        if (count != 0):
            j = 0
            for x in f:
                if (x[0] != "game_id" and x[0] == idn):
                    view [j] = x
                    j += 1

            view = primitif.print_padding(view)
                
            no = 1
            for i in view:
                print (str(no) + ". " + i[0] + " | " + i[1] + " | " + i[2] + " | " + i[3] + " | " + i[4])
                no += 1

        else:
            print ("Tidak ada game pada inventory-mu yang memenuhi kriteria")

    # Kasus untuk ID kosong dan tahun kosong
    elif (not(check_idn) and not(check_thn)):
        for x in f:
            if (x[0] != "game_id"):
                count += 1

        view = ["" for i in range (count)]
        if (count != 0):
            j = 0
            for x in f:
                if (x[0] != "game_id"):
                    view[j] = x
                    j += 1

            view = primitif.print_padding(view)

            no = 1
            for x in view:
                print (str(no) + ". " + x[0] + " | " + x[1] + " | " + x[2] + " | " + x[3] + " | " + x[4])
                no += 1

        else:
            print ("Anda tidak punya game!")

    # Kasus untuk ID terisi dan tahun terisi
    else:
        for x in f:
            if (x[0] != "game_id" and x[0] == idn and x[4] == thn):
                count += 1

        view = ["" for i in range (count)]

        if (count != 0):
            j = 0
            for x in f:
                if (x[0] != "game_id" and x[0] == idn and x[4] == thn):
                    view [j] = x
                    j += 1

            view = primitif.print_padding(view)
                
            no = 1
            for i in view:
                print (str(no) + ". " + i[0] + " | " + i[1] + " | " + i[2] + " | " + i[3] + " | " + i[4])
                no += 1


        else:
            print ("Tidak ada game pada inventory-mu yang memenuhi kriteria")

    return

search_my_game()