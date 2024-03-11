song = open ('song.txt')
word_dict = {}
counter = 0
for line in song:
    words=line.rstrip()
    words=words.split()
    for word in words:
        if word.lower() in word_dict:
            word_dict[word.lower()]+=1
        else:
            word_dict[word.lower()]=1
for x in word_dict:
    if word_dict[x]==1:
        print(x)
        counter += 1 

print(counter)
song.close()
