# Rock, paper and scissor
print('Choose r for rock, p for paper and s for scissor!')
import random as r

def match(comp, myinput):
    if(comp == myinput):
        return None
    elif(comp == 'r' and myinput == 'p'):
        return True
    elif(comp == 'p' and myinput == 's'):
        return True
    elif(comp == 's' and myinput == 'r'):
        return True
    else:
        return False

values = ('r', 'p', 's')
comp = r.randint(0,2)
comp = values[comp]
myinput = input('Enter your input : ')

win = match(comp, myinput)
print(f"You have choosen {myinput} and computer has choosen {comp}.")
if win is None:
    print('The match is draw.')
elif(win):
    print('Hurry! You bit the computer.')
else:
    print('Sorry! You loose. Better luck next time.')