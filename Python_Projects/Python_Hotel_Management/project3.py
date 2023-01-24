# Created by Suchith Goud Veeramalla
# Date: 29/12/2021

import random
import datetime
import daytime

totalRooms={"Delux Rooms":5,"Delux Suites":5}

#Assigning Room numbers in a list
deluxRoomNumbers=[i for i in range(101,101+int(totalRooms.get("Delux Rooms")))]
deluxSuiteNumbers=[i for i in range(201,201+int(totalRooms.get("Delux Suites")))]



#Calculating Total number of Rooms
totalNumberOfRooms=int(totalRooms.get("Delux Rooms"))+int(totalRooms.get("Delux Suites"))
countRoom=0
countSuites=0
allotedRoomsList=[]

check_in_date=[]

def roomsAvailable(typer,countr,counts):
    if typer==1:
        if countr==0:
            numOfDelux=int(totalRooms.get("Delux Rooms"))
            #print(numOfDelux)# For first iteration, returns total Rooms mentioned in Dictionary
            return numOfDelux
        else:
            numOfDelux=int(totalRooms.get("Delux Rooms"))-countr
            #print(numOfDelux)# From Second iteration onwards, returns num of rooms available
            return numOfDelux
    elif typer==2:
        if counts==0:
            numOfSuites=int(totalRooms.get("Delux Suites"))
            return numOfSuites
        else:
            numOfSuites=int(totalRooms.get("Delux Suites"))-counts
            return numOfSuites

def allotRoomNum(typer):

    if typer==1:#For Delux Rooms
        while True:
            #I want to assign room number, It picks a random room from the available room numbers in the list with repetition
            tempAllot= random.choice(deluxRoomNumbers)
            if tempAllot not in allotedRoomsList:# Avoiding allocation of same rooms with this if statement
                allotedRoomsList.append(tempAllot)# Only appending the alloted rooms not present in the list
                return tempAllot
                break

    else:
        while True:
            tempAllot = random.choice(deluxSuiteNumbers)
            if tempAllot not in allotedRoomsList:
                allotedRoomsList.append(tempAllot)
                return tempAllot
                break

#Actual execution starts here
i=1

while True:
    Option=int(input("Hi Welcome to  XYZ Hotel. Would you like to 1.Check-in or 2.Check-out(1/2): "))
    if Option==1:

        for i in range(4):
            #make totalRooms.keys() as an indexable list
            availType = list(totalRooms.keys())

            #Display The available room types
            for x in range(len(availType)):
                print(x+1," ",availType[x])
            typeRoom = int(input("Hi Welcome, Please enter the type of the room you want to check-in (1/2):  "))
            if typeRoom==1:
            # Check for number of rooms available

                updatedRooms=roomsAvailable(typer=typeRoom,countr=countRoom,counts=countSuites)

                print("The number of Delux rooms available: ", updatedRooms)
                if (countRoom<totalRooms.get("Delux Rooms")):

                    allotedRoom=allotRoomNum(typer=typeRoom)
                    print("You are alloted with Room number:", allotedRoom)
                    check_in_date_variable = daytime.checkinDate()
                    check_in_date.append(check_in_date_variable)

                    #print("You have checked in at: {}".format(datetime.datetime.now()))
                    countRoom += 1

                    print("countroom is: ",countRoom)
                    break
                elif (countSuites<totalRooms.get("Delux Suites")) and (countRoom>=totalRooms.get("Delux Rooms")):
                    print("We regret for the inconvenience. Delux Rooms are unavailable at the moment. Please check with Suite Rooms by selecting 2 or select N if you want to exit: ",end=" ")
                    opt_r = input()
                    if opt_r.upper() == "N":
                        break
                    else:
                        continue

                else:
                    print("We have no vacant Rooms.")
                    break

            elif typeRoom==2:

                updatedRooms=roomsAvailable(typer=typeRoom,countr=countRoom,counts=countSuites)

                print("The number of Delux Suites available: ", updatedRooms)
                if(countSuites<totalRooms.get("Delux Suites")):
                    allotedRoom = allotRoomNum(typer=typeRoom)
                    print("You are alloted with Room number:", allotedRoom)
                    check_in_date_variable = daytime.checkinDate()
                    check_in_date.append(check_in_date_variable)
                    #print("You have checked in at: {}".format(datetime.datetime.now()))
                    countSuites += 1

                    print("countsuites is:",countSuites)
                    break
                elif (countSuites>=totalRooms.get("Delux Suites")) and (countRoom<totalRooms.get("Delux Rooms")):
                    print("We regret for the inconvenience. Delux Suites are unavailable at the moment. Please check with Delux Rooms by selecting 1 or select N if you want to exit: ",end=" ")
                    opt=input()
                    if opt.upper()=="N":
                        break
                    else:
                        continue

                else:
                    print("We have no vacant Rooms")
                    break


    elif Option==2:

        if len(allotedRoomsList)!=0:
            roomNumAlloted = int(input("Please enter the room number you want to Check-Out: "))
            if roomNumAlloted in allotedRoomsList:

                index_roomNumAlloted=allotedRoomsList.index(roomNumAlloted)
                print(index_roomNumAlloted)
                num_of_days = daytime.numOfDays(check_in_date[index_roomNumAlloted])
                print(num_of_days)
                print("You occupied the room for {} days and you need to pay INR {}".format(num_of_days,num_of_days*1000))
                check_in_date.remove(check_in_date[index_roomNumAlloted])
                allotedRoomsList.remove(roomNumAlloted)

                if roomNumAlloted in deluxRoomNumbers:
                    countRoom-=1
                    print("countroom reduced to: ",countRoom)
                elif roomNumAlloted in deluxSuiteNumbers:
                    countSuites-=1
                    print("countroom reduced to: ", countSuites)

                print("Thank You, Have A Nice Day")

                #print("You have checked out at: {}".format(datetime.datetime.now()))
            else:
                print("Enter a valid Room number")
                continue
        else:
            print("Please enter a valid input")
            continue

    else:
        break


    print("Occupied Rooms List",allotedRoomsList)
    print("Check-in date", check_in_date)