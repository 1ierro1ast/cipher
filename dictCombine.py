import sys, subprocess, hashlib, zlib, random


def saveToFile(data,filename):
	with open(filename, 'a',encoding = "UTF-8") as file:
		file.write(data+'\n')
		file.close
	return data


def hasher(hashType,data):
	if hashType == "md5":
		res = str(hashlib.md5(bytes(data, encoding = "UTF-8")).hexdigest())
	elif hashType == "sha1":
		res = str(hashlib.sha1(bytes(data, encoding = "UTF-8")).hexdigest())
	elif hashType == "sha2":
		res = str(hashlib.sha2(bytes(data, encoding = "UTF-8")).hexdigest())
	elif hashType == "sha256":
		res = str(hashlib.sha256(bytes(data, encoding = "UTF-8")).hexdigest())
	elif hashType == "sha512":
		res = str(hashlib.sha512(bytes(data, encoding = "UTF-8")).hexdigest())
	else:
		return print("incorrect hash type")
	return res


def hashData(hashType, dataList, filename):
	for i in dataList:
		hashData = hasher(hashType = hashType, data = i)
		saveToFile(data = str(hashData), filename = filename)
	return filename


def openDict(dictHash):
	with open(dictHash,"r",encoding = "UTF-8") as file:
		data = file.read()
		dataList = data.split("\n")
		return dataList


def brute(dataList,search):
	for i in dataList:
		if i == search:
			return i
			break


def bruteHash(dataList,data,hashType):
	for i in dataList:
		if str(hasher(hashType = hashType, data = i)) == data:
			return i
			break


def genPassDict(filename,minSize,maxSize,sizeList):
	ruA = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
	enA = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	
	for i in range(0,sizeList):
		lenW = random.randint(minSize,maxSize)
		word = ""
		for j in range(0,lenW):
			g = random.randint(0,len(ruA)-1)
			word += ruA[g]
		saveToFile(word,filename)
	return "success"


def logo():
	return splitter()+"\n|=========dictCombine==="


def splitter():
	return "\n|======================="


def inputDataBrute():
	print(splitter())
	passwordBase = input("| Enter password base name: ")
	word = input("| Enter check word: ")
	return passwordBase, word


def inputDataHashBrute():
	print(splitter())
	passwordBase = input("| Enter password base name: ")
	hash4Brute = input("| Enter hash for brute: ")
	hashType = input("| Enter hash type for brute(md5,sha1,sha2,sha256,sha512): ")
	return passwordBase, hash4Brute, hashType


def inputDataGenDict():
	print(splitter())
	dictData = input("| Enter dictionary name: ")
	wordMaxLen = int(input("| Enter max word lenght: "))
	wordMinLen = int(input("| Enter min word lenght: "))
	sizeList = int(input("| Enter wordlist size: "))
	return dictData, wordMinLen, wordMaxLen, sizeList


def inputDataHashDict():
	passwordBase = input("| Enter password base name: ")
	filename = input("| Enter new filename for base: ")
	hashType = input("| Enter hash type for brute(md5,sha1,sha2,sha256,sha512): ")
	return passwordBase, filename, hashType


def inputData():
	dictData = input("| Enter dictionary name: ")
	passwordBase = input("| Enter password base name: ")
	filename = input("| Enter new filename for base: ")
	word = input("| Enter check word: ")
	hash4Brute = input("| Enter hash for brute: ")
	hashType = input("| Enter hash type for brute(md5,sha1,sha2,sha256,sha512): ")
	return dictData, passwordBase, filename, word, hash4Brute, hashType


def main():
	print(logo())
	print(splitter())
	chMenu = input("\n| Choose function: \n| 1. Brute\n| 2. Create hash dictionary\n| 3. Create brute dictionary(no hash)\n| 4. Generate random words dictionary\n| 5. Exit\n| >>> ")
	if chMenu == "1":
		chBruteSubMenu = input("\n| Choose brute type(1 - no hash|2 - hash): ")
		if chBruteSubMenu == "1":
			data = inputDataBrute()
			print(brute(dataList = openDict(data[0]), data = data[1]))
		elif chBruteSubMenu == "2":
			data = inputDataHashBrute()
			print(bruteHash(dataList = openDict(data[0]), data = data[1], hashType = data[2]))
	elif chMenu == "2":
		data = inputDataHashDict()
		hashData(hashType = data[2],dataList = openDict(data[0]),filename = data[1])
	elif chMenu == "3":
		print("nothing")
	elif chMenu == "4":
		data = inputDataGenDict()
		genPassDict(filename = data[0],minSize = data[1],maxSize = data[2], sizeList = data[3])
	elif chMenu == "5":
		sys.exit()


if __name__ == "__main__":
	sys.exit(main())