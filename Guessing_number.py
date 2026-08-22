import random
secret_number = random.randint(1,100)
guess_count = 0

while True:
    guess = int(input("enter guess:"))
    guess_count += 1

    if guess == secret_number:
        print("you got it🎉")
        print("attempts:", guess_count)
        break
    elif guess > secret_number:
        print("too high!")
    else:
        print("too low!")

