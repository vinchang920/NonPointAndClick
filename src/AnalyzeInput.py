#Seth Doubek 3/8/18
class AnalyzeInput(object):

    def __init__(self, text):
        self.text = str.lower(text)
    
    #This puts the sentence into a list of words
    def analyzeText(self):
        startWord = 0
        endWord = 0
        sentence = []
        for var in range(len(self.text)):
            letterList = self.text[var]
            spacePlace = letterList.count(' ')
            if spacePlace == 0:
                endWord += 1
            else:
                sentence.append(self.text[startWord:endWord])
                startWord = endWord + 1
                endWord += 1
        sentence.append(self.text[startWord:endWord])
        
        #This detects the first word
        keyword = sentence[0]
        prefix = ''
        #Change Location
        if keyword == 'travel':
            prefix = "You are traveling to"
            #This detects for other words
            otherWord = sentence[1:]
            suffix = ''
            #Locations
            #The Courtyard
            if otherWord == ['the', 'courtyard'] or otherWord == ['to', 'the', 'courtyard']:
                suffix = " to the courtyard, good luck!"
            else:
                suffix = " or you used an incorrect format, please try again"
            
        #Attack
        elif keyword == 'attack':
            prefix = "You are attacking "
            otherWord = sentence[1:]
            suffix = ''
            #NPCS
            if otherWord == ['the', 'old',  'man']:
                suffix = " the old man, RIP"
            else:
                suffix = " or you used an incorrect format, please try again"

        #Interaction
        elif keyword =='talk':
            prefix = "You are talking to"
            otherWord=sentence[1:]
            suffix = ''
            #NPC's
            if otherWord == ['the' , 'old', 'man'] or otherWord ==['to', 'the', 'old', 'man']:
                suffix =  " the old man, he says "
            else:
                prefix = "You used an incorrect format or tried to talk to a non-existent entity, please try again."
                
            
        #They Goofed         
        else:
            prefix = "You used an incorrect keyword"
            
        #Objects
        print(prefix + suffix)
