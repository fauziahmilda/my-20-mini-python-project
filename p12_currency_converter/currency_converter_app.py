def main():
    print("This program convert US dollars to Pounds Sterling")
    print("")

    dollars = eval(input("Enter amount in dollars: "))

    pounds = convert_to_pounds(dollars)

    print(f"That is {pounds} pounds.")


def convert_to_pounds(dollars): return dollars * 0.82


main()
