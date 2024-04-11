#Nick Riblett
#CIS129 Lab 8
#4/7/24
#This project will be able to tell if a word entered is a palindrome, spelled the same forwards and backwards, using a stack


def main():
    keepGoing = 'y'

    while keepGoing == 'y':
    #Declared Variables
        userWordList = []
        palindrom = []
        IS_PALIDROME = True

        userWord = input("""Enter a word and I'll tell you if it's
spelled the same backwards 
(special characters and numbers are ignored): """)
        userWord = userWord.lower() #changes all uppercase letters to lowercase

        for i in range(len(userWord)): #Creates empty lists of length userWord and loads userWordList with the user's word
            userWordList.append(i)
            userWordList[i] = userWord[i]

        #Validates the user entered only letters, deletes everything that is not
        userWordList = InputValidation(userWordList)
    
        #Creates an idetical list just reversed
        palindrom = userWordList[::-1]

        #Checks to make sure every letter is idetical and in the same place i.e. a palidrome
        for i in range(len(palindrom)):
            if userWordList[i] == palindrom[i]:
                continue
            else:
                IS_PALIDROME = False #Changes IS_PALINDROME to false if it isn't a palidrome
                break
        if IS_PALIDROME == True:
            print("\nThat is a palidrom!")
            print(''.join(userWordList), end = '')
            print(" is the same as ", end = '')
            print(''.join(palindrom))
        else:
            print("\nThat is not a palindrome")
            print(''.join(userWordList), end = '')
            print(" is not the same as ", end = '')
            print(''.join(palindrom))
        keepGoing = input("Would you like to enter another word?(y/n): ")
        print()

#Checks the users list does not contain special characters or numbers
def InputValidation(userList):
    specialChar = ['!','@','#','$','%','^','&','*','(',')','<','>','?','/','','|','[','{','}',']',',','.']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    counter = 0

    for i in range(-1, -len(userList) -1, -1):
        if userList[i] in specialChar or userList[i] == ' ' or userList[i] in numbers:
            userList.pop(i)
            userList.append(' ')
            counter = counter + 1
    if counter > 0:
        del userList[-counter:]

    return(userList)

main()