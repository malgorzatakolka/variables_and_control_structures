def input_validator(str_input, t = float):

    """
    A function that ask a user for an input, checks if the input can be casted to data type and returns casted value.
    Parameteres: str str_input, t -> data type
    Returns: user_input casted to the required data type
    """   
    
    # Ask user for an input
    
    # Check if user_input can be cast to type t
    try:
        user_input = input(str_input).strip(" ,")
        t(user_input)

    except ValueError:
        print ("\nThe value you have entered is incorrect. Please try again.\n")

        return input_validator(str_input, t)

    else:
        return (t(user_input))


def finance_calculators():
    
    """
    Function calculating total repay of investment or bond based on user input.
    """
    
    # Importing math module
    import math

    # First sentence to be displayed on the screen
    first_sentence = """\nChoose either 'investment' or 'bond' from the menu below to proceed:

    investment  -   to calculate the amount of interest you'll earn on your investment
    bond        -   to calculate the amount you'll have to pay on a home loan \n
    """

    # Asking the user for an input 
    # Transforming to lower case letters
    calculator = input(first_sentence).lower()

    # Checking if the input is valid
    if not (calculator == "investment" or calculator == "bond"):
        print("Your input is incorrect. Please try again.")
        finance_calculator()

    # Investment
    elif calculator == "investment":
        
        # User input:

        # 1 -> The amount of money the user wants to deposit
        deposit_str = "\nPlease enter the amount of money you want to deposit: \n"
        
        # Ask and check if deposit is valid
        deposit = input_validator(deposit_str, t = float)
        

        # 2 -> The interest rate
        interest_str = "\nPlease enter the interest rate in percents as number: \n"
        
        # Ask and check if interest_rate is valid
        interest_rate = input_validator(interest_str, t = float)
        
        # Interest rate in decimals
        interest_rate = interest_rate / 100


        # 3 -> Years of investement
        invest_str = "\nPlease enter how many year you want to keep your investment for: \n"

        # Ask and check if years of investment are valid
        invest_years = input_validator(invest_str, t = int)
        

        # 4 -> Kind of interest: single or compound -> lower case
        interest = input("\nPlease choose which interest you would like to proceed with (simple/compound): \n").lower()


        # Check if kind of interest is valid
        if not (interest == "simple" or interest == "compound"):
            print("\nThe value you have entered is incorrect. Please try again.\n")
            interest = input("\nPlease choose which interest you would like to proceed with (simple/compound): \n")

        # Calculating simple interest and displaying
        elif interest == "simple":
            total_amount_simple = deposit * (1 + interest_rate * invest_years)
            print(f'\nTotal amound that you will get in simple interest after {invest_years} year/s with interest rate {round(interest_rate, 2)} is {total_amount_simple:.2f}\n')
        
        # Calculating compound interest and displaying
        elif interest == "compound":
            total_amount_compound = deposit * math.pow((1 + interest_rate), invest_years)
            print(f'\nTotal amound that you will get in compound interest after {invest_years} year/s with interest rate {round(interest_rate, 2)} is {total_amount_compound:.2f}\n')

    # Bond
    elif calculator == "bond":

        # Ask the user:

        # The string to ask for present value of the house 
        value_str = "\nPlease enter the value of the house: \n"
          
        # Ask and check if value is valid
        value = input_validator(value_str, t = int)

        # The string to ask for interest rate
        interest_str = "\nWhat is the interest rate per year? (number of percents) \n"

        # Ask and check if interest rate is valid
        interest_rate = input_validator(interest_str, t = float)

        # Calculating monthly interest rate
        monthly_interest = interest_rate / 120

        # String to ask for a repay
        repay_str = "\nHow many months will the repay take? \n"

        # Ask and check if repay_time is valid
        repay_time = input_validator(repay_str, t = int)

        # Calculate the repay total
        repay_total = (monthly_interest * value) / (1 - math.pow((1 + monthly_interest), ((-1) * repay_time)))

        print(f'\nValue of the house: \t\t{value} \nInterest rate per month: \t{monthly_interest:.2f} \nRepay for month: \t\t{repay_total:.2f}\n')




finance_calculators()