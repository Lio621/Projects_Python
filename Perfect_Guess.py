import random as r

val1 = r.randint(100, 500)

def guess_game(rand_val):
    i = 0
    while(1):
        val2 = int(input('Enter a number for guessing between 100 to 500 : '))
        if(val2 == rand_val):
            print('Perfect guess!')
            break
        elif(val2 > rand_val):
            print('Lower number please!')
        elif(val2 < rand_val):
            print('Higher number please!')
        i += 1
    return i

val3 = guess_game(val1)
print('Computer generated the number =',val1)
print(f'The perfect geuss cames after {val3+1} number of guesses.')