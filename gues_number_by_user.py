import random
#user guessing function
def user_guess(limit):
    comp_number = random.randint(1,limit)
    guess = 0
    life = 5
    winner = True
    
    while(guess !=comp_number):
        if life > 0:
            guess = int(input("guess the number: "))
            if guess < comp_number:
                print("It is too low.! Try again")
            elif guess > comp_number:
                print("It is too high.! Try again") 
            life = life - 1    
            print(f"you have remained with {life} life")  
        else:
            print(f"you loose.! game over")
            winner = False
            break
    if winner:        
        print("Wow! you really got it, you win")

user_guess(10)

  


