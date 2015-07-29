#########################################################
#Name: Thalla Divya
#Class: CMPS 5363 Cryptography
#Date: 29th July 2015
#Program 2 - Randomized Vigenere Cipher
#########################################################
import random
import sys

#Generates a random matrix
def buildVigenere(seed):
    random.seed(seed)
    symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    n = len(symbols)
    vigenere = [[0 for i in range(n)] for i in range(n)]
    symbols = list(symbols)
    random.shuffle(symbols)
    symbols = ''.join(symbols)
    
    for sym in symbols:
        random.seed(seed)
        myList = []
    
        for i in range(n):
            r = random.randrange(n)
            
            if r not in myList:
                myList.append(r)
            else:
                while(r in myList):
                    r = random.randrange(n)
            
                myList.append(r)
                               
            while(vigenere[i][r] != 0):
                r = (r + 1) % n
            
            vigenere[i][r] = sym
            
    return vigenere
	#function to create and print randomized vigenere matrix
def printMatrix():
    i=0
    j=0
    k=0
    line = ""

    for i in range(len(symbols)*len(symbols)):
        line = line + vigenere[j][k]
        j = j + 1
        if j >= 26:
            print(line)
            line = ""
            j = 0
            k = k + 1	
			
#############################################################

#Encryptes the message with the key and seed value
def encrypt(message,seed):
	key=keywordFromseed(seed)
	vigenere=buildVigenere(seed)
	cipherText = ""
	i=0
	for i in range(len(message)):
		mi = i
		ki = i % len(key)
		col = ord(message[mi]) - 32
		row = ord(key[ki]) - 32
		cipherText = cipherText + vigenere[row][col]
	return cipherText

	
#Decryptes the message with the key and seed value
def d_decrypt(cipherText,seed):
	DecText = ""
	key=keywordFromseed(seed)
	vigenere=buildVigenere(seed)
	i=0
	for i in range(len(cipherText)):
		emi = i
		ki = i % len(key)
		if ord(cipherText[i]) == 32:
			DecText = DecText + ' '
		else:
			DecText = DecText + decrypt(cipherText,key,ki,emi,vigenere)
	return DecText
	#--------------------------------------------------------------------  
def decrypt(cipherText,key,ki,emi,vigenere):
	#key=keywordFromseed(seed)
	row = ord(key[ki])-32
	message = cipherText[emi]
	#symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
	i = 0
	#n=len(symbols)
	for i in range(95):
		if cipherText[emi]==vigenere[row][i]:
			decryptchar=chr(i+32)
			return(decryptchar)
			i += 1
	#keyword is generated from seed      
def keywordFromseed(seed):
    Letters = []
    
    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)
    
	