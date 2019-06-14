# checks if letter passed to it is vowel or not
def isVowel(letter):
    letter = letter.lower()
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return True
    else:
        return False

def vowelWords(s):
    tempWord = ""
    kevinWords = []
    stuartWords = []
    length = len(s)
    for idx, char in enumerate(s): #iterate through each character in string
        if isVowel(char): # if character is a vowel
            for i in range(idx,length): #create words starting from it and end at len(s)
                tempWord = s[i:]
                kevinWords.append(tempWord)
        if not isVowel(char):
            counter = length
            while counter != 0:
                tempWord = s[idx:counter]
                stuartWords.append(tempWord)
                counter -= 1
    stuartWords = list(filter(None, stuartWords))
    kevinScore = len(kevinWords)
    stuartScore = len(stuartWords)
    if stuartScore > kevinScore:
        print("Stuart ", stuartScore)
    elif kevinScore > stuartScore: 
        print("Kevin ", kevinScore)
    else:
        print("Draw")
string = input()
vowelWords(string)
