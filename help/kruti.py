import string

fname = 'kruti.txt'

def fileStats(inFile, outFile):
    I = open(inFile)
    O = open(outFile, 'w')
    F = I.readlines()
    s = ''
    chars = 0
    wordlist = []
    for line in F: 
        chars += len(line)
        wordlist += line.split()
    s += "characters " + str(chars) + '\n'
    s += "lines " + str(len(F)) + '\n'
    s += "words " + str(len(wordlist)) + '\n'
    dCount = 0
    pCount = 0
    for i in wordlist:
        for j in i:
            if j in string.punctuation: pCount +=1
            if j in string.digits: dCount += 1
    s += "digits " + str(dCount) + '\n' + 'punctuation ' + str(pCount) + '\n'
    O.write(s)
    O.close()

fileStats(fname, 'out.txt')




