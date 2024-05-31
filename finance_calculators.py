# This program allows the user choose to calculate either the returns on an investment or a bond repayment for a house
# An exception check is in place to catch any exception entered other than the correct input of 'investment' or 'bond'
# If the user chooses to calculate the returns on an investment, the user will be prompted to enter the principal the interest rate and the lenght of period he wants to invest
# The user will then be asked what type of investment he is doing; simple or compound and a formular is in place to calculate either investment type and the answer is stored in a variable amount
# An exception check is in place to catch any exception entered other than the correct input of 'simple' or 'compound'
# The program then displays the amount.  This is formatted with the round() function to make it suitable for currency
#
# If the user chooses to calulate a bond repayment for a house, the user will be prompted to enter the current value of the house, the rate and the repayment period
# A formular is in place to calculate the repayment and this is stored in the variable repayment
# The program then displays the repayment.  This is formatted with the round() function to make it suitable for currency


import math

#error = True  # The error variable will be used to ensure user enters a valid input. It is set to 'True' if the user enters a valid input

print("## Welcome To Capstone Financial Calculator ##")
print("")
print("Select one of the following options: ")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

while True:
    try:
        finance_option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
        finance_option = finance_option.lower()

        if finance_option == "investment":
            deposit = input("Enter how much do you plan on depositing: ")
            deposit = float(deposit)            
            interest_rate = input("Enter the interest rate on your investment (do not include the % sign): ")
            interest_rate = float(interest_rate)
            interest_rate = interest_rate / 100  # converts the interest to a decimal so an interest of 8% will be converted 0.08 for the purpose of the formula
            inv_period = input("How many years are you investing for: ")
            inv_period = int(inv_period)
            

            while True:   # A while loop was used to catch exceptions.  So that the program doesn't terminate each time a wrong input was entered.
                try:
                    interest = input("Enter either 'simple' for simple interest and 'compound' for compound interest: ")
                    interest = interest.lower()
                    
                    if interest == "simple":
                        amount = deposit  * (1 + interest_rate * inv_period)   #Calculate the total amount the user will be getting if simple interest
                        print(f"After {inv_period} years, your deposit investment of £ {round(deposit, 2)} will yield a total amount of £ {round(amount, 2)}")
                        break
                    elif interest == "compound":
                        amount = deposit * math.pow((1 + interest_rate), inv_period)  
                        amount = round(amount, 2)
                        print(f"After {inv_period} years, your deposit investment of £ {round(deposit, 2)} will yield a total amount of £ {round(amount, 2)}")
                        break
                    else:
                        raise Exception("You entered an invalid input!") # this defines the exception string to be displayed if an exception is caught i.e. if any other thing is entered other than 'simple' or 'compound'

                except Exception as error1:
                    print(error1)   # this displays the exception string above

            break

        elif finance_option == "bond":
            present_val = input("Please enter the present value of the house: ")
            present_val = float(present_val)
            interest_rate = input("Enter the interest rate: ")
            interest_rate = float(interest_rate)
            interest_rate = interest_rate / 100 # converts the interest to a decimal so an interest of 8% will be converted 0.08 for the purpose of the formula
            rep_period = input("Enter the number of months you plan to repay: ")
            rep_period = int(rep_period)
            repayment = (interest_rate * present_val)/(1 - (1 + interest_rate)**(-rep_period))
            print(f"The amount to be repaid on the home loan with a present value of £ {round(present_val, 2)} for a period of {rep_period} months is £ {round(repayment, 2)}")

            break

        else:
            raise Exception("You entered an invalid input!")  # this defines the exception string to be displayed if an exception is caught i.e. if any other thing is entered other than 'investment' or 'bond'
    
    except Exception as error2:
        print(error2)  

