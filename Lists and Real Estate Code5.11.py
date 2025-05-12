#  Lists and Real Estate Analyzer

# asks the user for a number and checks if it's valid.
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("That was not a number. Please try again.")

# This function finds the middle value from the list.
def getMedian(sales_list):
    count = len(sales_list)
    if count == 0:
        return 0.0
    middle = count // 2
    if count % 2 == 1:
        return sales_list[middle]  # If odd
    else:
        return (sales_list[middle - 1] + sales_list[middle]) / 2.0  # If even

# Main 
def main():
    sales = []

    # Ask for sales prices until user says no
    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        sales.append(fSalesPrice)

        while True:
            again = input("Enter another value Y or N: ").strip().lower()
            if again in ('y', 'n'):
                break
            else:
                print("Please enter Y for Yes or N for No.")

        if again == 'n':
            break

    # Sort the sales list
    sales.sort()

    print("\n--- Real Estate Sales Summary ---")
    print("Sales Entries:")
    for s in sales:
        print(f"  ${s:,.2f}")

    # Calculate results
    total = sum(sales)
    minimum = sales[0]
    maximum = sales[-1]
    average = total / len(sales)
    median = getMedian(sales)
    commission = total * 0.03

    # Results
    print(f"\nMinimum Sale: ${minimum:,.2f}")
    print(f"Maximum Sale: ${maximum:,.2f}")
    print(f"Total Sales: ${total:,.2f}")
    print(f"Average Sale: ${average:,.2f}")
    print(f"Median Sale: ${median:,.2f}")
    print(f"Commission (3%): ${commission:,.2f}")

    print("\n--- End of Report ---")

# Start the program
if __name__ == "__main__":
    main()
