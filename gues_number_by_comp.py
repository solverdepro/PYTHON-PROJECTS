import random
#computer guessing function    
def computer_guess(limit):
    print(f"Think any number from 1 to 10 and computer will try to guess it, and enter H if it is higher or \
    L if it is lower than your number and C if it is a correct one")
    response = ""
    low = 1
    high = limit
    while(response != "c"):
        comp_number = random.randint(low, high)
        print(comp_number)
        response = input("enter feedback: ")
        if response == "h":
            high = comp_number - 1
        elif response == "l":
            low = comp_number + 1

    print("okay have a nice moment and welcome again")
computer_guess(10)