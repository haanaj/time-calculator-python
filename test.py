#testing out bits of code here

#testing out the while loop that formats the minute string if under 10
counter = 0
firstMin = 0
if(firstMin < 10):
    while(firstMin >= counter):
        if(firstMin == counter):
            firstMin = "0" + str(counter)
            print(firstMin)
            break
        counter += 1