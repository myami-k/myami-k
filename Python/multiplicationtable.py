# "while true", "try", "except" & "break" has been used to check if the input is an integer.
# "if" & "else" has been used to check the answer given and so, set the score higher.
# "random" has been used to get a random number from the list_random_numbers
import random
list_random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
score = 0

# asking the user to type a number and checking if he typed an integer:
while True:
    print('Which multiplication table do you want to revise?')
    try:
        int_number = int(input())
        break
    except ValueError:
        print('Sorry it is not a number')

# now printing questions number taken + random number:
while True:
    random_n = random.choice(list_random_numbers)
    print('What is', int_number, 'X', random_n)
    while True:
        try:
            int_answer = int(input())
            break
        except ValueError:
            print('Sorry it is not a number')
    # checking answers and setting score:
    if int_answer == int_number*random_n:
        print('Correct')
        score = score + 1
    else:
        print('False')
    # checking score to stop the loop
    if score == 10:
        break

# congrats
print('Congratulations, you have done the', int_number, 'multiplication table!')
exit()
