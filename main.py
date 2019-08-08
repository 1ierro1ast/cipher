import sys, subprocess, hashlib, zlib, base64

subprocess.call("cls", shell = True)


def atbashCipher(word,alphabet):
	res = []
	result = ""
	normalA = alphabet
	reverseA = list(reversed(alphabet))

	for i in range(0,len(word)):
		for j in range(0,len(normalA)):
			if word[i] == normalA[j]:
				res.append(reverseA[j])
	for p in range(0,len(res)):
		result += res[p]
	return result


def atbashDecipher(word,alphabet):
	res = []
	result = ""
	normalA = alphabet
	reverseA = list(reversed(alphabet))

	for i in range(0,len(word)):
		for j in range(0,len(reverseA)):
			if word[i] == reverseA[j]:
				res.append(normalA[j])
	for p in range(0,len(res)):
		result += res[p]
	return result


def caesarCipher(word,key,alphabet):
	res = []
	result = ""

	for i in range(0,len(word)):
		for j in range(0,len(alphabet)):
			if word[i] == alphabet[j]:
				res.append(alphabet[j-int(key)])
	for p in range(0,len(res)):
		result += res[p]
	return result


def caesarDecipher(word,key,alphabet):
	res = []
	result = ""

	for i in range(0,len(word)):
		for j in range(0,len(alphabet)):
			if word[i] == alphabet[j]:
				res.append(alphabet[j+int(key)])
	for p in range(0,len(res)):
		result += res[p]
	return result


def inputData():
	return input(splitter()+"\n| Choose language(EN,RU): ").lower(),(input("|| Word: ").lower()).replace(" ",""),input("|| Key: ")


def splitter():
	return "|==========================="


def logo():
	return splitter()+"\n|=========CiPh3R============"


def chooseLang(chLang):
	ruA = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
	enA = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	while True:
		if chLang == "ru":
			lang = ruA
			break
		elif chLang == "en":
			lang = enA
			break
		else:
			chLang = input(splitter()+"\n| Choose EN or RU only: ")
	return lang


def atbash():
	chOper = input(splitter()+"\n| Choose operation:\n| 1.Crypt\n| 2.Decrypt\n| 3.Exit\n| >>> ")
	data = inputData()

	if chOper == "1":
		res = "| "+atbashCipher(word = data[1], alphabet = chooseLang(data[0]))
	elif chOper == "2":
		res = "| "+atbashDecipher(word = data[1], alphabet = chooseLang(data[0]))
	elif chOper == "3":
		sys.exit(main())
	else:
		chOper = input(splitter()+"\n| Enter number:\n| 1.Crypt\n| 2.Decrypt\n| 3.Exit\n| >>> ")
	return res


def caesar():
	chOper = input(splitter()+"\n| Choose operation:\n| 1.Crypt\n| 2.Decrypt\n| 3.Exit\n| >>> ")
	data = inputData()

	if chOper == "1":
		res = "| "+caesarCipher(word = data[1], key = data[2], alphabet = chooseLang(data[0]))
	elif chOper == "2":
		res = "| "+caesarDecipher(word = data[1], key = data[2], alphabet = chooseLang(data[0]))
	elif chOper == "3":
		sys.exit(main())
	else:
		chOper = input(splitter()+"\n| Enter number:\n| 1.Crypt\n| 2.Decrypt\n| 3.Exit\n| >>> ")
	return res, data[2]


def saveToFile(data):
	with open('results.txt', 'a',encoding = "UTF-8") as file:
		file.write(data+'\n')
		file.close
	return data


def hash():
	chHash = input(splitter()+"\n| Choose hash function:\n| 1. md5\n| 2. sha1\n| 3. sha256\n| 4. sha512\n| 5. raw\n| 6. base64\n| 7. Exit\n| >>> ")
	dataHash = input(splitter() + "\n| Enter data for hash: ")
	while True:
		if chHash == "1":
			res = str(hashlib.md5(bytes(dataHash, encoding = "UTF-8")).hexdigest())
			title = "md5 hash: "
			break
		elif chHash == "2":
			res = str(hashlib.sha1(bytes(dataHash, encoding = "UTF-8")).hexdigest())
			title = "sha1 hash: "
			break
		elif chHash == "3":
			res = str(hashlib.sha256(bytes(dataHash, encoding = "UTF-8")).hexdigest())
			title = "sha256 hash: "
			break
		elif chHash == "4":
			res = str(hashlib.sha512(bytes(dataHash, encoding = "UTF-8")).hexdigest())
			title = "sha512 hash: "
			break
		elif chHash == "5":
			res = str(bytes(dataHash, encoding = "UTF-8"))
			title = "raw data: "
			break
		elif chHash == "6":
			print("not worked")
#			res = str(base64.b64encode(bytes(dataHash, encoding = "UTF-8")))
#			title = "base64 data: "
		elif chHash =="7":
			sys.exit(main())
			break
		else:
			chHash = input(splitter()+"\n| Enter number:\n| 1. md5\n| 2. sha1\n| 3. sha256\n| 4. sha512\n| 5. raw\n| 6. Exit\n| >>> ")

	return title + res


def cipher():
	chCipher = input(splitter()+"\n| Choose cipher function:\n| 1. Caesar\n| 2. Atbash\n| 3. Exit\n| >>> ")
	if chCipher == "1":
		data = caesar()
		res = data[0]
		title  = "caesar's cipher with key("+data[1]+"): "
	if chCipher == "2":
		res = atbash()
		title = "atbash's cipher: "
	return title + res


def mainMenu():
	chMain = input(splitter()+"\n| Choose function: \n| 1.Hash\n| 2.Cipher\n| 3.Start dictCombine\n| 4.Exit\n| >>> ")
	while True:
		if chMain == "1":
			print("| "+saveToFile(hash()))
			break
		elif chMain == "2":
			print("| "+saveToFile(cipher()))
			break
		elif chMain == "3":
			subprocess.call(["python","dictCombine.py"])
			subprocess.call(["python3","dictCombine.py"])
			break
		elif chMain == "4":
			sys.exit()
		else:
			chMain = input(splitter()+"\n| Enter number: \n| 1.Hash\n| 2.Cipher\n| 3.Exit\n| >>> ")


def main():
	print(logo())
	while True:
		mainMenu()

if __name__ == "__main__":
	sys.exit(main())