import random
def game():
    sec_num = random.randint(1, 100)
    max_attempts=9
    attempts=0
    won=False
    print("welcome to the GAME!")
    while attempts<max_attempts:
        guess=int(input(f"attempt {attempts +1}/{max_attempts} - try a number between 1 and 100:"))
        attempts+=1
        if guess<1 or guess>100:
            print("you have to choose a number between 1 and 100")
            game()
        elif guess>sec_num:
            print("Too high")
        elif guess<sec_num:
            print("Too low")
        else:
            print("CONGRATS! YOU ARE RIGHT")
            won=True
            break
    if not won:
        print(f"Sorry, you are out of attempts! The number was {sec_num}")
game()


