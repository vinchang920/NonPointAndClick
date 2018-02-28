text = input("DO IT: ")
text = str.lower(text)
startWord = 0
endWord = 0
sentence = []
#This puts the sentence into a list of words
for var in range(len(text)):
    letterList = text[var]
    spacePlace = letterList.count(' ')
    if spacePlace == 0:
        endWord += 1
    else:
        sentence.append(text[startWord:endWord])
        startWord = endWord + 1
        endWord += 1
sentence.append(text[startWord:endWord])

#This detects the first word
keyword = sentence[0]
if keyword == 'travel':
    prefix = "You are traveling to"
    
elif keyword == 'attack':
    prefix = "You are attacking "

#This detects for other words
otherWord = sentence[1:]
if otherWord == ['the', 'courtyard'] or otherWord == ['to', 'the', 'courtyard']:
    suffix = " to the courtyard, good luck!"
elif otherWord == ['the', 'old',  'man']:
    suffix = " the old man, RIP"

print(prefix + suffix)
