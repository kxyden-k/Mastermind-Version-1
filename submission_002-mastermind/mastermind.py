import random


def run_game():
    #for value in number()
    #Step1 randomize code
    number = []
    while (len(number)< 4):
        value = str(random.randint(1, 8))
        if value not in number:
            number.append((value))
    
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")

    #Step2 making sure input is correct
    guesses = 12
    while (guesses > 0):
        while True:
            try:
                code_input = int(input("Input 4 digit code: "))
            except:
                continue
            if (len(str(code_input)) == 4 and '0' not in str(code_input) and '9' not in str(code_input)):   
                break
            else:
                print("Please enter exactly 4 digits.")
                continue
        
        guess_str = str(code_input)
        guess_list = list(guess_str)

        #Step3
        count1 = 0
        count2 = 0
        for i in range(0,4):
            #if digit in number
            if (guess_list[i] in number ):
                count1 += 1
            #if digit in the correct place
            if (guess_list[i] == number[i]):
                count2 += 1
                count1 -= 1
        
        print("Number of correct digits in correct place:    ",count2)
        print("Number of correct digits not in correct place:",count1)
        if (count2 == 4):
            print("Congratulations! You are a codebreaker!") 
            
            break
        else:
            guesses -= 1
            print("Turns left:",guesses)

    print("The code was:","".join(number))


if __name__ == "__main__":
    run_game()
