import math

# Paint Job with Functions CIT 115- Prof C

# Function to get valid float input
def get_float(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num > 0:
                return num
            else:
                print("Enter a number greater than 0.")
        except:
            print("Invalid input. Try again.")

def main():
    print("Paint Job Estimator")

    sqft = get_float("Wall square footage: ")
    price = get_float("Paint price per gallon: ")
    coverage = get_float("Coverage per gallon (sq ft): ")
    hours_per_gal = get_float("Labor hours per gallon: ")
    labor_rate = get_float("Labor charge per hour: ")

    gallons = math.ceil(sqft / coverage)
    paint_cost = gallons * price
    labor_hours = gallons * hours_per_gal
    labor_cost = labor_hours * labor_rate
    total_cost = paint_cost + labor_cost

    print("\n--- Estimate ---")
    print(f"Gallons: {gallons}")
    print(f"Paint Cost: ${paint_cost:.2f}")
    print(f"Labor Cost: ${labor_cost:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

main()
