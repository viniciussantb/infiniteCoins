'''
The onChange function below receives as a parameter the changeLeft, which is how much the change in coins will be,
then executes a call stack, which will decrease from the change the value corresponding to 
the name of the function (quarters = 25, dimes = 10, nickels = 5, pennies = 1). The last function to be called
(and the first to be finished) will be pennies, because has the smallest value among the functions, which will add
to the `change` list another list of values ​received in the parameters that correspond to the number of each type of coins
that will be contained in the change, increasing (5, 10, 25) the number of each coin in the finalization of each function.
Finally, the onChange function returns the `change` list that contains all possible change appended by the `pennies`
function.
'''

def pennies (change, changeLeft, quartersCount, dimesCount, nickelsCount):
  change.append([quartersCount, dimesCount, nickelsCount, changeLeft])

def nickels (change, changeLeft, quartersCount, dimesCount):
  decreaseCents = 0
  nickelsCount = 0
  while (changeLeft - decreaseCents > 0):
    nickelsLeft = changeLeft - decreaseCents
    pennies(change, nickelsLeft, quartersCount, dimesCount, nickelsCount)
    decreaseCents += 5
    nickelsCount += 1

def dimes (change, centsLeft, quartersCount):
  decreaseCents = 0
  dimesCount = 0
  while (centsLeft - decreaseCents > 0):
    dimesLeft = centsLeft - decreaseCents
    nickels (change, dimesLeft, quartersCount, dimesCount)
    decreaseCents += 10
    dimesCount += 1

def quarters(change, changeLeft):
  decreaseCents = 0
  quartersCount = 0
  while (changeLeft - decreaseCents > 0):
    quartersLeft = changeLeft - decreaseCents
    dimes(change, quartersLeft, quartersCount)
    decreaseCents += 25
    quartersCount += 1

def onChange(changeLeft):
  change = []
  quarters(change, changeLeft)
  return change

changeLeft = int(input('change cents: '))

print(onChange(changeLeft))
