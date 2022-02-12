word="ahjdncksa iasjdl lsndjha"
word1=word[::-1]
word2=''
for i in range(0,(len(word)+1)):
    if word[i:i+1]==word1[i:i+1]:
        word2+=''
    else:
        word2+=word[i:i+1]
print(word2)

print(word.replace(' ',''))