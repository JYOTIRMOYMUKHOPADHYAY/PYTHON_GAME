import random



def get_guess():
    return list(input("What is your guess?"))

def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code, userGuess):
    if userGuess == code:
        return "CODE CRACK"

    clues = []

    for ind,num in enumerate(userGuess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("CLOKSE")
    if clues == []:
        return ["nope"]
    else:
        return clues

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
secretCode = generate_code()
print(f"{secretCode} : Code has been generated, please guess a 3 digit number")# Another hint:

clueReport = []

while clueReport != "CODE CRACK":

    guess = get_guess()

    clueReport = generate_clues(guess, secretCode)

    print("Here is the result of your guess: ")
    for clue in clueReport:
        print(clue)
