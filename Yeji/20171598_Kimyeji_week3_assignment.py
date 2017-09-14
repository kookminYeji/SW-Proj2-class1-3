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
		if inputstr == "": continue
		parse = inputstr.split(" ")

		if parse[0] == 'add':
			try:
				record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
			except:
				print("에러발생 다시 입력하시오", dbfilename)
			else:
				scdb += [record]
		elif parse[0] == 'del':
			for p in scdb:
				if p['Name'] == parse[1]:
					scdb.remove(p)
					continue
		elif parse[0] == 'show':
			try:
				sortKey ='Name' if len(parse) == 1 else parse[1]
			except:
				print("에러발생 다시 입력하시오", dbfilename)
			else:
				showScoreDB(scdb, sortKey)
		elif parse[0] == 'quit':
			break
		elif parse[0] == 'find':
			name = parse[1]
			for i in range(0,len(scdb), 1):
				temp = scdb[i]
				if name in temp.values():
					print(temp)
					break
		elif parse[0] == 'inc':
			name = parse[1]
			amount = parse[2]
			for i in range(0, len(scdb), 1):
				temp = scdb[i]
				if name in temp.values():
					temp['Score'] = int(temp['Score']) + int(amount)
				#parse2 = temp
			#if parse2[1] == "Name=" + name:
			#	print(temp)
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
