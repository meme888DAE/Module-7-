# This is the fourth installment - title functions 
# definition of functions 

# example function to display math 

#def displayMath():
    #print("The sum of 9*9 = 81")

#displayMath()

# Function Arguments
def displayMathAdvance(firstNumber, secondNumber ):
    answer = firstNumber + secondNumber
    print( "The sum of", firstNumber, "and", secondNumber, "is", answer )

#displayMathAdvance(9, 9)   

# Return Value Function 

def displayMathSuperAdvanced( firstNumber, secondNumber, thirdNumber):
    difference = firstNumber - secondNumber + thirdNumber
    return difference
superAdvanceDifference = displayMathSuperAdvanced(9,8,7)
print(superAdvanceDifference)

# Multiple Return Example
def applyBasicCalculations(firstNumber, secondNumber):
    
 sum = firstNumber + secondNumber
 difference = firstNumber - secondNumber
 product = firstNumber * secondNumber
 quotient = firstNumber / secondNumber

 return sum, difference, product, quotient

applyBasicCalculations(10,3)

def main():
    sum, differenceOutsideOfFunction, product, quotientReceived = applyBasicCalculations(4, 2)
    print( sum, differenceOutsideOfFunction, product, quotientReceived)

# This is a call
main; 