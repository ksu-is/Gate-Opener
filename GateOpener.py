# lets get started
import random

lst = [1234, 4321, 0000, 5678]
def entry_code():
    num = ""
    holder = "Working! Welcome"
    while True:
        num = input("Please enter your four digit code: ")
        if int(num) in lst:
            return holder #people who already have acess to gate
            
        elif num not in lst:
            no_num = input("Sorry that code is not in our system\n Would you like to gain acess to this lot? (yes or no): ")
            if no_num == "yes":
                no_num_sub = input("Would you like a subscription or one time acess? (sub or one): ")
                if no_num_sub == "sub":
                    sub_num = random.randint(1000,9999)
                    return "Your new code is", sub_num ,"\n Thank you for your purchase!" # need to append the random number
                elif no_num_sub == "one":
                    return "Welcome!" # this where the gate would open up
            elif no_num == "no":
                return "OK, Thank you for your time!"
            

print(entry_code())
