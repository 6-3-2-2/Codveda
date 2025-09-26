import random
secret = random.randint(1, 100)
attempts = 7
for i in range(attempts):
    guess = int(input("Enter guess: "))
    if guess == secret:
        print("🎉 Correct!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print("Out of attempts! Number was:", secret)