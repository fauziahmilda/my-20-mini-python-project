# collect the necessary input: principal (loan amount), apr (annual interest rate), years
# calculate the monthly payment
# show to the user

def main():
    print("This is a monthly payment loan calculator \n")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the anual interest rate: "))
    years = int(input("Input amount of years: "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / \
        (1-(1 + monthly_interest_rate) ** (-amount_of_months))

    print(f"The monthly payment for this loan is: {monthly_payment}")


main()
