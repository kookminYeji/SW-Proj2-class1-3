import pickle

dbfilename = 'test3_4.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
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

def index_get(scdb , name):
    index = False
    for idx, row in enumerate(scdb):
        if row['Name'] == name:
            index = idx
            return index


def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
            scdb += [record]
        elif parse[0] == 'del':

            while True:
                if index_get(scdb,parse[1]):
                    print (scdb[index_get(scdb,parse[1])])
                    del scdb[index_get(scdb,parse[1])]
                else:
                    break


        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'inc':
            _index = index_get(scdb,parse[1])
            a = scdb[_index]
            _data = int(a["Score"])
            insert_data = int(parse[2])
            a["Score"] = insert_data + _data
            a["Score"] = str(a["Score"])

        elif parse[0] == 'find':
            print(scdb[index_get(scdb, parse[1])])
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')

        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
