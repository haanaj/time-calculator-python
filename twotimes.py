#this is to get how much time has passed between two set times

#first, get the first time by asking for the hours, minutes, and AM/PM
print()
print("Welcome to the time calculator! This will calculate how much time has elapsed between two times.")
print("")
firstHours = int(input("Type the hr part of hr:mn for the start time: "))
firstMin = int(input("Type the mn part of hr:mn for the start time: "))
firstTime = input("AM or PM: ")

print("")

#second, get the second set of times
secondHours = int(input("Type the hr part of hr:mn for the end time: "))
secondMin = int(input("Type the mn part of hr:mn for the end time: "))
secondTime = input("AM or PM: ")

print("")

#clean up the firstTime and secondTime strings by capitalizing the entire srting and removing all spaces
firstTime = firstTime.upper().replace(" ", "")
secondTime = secondTime.upper().replace(" ", "")

#create a total hours and total minutes variable
totalHours = 0
totalMinutes = 0

#calculate the total minutes
if(firstMin != 0):
    totalMinutes = 60 - firstMin #this gets how many minutes pass before the next hour
    totalMinutes += secondMin #this adds on the second amount of minutes
    if(totalMinutes == 60): #if it simply equals one hour, then we just keep it at 0
        totalMinutes = 0
    elif(totalMinutes >= 60):
        totalMinutes = totalMinutes - 60
        
#get the total hours
if firstTime == secondTime:
    if firstHours == 12:
        totalHours = secondHours
    elif secondHours > firstHours:
        if((secondHours - firstHours) == 1 and totalMinutes < 60):
            totalHours = 0
        elif secondHours == 12 and secondTime == "AM": #if we want the difference between 1am and 12am, then it's 24 hours minus the first time
            totalHours = 24 - firstHours
        else: 
            totalHours = secondHours - firstHours
    else:
        totalHours = 24 + (secondHours - firstHours)
else:
    if(firstHours == secondHours):
        totalHours += 12
    else:
        totalHours = totalHours + (12 - firstHours)
        totalHours += secondHours
    

#string formatting for hr:mn
counter = 0
if(firstMin < 10):
    while(firstMin >= counter):
        if(firstMin == counter):
            firstMin = "0" + str(counter)
            break
        counter += 1
counter2 = 0
if(secondMin < 10):
    while(secondMin >= counter2):
        if(secondMin == counter2):
            secondMin = "0" + str(counter2) 
            break
        counter2 += 1           

#print out the statement

print("The total amount of time between " + str(firstHours) + ":" + str(firstMin) + " " + firstTime + " and " + str(secondHours) + ":" + str(secondMin) + " " + secondTime + " is " + str(totalHours) + " hours and " + str(totalMinutes) + " minutes.")
    
    


