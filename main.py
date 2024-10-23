def getDeposit():
    while True:
        deposit = input("Please enter your deposit amount: $")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                if deposit > 7500:
                    print("You do NOT have that much money lil bro 🤣")
                else:
                    return deposit  # Return deposit and exit the loop when valid
            else:
                print("Deposit must be greater than zero!!!")
        else:
            print("Please enter a valid number...")

def main():
    deposit = getDeposit()
    print(f"Your current balance is: ${deposit}")

main()
