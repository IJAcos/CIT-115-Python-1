# Grade Analyzer for Prof.C 

# Ask student's name
sName = input("Student's name: ")

# Ask for 4 test scores
iTest1 = int(input("Test score 1: "))
iTest2 = int(input("Test score 2: "))
iTest3 = int(input("Test score 3: "))
iTest4 = int(input("Test score 4: "))

# Ask if we should drop the lowest grade
sDrop = input("Drop the lowest grade? (Y or N): ").upper()

# Stop if any score is below 0
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0.")
    exit()

# Stop if the user types anything other than Y or N
if sDrop != "Y" and sDrop != "N":
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

# Total score and how many tests to average
if sDrop == "Y":
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        total = iTest2 + iTest3 + iTest4
    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        total = iTest1 + iTest3 + iTest4
    elif iTest3 <= iTest1 and iTest3 <= iTest2 and iTest3 <= iTest4:
        total = iTest1 + iTest2 + iTest4
    else:
        total = iTest1 + iTest2 + iTest3
    count = 3
else:
    total = iTest1 + iTest2 + iTest3 + iTest4
    count = 4

# Calculate average
fAverage = total / count

# The letter grade
if fAverage >= 97:
    grade = "A+"
elif fAverage >= 94:
    grade = "A"
elif fAverage >= 90:
    grade = "A-"
elif fAverage >= 87:
    grade = "B+"
elif fAverage >= 84:
    grade = "B"
elif fAverage >= 80:
    grade = "B-"
elif fAverage >= 77:
    grade = "C+"
elif fAverage >= 74:
    grade = "C"
elif fAverage >= 70:
    grade = "C-"
elif fAverage >= 67:
    grade = "D+"
elif fAverage >= 64:
    grade = "D"
elif fAverage >= 60:
    grade = "D-"
else:
    grade = "F"

# Show the results
print("\nGrade Report")
print("-------------")
print("Name:", sName)
print("Average:", format(fAverage, ".1f"))
print("Grade:", grade)
