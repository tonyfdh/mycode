#!/usr/bin/env python3

round = 0
correct="Brian"
secret="shrubbery"
while True:
    round = round + 1
    print('Finish the movie title, "Monthy Python\'s The Life of _____"')
    answer=input('Your guess-->')
    if answer.lower() == correct.lower():
        print('Correct')
        break
    elif round==3:
        print("Sorry, the answer was Brian.")
        break
    elif answer.lower() == secret.lower():
        print('We are the Knights who say NI!')
        print('You have brought us a shrubbery! You may pass!')
        break
    else:
        print("Sorry! Try again!")


