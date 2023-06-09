# Lists and Tuples which are both sequences 

#def main():
    #Travel = [" Paris", "Venice", "Greece", "Monaco", "British Isles"]
   #print( Travel)


   # main()

# print each name with for loop 
#def main():
    #travel = [" Paris", "Venice", "Greece", "Monaco", "British Isles"]
    
    #print( " The pLaces want to travel to again")
    #for currenttravelIndex in range (len( travel)):
        #print(travel[currenttravelIndex])


    #main()

# elif statement 
def main():
    travel = [" Paris", "Venice", "Greece", "Monaco", "British Isles"]
    
    print()
    print( " The pLaces want to travel to again")
    for currentTravelIndex in range (len( travel)):
        if currentTravelIndex == len(travel)- 1:
          print("and", travel[currentTravelIndex], end=".")
        elif currentTravelIndex == len (travel) - 2:
            print (travel [currentTravelIndex] , end="")
        else:
            print(travel [currentTravelIndex], end="")

    print()
    print()


main()

#tuples just like lists- used to store password
def main():
    daysOfTheWeek = ("Monday", "Tuesday", "Friday")
    print (type( daysOfTheWeek))

main()