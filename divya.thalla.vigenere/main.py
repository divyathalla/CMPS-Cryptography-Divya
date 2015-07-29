##########################################
#Name:Thalla Divya
#Class:CMPS 5363 Cryptography
#Date:29 july 2015
#Program 2-Randomized Vigenere cipher
##########################################

import argparse
import randomized_vigenere as rv


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
	parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
	parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
	parser.add_argument("-s", "--seed", dest="seed",help="Integer seed")
	args = parser.parse_args()
	#generating a keyword
	seed=args.seed
	f = open(args.inputFile,'r')
	message = f.read()
	#encrypting the plaintext
	if(args.mode == 'encrypt'):
		imp=rv.encrypt(message,int(seed))
		#data = rv.encrypt(message,seed)
		o = open(args.outputFile,'w')
		o.write(str(imp))
		o.close()
    #decrypting the encoded message
	else:
		imp=rv.d_decrypt(message,int(seed))
		#data = rv.decrypt(cipherText,seed)
		o = open(args.outputFile,'w')
		
		o.write(str(imp))
		o.close()
    


if __name__ == '__main__':
    main()
    