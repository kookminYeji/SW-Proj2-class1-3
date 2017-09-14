import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "":
            continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try: #이름, 나이, 점수를 적지 않았을 때.
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
            except IndexError:
                print("Write Name, Age, Score")
            else:
                scdb += [record]
        elif parse[0] == 'del':
            try: #삭제할 이름을 적지 않았을 때.
                copy_scdb = scdb[:]
                for p in copy_scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except IndexError:
                print("Write Name for deletion")
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find': #정보를 찾을 이름을 적지 않았을 때.
            try:
                for k in scdb :
                    if k["Name"] == parse[1]:
                        for attr in sorted(k):
                            print(attr + "=" + str(k[attr]), end=' ')
                        print()
            except IndexError:
                print("Write name to find information")
        elif parse[0] == 'inc':
            try: #점수를 증가시킬 이름이나 점수를 적지 않았을 때.
                for i in scdb:
                    if i['Name'] == parse[1]:
                        a = int(i['Score']) + int(parse[2])
                        if a < 0: #점수가 음수일 때.
                            print("Score is nagative number")
                            break
                        else:
                            i['Score'] = a
            except IndexError:
                print("Write Name and Number")
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()



scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)