"""
autoComplete.py
This file has the functionality to do a auto complete of words. The run has a command line input of file name which
contains all the words that are to searched for autocompletion. The words from the given file are read into a list
and sorted, printed. Then user is asked to enter a prefix to do a autocomplete. If a quit is given then the program will
terminate.

@author: Santosh Kumar Nunna (sn7916@rit.edu)
@author: Mouna Reddy Kallu (mk9014@rit.edu)
"""
import sys


def sort(knownsList):
    """
    The sort function sorts and prints the list of sorted version of the entered list input.
    It also updates the same list with the sorted elements.
    :param knownsList: list of words to be sorted
    :return: None
    """
    for index in range(len(knownsList) - 1):
        min = index
        for index1 in range(len(knownsList) - 1):
            if knownsList[min] < knownsList[index1]:
                knownsList[index1], knownsList[min] = knownsList[min], knownsList[index1]
    print("The sorted list is: ", knownsList)


def searchWord(knownsList, wordToSearch, index):
    """
    This function searches for the prefixed word from the knownlist of words starting with the index, and returns
     the index value of the next match.
    :param knownsList: input words list
    :param wordToSearch: word to be searched for
    :param index: index from which the search has to be started
    :return: index of the next match
    """
    for x in range(index, len(knownsList)):
        if knownsList[x].startswith(wordToSearch):
            print(knownsList[x])
            return x
    return -1


def bsearch(knownsList, wordToSearch, left, right):
    """
    This function does the prefix or word search for the entered input in the list of words from the file and returns
    the index of the first occurance.
    :param knownsList: list of words to be searched for
    :param wordToSearch: word to be searched
    :param left: leftmost index to start the search
    :param right: rightmost index to end the search
    :return: index of the matched word
    """
    if left > right:
        return left
    midIndex = (left + right) // 2
    if knownsList[midIndex] == wordToSearch:
        return midIndex
    elif knownsList[midIndex] > wordToSearch:
        return bsearch(knownsList, wordToSearch, left, midIndex - 1)
    else:
        return bsearch(knownsList, wordToSearch, midIndex + 1, right)


if __name__ == "__main__":
    knownsList = list()
    toQuit = False
    inputStatus = False

    try:
        fileName = sys.argv[1]
        file = open(fileName, "r")
        knownsList = file.read().split("\n")
        sort(knownsList)
        print("Welcome to Auto-Complete.\nUsage: Enter a prefix to auto-complete.\nEntering nothing will search for the "
              "next word with that prefix.\nEnter <QUIT> when asked for a prefix to exit.\n")
        while toQuit != True:
            wordToSearch = input("Enter a prefix to search for: ")
            if wordToSearch == "<QUIT>":
                print("Exiting Auto-complete! Good bye.")
                toQuit = True
            elif wordToSearch == "" and inputStatus == False:
                print("Enter a prefix to start searching!!")
                continue
            elif wordToSearch != "":
                inputStatus = True
                indexValue = bsearch(knownsList, wordToSearch, 0, len(knownsList)-1)
                if indexValue < len(knownsList) and knownsList[indexValue].startswith(wordToSearch):
                    print(knownsList[indexValue])
                else:
                    print("No Match")
                wordEarlier = wordToSearch
            elif wordToSearch == "" and inputStatus == True:
                indexValue = searchWord(knownsList, wordEarlier, indexValue + 1)
                if indexValue == -1:
                    indexValue = searchWord(knownsList, wordEarlier, 0)

    except(IndexError):
        print("File name not entered during command line! Try again!")
