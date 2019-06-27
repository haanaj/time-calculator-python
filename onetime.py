#get the time after inputting a set time and the amount of time elapsed

#get user input
print("")
print("Welcome to the time calculator! This will give you a start/end time based on your inputs.")
print("")
shift = input("Do you want to go back in time or forward? Type B for back, and F for forward: ")
shift = shift.upper().replace(" ", "")

#personalize the inputs to the response of B or F

if shift == "B":
    currentHours = int(input("Type in the hr part of hr:mn of your end time: "))
    currentMinutes = int(input("Type in the mn part of hr:mn of your end time: "))
    currentTime = input("AM or PM: ")
    elapsedHours = int(input("How many hours would you like to go back?: "))
    elapsedMinutes = int(input("How many minutes would you like to go back?: "))
    print()
else:
    currentHours = int(input("Type in the hr part of hr:mn of your start time: "))
    currentMinutes = int(input("Type in the mn part of hr:mn of your start time: "))
    currentTime = input("AM or PM: ")
    elapsedHours = int(input("How many hours would you like to go forward?: "))
    elapsedMinutes = int(input("How many minutes would you like to go forward?: "))
    print()

currentTime = currentTime.upper().replace(" ", "")

#create the hours variable for the end/start time

hours = currentHours
minutes = 0
current = currentTime

#calculate the forward time first

if(shift == "F"):
    minutes = elapsedMinutes + currentMinutes #get the total minutes
    if(minutes >= 60): #if greater than an hour, we add an hour and take the remainder of the minutes
        hours += 1
        minutes -= 60
    counter = 0 #set a counter
    while(counter != elapsedHours): #while the counter isn't equal to the hours limit
        counter += 1 #increment the counter
        hours += 1 #add an hour
        if(hours >= 12): #if we reach 12, that means we need to switch over to am or pm
            if(current == "AM"):
                current = "PM"
            else:
                current = "AM"
            hours -= 12 #start over
    #format the hours
    if hours == 0:
        hours = 12
    #format the minutes
    counter2 = 0
    if(currentMinutes < 10):
        while(currentMinutes >= counter2):
            if(currentMinutes == counter2):
                currentMinutes = "0" + str(counter2) 
                break
            counter2 += 1
    counter3 = 0
    if(minutes < 10):
        while(minutes >= counter3):
            if(minutes == counter3):
                minutes = "0" + str(counter3) 
                break
            counter3 += 1   
    #print the final statement
    print("If you start at " + str(currentHours) + ":" + str(currentMinutes) + " " + currentTime + " and " + str(elapsedHours) + " hours and " + str(elapsedMinutes)+ " minutes have passed, then you will end up at " + str(hours) + ":" + str(minutes) + " " + current + "." )
elif(shift == "B"): #check backwards now
    minutes = currentMinutes - elapsedMinutes #get the amount of minutes by going backwards
    if(minutes <= 0): #if this is a negative number, we add 60 to make it positive
        hours -= 1 #remove an hour since we go back
        minutes += 60
    elif(minutes <= 60): #if it's just less than 60, no worries, we don't change the minute variable
        hours -= 1
    counter = 0 #counter for while loop
    while(counter != elapsedHours): #while the counter doesn't equal our hours limit
        counter += 1 #add to the counter
        hours -= 1 #subtract an hour (since we go back)
        if(hours <= 0): #if the hours reaches 0, this means we have reached 12 am or pm
            if(current == "AM"): 
                current = "PM"
            else:
                current = "AM"
            hours += 12 #add 12 so we can begin subtracting again
    hours = abs(hours) + 1 #once the while loop is done, we change from negative to positive
    #correcting the issue with 0 and 13 am below
    if hours == 0:
        hours = 12
    if hours == 13:
        hours = 1
    #format the minutes
    counter2 = 0
    if(currentMinutes < 10):
        while(currentMinutes >= counter2):
            if(currentMinutes == counter2):
                currentMinutes = "0" + str(counter2) 
                break
            counter2 += 1
    counter3 = 0
    if(minutes < 10):
        while(minutes >= counter3):
            if(minutes == counter3):
                minutes = "0" + str(counter3) 
                break
            counter3 += 1   
    #print the final statement
    print("If you end at " + str(currentHours) + ":" + str(currentMinutes) + " " + currentTime + " and you have gone " + str(elapsedHours) + " hours and " + str(elapsedMinutes)+ " minutes back, then you will start at " + str(hours) + ":" + str(minutes) + " " + current + "." )





