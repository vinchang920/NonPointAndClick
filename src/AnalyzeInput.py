#Seth Doubek 3/8/18
class AnalyzeInput(object):
    currentLocation = ""

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
        
        #Travel
        if keyword == 'travel':
            prefix = "You are traveling to"
            otherWord = sentence[1:]
            suffix = ''
            #Locations
            #The Courtyard
            currentLocation = ''
            if otherWord == ['the', 'courtyard'] or otherWord == ['to', 'the', 'courtyard']:
                suffix = " to the courtyard, good luck!"
                global currentlocation
                currentLocation = 'courtyard'
            else:
                suffix = " or you used an incorrect format, please try again"

        #Location
        elif keyword == 'location':
            prefix = "You are currently in "
            otherWord = sentence[1:]
            suffix = ''
            suffix = AnalyzeInput.currentLocation
            
            
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
        
        #They Goofed         
        else:
            prefix = "You used an incorrect keyword"
            suffix = ", Try again"
            
        #Objects
        print(prefix + suffix)
