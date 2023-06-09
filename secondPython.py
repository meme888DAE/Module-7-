# This is the second Page of Python 


# These are examples of Boolean Expressions 
# If then statements & Decision Structures

userGrade = 65 

if userGrade < 70: 
    print( " You did not pass this test ")

# If Else Example 

userGrade = 90 

if userGrade < 89: 
    print( " You did not pass this test ")
else:
    print( " Congratulations: You passed the test ")

# These are examples of relational operators using elif

if userGrade < 89: 
    print( " You did not pass this test ")
elif userGrade < 95:
    print( " Congratulations: Well Done! You have passed the test  ")
elif userGrade < 60:
    print( "You really need to study and retake the exam" )
elif userGrade < 80: 
    print( "You passed, but did not comprehend all of the information" )


# This is an example of using equal sign 
userAge= 67

if userAge == 67:
    print( "we have a match ")
else: 
    print( "Your age isn't 67")

# Logical Operators 
# use of AND  logical operator in Boolean expression 

REQUIRED_GRADE = 85 
REQUIRED_GPA = 3

userGrade = 80
userGPA = 4 

if userGrade >= REQUIRED_GRADE and userGPA >= REQUIRED_GPA:
    print( " You are eligible for a scholarship ")
else:
    print( " Sorry, you are not eligible this year ")


# use of the OR  logical operator 

REQUIRED_MONEY = 20
REQUIRED_AGE = 18 

userAge = 29 
userMoney = 100 

if userAge < REQUIRED_AGE or userMoney <REQUIRED_MONEY:
    print( "You have to meet the requirements ")
else:
    print( "Enjoy the party" )
