# Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String
def getMiddleThreeChars(sampleStr):
    middleIndex = int(len(sampleStr) / 2)
    print("Original String is", sampleStr)
    middleThree = sampleStr[middleIndex - 1:middleIndex + 2]
    print("Middle three chars are", middleThree)


getMiddleThreeChars("JhonDipPeta")
getMiddleThreeChars("Jasonay")