# 20171583 kim ki bum
import pickle
import string

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
		for x in scdb:
			x['Age'] = int(x['Age'])
			x['Score'] = int(x['Score'])
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
	fH = open(dbfilename, 'wb')
	pickle.dump(scdb, fH)
	fH.close()


def doScoreDB(scdb):
	while (True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			if len(parse) == 4:
				try:
					parse[1] = string.capwords(parse[1])
					record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
					scdb += [record]
				except ValueError:
					print("ValueError Age Score must be int")
			else:
				print("put Name, Age, Score")
		elif parse[0] == 'del':
			for p in scdb:
				parse[1] = string.capwords(parse[1])
				if p['Name'] == parse[1]:
					scdb.remove(p)
		elif parse[0] == 'show':
			sortKey = 'Name' if len(parse) == 1 else parse[1]
			showScoreDB(scdb, sortKey)
		elif parse[0] == 'find':
			if len(parse) == 2:
				for p in scdb:
					parse[1] = string.capwords(parse[1])
					if parse[1] == p['Name']:
						for key in p:
							print(key + "=" + str(p[key]), end=' ')
						print()
			else:
				print("Enter finding Name")
		elif parse[0] == 'inc':
			if len(parse) == 3:
				for p in scdb:
					parse[1] = string.capwords(parse[1])
					if parse[1] == p['Name']:
						parse[2] = int(parse[2])
						p['Score'] += parse[2]
			else:
				print("Enter the Nmae, Ammount")
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
