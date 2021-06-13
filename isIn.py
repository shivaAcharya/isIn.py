# python3
# Program to determine if a character is in an alphabetically ordered string.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    i = len(aStr)
    if i < 1:
        return False   
    
    # Bisection Search Algorithm
    testChar = aStr[round(i/2)]
    if testChar == char:
        return True
    elif testChar > char:
        subStr = aStr[:round(i/2)]
        return isIn(char, subStr) # Recursive function
    else:
        subStr = aStr[round(i/2)+1:]
        return isIn(char, subStr)

print(isIn('s', 'addfgghklsvwz'))