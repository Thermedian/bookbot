def main():
    #open the text file to be processed
    with open("./books/frankenstein.txt") as f:
        text = f.read()
    #How many words are in the text file?
    num_words = getNumWords(text)
    print(f"{num_words} words found in the book")
    #How many times does a character appear in the text file?
    letterCount = getLetterCount(text)
    print(letterCount)
    printReport(letterCount)

#Take a text file, and return the number of words it contains
def getNumWords(text):
    #make a list of words from the text file by spliting on spaces
    words = text.split()
    return len(words)

#Take a text file and reurn a dictionary for the number of times a character appears
def getLetterCount(text):
    #create empty dictionary
    count = {}
    #loop through each character in the text file
    for character in text:
        #count upper case as lower case
        lowered = character.lower()
        if lowered in count:
            #this character has been seen before, add 1 to count
            count[lowered] += 1
        else:
            #new character seen, add to dictionary
            count[lowered] = 1
    return count
   
def printReport(letters):
    for character in letters:
        print("")
    #letterList.sort(reverse=True, key=)
    return

main()