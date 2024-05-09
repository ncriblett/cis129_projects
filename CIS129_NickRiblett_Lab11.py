#Nick Riblett
#CIS 129
#Lab 11
#Excersises 9.1, 9.2, 9.3 


#9.1
newGrade = 0
SENTIAL = '-99'

with open('grades.txt', mode= 'w', newline='') as grades: #Opens the file to write to
    while newGrade != SENTIAL:
        newGrade = input("Enter a grade(-99 to quit): ") #Gets the grades form the user
        if newGrade == SENTIAL: #breaks the loop when the user is done
            break
        grades.write(f'{newGrade}\n') #Writes newGrade to the text file

#9.2
#Delcared variables
newGrade = []
count = 0
sum = 0
j = 0
letterGrade = ''
p = 0
with open('grades.txt', mode= 'r') as grades: #Opens the file to read
    print(f'{"TOTAL":<10}{'GRADE':<10}{"COUNT":<10}{"AVERAGE":<10}')
    for i in grades: #Creates a list that holds all the grades
        newGrade.append('')
        record = i.replace('\n','') #Gets rid of the new line character
        newGrade[j] = int(record) #Turns the input from the file into an integer and stores it in the list newGrade
        sum += newGrade[j] #Calculates the sum of all the grades
        j += 1 # counter for the index
        count += 1 #counter for the average
    for k in range(len(newGrade)): #determines the letter grade 
        if newGrade[k] < 60:
            letterGrade = 'F'
        elif newGrade[k] >= 60 and newGrade[k] < 70:
            letterGrade = 'D'
        elif newGrade[k] >= 70 and newGrade[k] < 80:
            letterGrade = 'C'
        elif newGrade[k] >= 80 and newGrade[k] < 90:
            letterGrade = 'B'  
        elif newGrade[k] >= 90:
            letterGrade = 'A'
        if p != 1: 
            print(f"{newGrade[k]:<10}{letterGrade:<10}{count:<10}{sum / count:<10.2f}")
            p = 1
        else:
            print(f'{newGrade[k]:<10}{letterGrade:<10}')


#9.3
import csv
#declared variables
keepGoing = 'y'

with open('grades.csv', mode='w', newline='') as grades: #opens the csv 
    student = csv.writer(grades) #
    while keepGoing == 'y':
        firstName, lastName, exam1, exam2, exam3 = input("Enter students firstname, lastname, exam1grade, exam2grade, exam3grade: ").split(',')
        student.writerow([firstName, lastName, int(exam1), int(exam2), int(exam3)])
        keepGoing = input("Would you like to make another entry?(y/n): ")
	


