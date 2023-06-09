# This is the fifth Python Page 
# Files and Exceptions

# writing a file - interpreter?
#def main ():
    #testFile = open ("testfile.txt", "w" )

    #testFile.write("2") 
    #testFile.write (("4") + "\n")
    #testFile.write (str (8))
#main()    

# reading from a file 
#def main ():

    #testFile = open ("testfile.txt", "r" )

    #line = testFile.readline()

    #while line != "":
       # print(line)
        #line = testFile.readline()

        #testFile.close()

#main() 

# exceptions - specific ones 
def main ():
    try:
        testFile = open ("testfile.txt", "r" )

        line = testFile.readline()

        while line != "":
            print(line)
            line = testFile.readline()
    except ValueError:
        print ("uh, something is wrong")
    except FileNotFoundError:
        print("Hello, Your file doesnot exist. Please fix it")    
    else:
        print("All systems are functioning")
    finally:
        testFile.close()

main()

# for any type of exception 
def main ():
    try:
        testFile = open ("testfile.txt", "r" )

        line = testFile.readline()

        while line != "":
            print(line)
            line = testFile.readline()
    except Exception as potentialError:
        print( potentialError)
    else:
        print("All systems are functioning")
    finally:
        testFile.close()
        print("End of program")

main()