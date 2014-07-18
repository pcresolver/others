__author__ = 'Steve Gledhill'
# This is from http://trevorappleton.blogspot.co.uk/2013/08/python-crossword-solver.html
"""
1 - Type in a word to check if its a real word.
2 - Open up a dictionary of real words to check against.
3 - Compare my word with the words in the dictionary.
4 - If word matches with a word in the dictionary report this is successful.
If it fails to match then I also need to report this back.
"""


def getdictionary():  # function used to open the dictionary file, get the contents and close the file
    with open('DictionaryE.txt') as dictionaryopen:  #with open closes the file also. or at least i think it does
        dictionarylist = dictionaryopen.read().split()  #reads file and splits each word as list elements
    return dictionarylist


inputtedWord = input('Please enter a word: ').lower()
print(inputtedWord)

dictionary = getdictionary()
print(dictionary[110])

if inputtedWord in dictionary:
    print("Well done, you know what a word is")
else:
    print("You're making that up!", inputtedWord, "is not a word.")