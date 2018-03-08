import AnalyzeInput
def analyzeIt():
    userTyped = input("You: ")
    analyzed = AnalyzeInput.AnalyzeInput(userTyped)
    analyzed.analyzeText()
    analyzeIt()
analyzeIt()
