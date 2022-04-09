import primitif

def top_up ():
    f = primitif.load_data("user.csv")
    
    user = input("Masukkan username: ")
    saldo = int(input("Masukkan saldo: "))

    # Finding username
    found = False
    for x in f:
        if (x[1] == user):
            found = True

    if (found):
        for x in f:
            if (x[1] == user):
                money = int(x[5])

        if (saldo > 0):
            print ("Top up berhasil. Saldo " + user + " bertambah menjadi " + str(money + saldo) + ".")

            for x in f:
                if (x[1] == user):
                    x[5] = str(money + saldo)

        else:
            if (money + saldo < 0):
                print ("Masukan tidak valid.")

            else:
                print ("Top up berhasil. Saldo " + user + " berkurang menjadi " + str(money + saldo) + ".")

                for x in f:
                    if (x[1] == user):
                        x[5] = str(money + saldo)


    else:
        print ("Username " + "\"" + user + "\"" + " tidak ditemukan.")

    print (f)

top_up()