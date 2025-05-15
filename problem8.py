def guess_the_number():

    secret_num = 6

    while True:
        user_input = int(input("Guess a number between 1 and 9: "))
        if 1<=user_input<=9:
            if user_input<secret_num:
                print("Your guess is almost there!")
            elif user_input> secret_num:
                print("Your guess is higher!")
            else:
                print("Your guess is correct!")
                break
            
        else:
            print("Invalid input. please enter your number 1 and 9")


guess_the_number()
