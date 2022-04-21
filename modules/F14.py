from things import read_csv,length

def help(uid,userDat):
    role = ''
    for i in range(0,length(userDat)):
        if (userDat[i][0] == uid):
            role = userDat[i][4]

    helps = read_csv("help.txt",'')
    number = 1

    if(role == 'User'):
        for i in range(0,length(helps),2):
            if ('u' in helps[i][0]):
                print('{}. {}'.format(number,helps[i+1][0]))
                number+=1
    else:
        for i in range(0,length(helps),2):
            if ('a' in helps[i][0]):
                print('{}. {}'.format(number,helps[i+1][0]))
                number+=1


udat = read_csv("tesuser.csv")
help("GAME002",udat)