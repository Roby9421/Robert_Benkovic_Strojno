ssc = open ('SMSSpamCollection.txt')
spamc=0
hamc=0
spamWords=0
hamWords=0
spamExc=0
for line in ssc:
    line=line.rstrip()
    words=line.split()
    if words[0]=="spam":
        spamc+=1
        spamWords+=len(words)-1
        if words[len(words)-1].endswith("!"):
            spamExc+=1
    else:
        hamc+=1
        hamWords+=len(words) -1
print("Spam message count: ",spamc, ", average word count: ",spamWords/spamc)
print("Spam messages ending with !: ",spamExc)
print("Ham message count: ",hamc, ", average word count: ",hamWords/hamc)
