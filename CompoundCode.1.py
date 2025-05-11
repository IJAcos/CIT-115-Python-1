# Compound Interest Calculator CIT-115 Python Prof. C

# Welcome
print("Welcome to the Savings Calculator!")

# Function to positive input
def get_positive_float(message, allow_zero=False):
    while True:
        try:
            value = float(input(message))
            if allow_zero and value >= 0:
                return value
            elif not allow_zero and value > 0:
                return value
            else:
                print("Error: Value must be positive." if not allow_zero else "Error: Value cannot be negative.")
        except:
            print("Error: Please enter a valid number.")

# Validation
fDeposit = get_positive_float("Enter starting money: ")
fInterestRate = get_positive_float("Enter yearly interest rate (example: 5 for 5%): ")
iMonths = int(get_positive_float("Enter number of months: "))
fGoal = get_positive_float("Enter your savings goal (0 if none): ", allow_zero=True)

# Monthly interest rates
fMonthlyInterest = (fInterestRate / 100) / 12

# Balance each month
fBalance = fDeposit
print("\nMonth-by-Month Savings:")

for iMonth in range(1, iMonths + 1):
    fBalance += fBalance * fMonthlyInterest
    print("Month", iMonth, ": $" + format(fBalance, ",.2f"))

# How many months to reach goal
if fGoal > 0:
    fBalanceGoal = fDeposit
    iMonthsCount = 0

    while fBalanceGoal < fGoal:
        fBalanceGoal += fBalanceGoal * fMonthlyInterest
        iMonthsCount += 1

    print("\nGoal reached in {:,} months!".format(iMonthsCount))
else:
    print("\nNo goal entered.")
