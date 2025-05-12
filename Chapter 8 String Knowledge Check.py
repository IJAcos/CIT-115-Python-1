# Chapter 8 - String Methods Demonstration

# 1: 
sQuote = "Python is a great programming language"
print("1. sQuote[2:]:", sQuote[2:])  # Output: thon is a great programming language

# 2: 
print("2. sQuote[2:5]:", sQuote[2:5])  # Output: tho

# 3: 
print("3. sQuote.isupper():", sQuote.isupper())  # Output: False

# 4: 
print("4. len(sQuote):", len(sQuote))  # Output: 39

# 5:
print("5. sQuote.upper():", sQuote.upper())  # Output: PYTHON IS A GREAT PROGRAMMING LANGUAGE

# 6:
print("6. sQuote.lower():", sQuote.lower())  # Output: python is a great programming language

# 7:
print("7. sQuote.index('great'):", sQuote.index("great"))  # Output: 12

# 8: 
print("8. sQuote[8]:", sQuote[8])  # Output: s

# 9:
print("9. sQuote.find('Dan'):", sQuote.find("Dan"))  # Output: -1

# 10:
print("10. sQuote == 'Brian':", sQuote == "Brian")  # Output: False

# 11:
print("11. sQuote.replace('a','@'):", sQuote.replace("a", "@"))  # Output: Python is @ gre@t progr@mming l@ngu@ge

# 12:
print("12. sQuote == 'Python':", sQuote == "Python")  # Output: False

# 13:
print("13. sQuote.lower().endswith('Age'):", sQuote.lower().endswith('Age'))  # Output: False

# 14:
sResult = sQuote[:9]
print("14. sQuote[:9]:", sResult)  # Output: Python is

# 15:
print("15. sQuote.rfind('a'):", sQuote.rfind('a'))  # Output: 36

# 16:
sQuote2 = "Python"
print("16. sQuote2[::-1]:", sQuote2[::-1])  # Output: nohtyP

# 17:
print("17. sQuote2 + 'is awesome!':", sQuote2 + "is awesome!")  # Output: Pythonis awesome!

# 18:
print("18. sQuote2[-4:]:", sQuote2[-4:])  # Output: thon

# 19:
print("19. sQuote2[-4:-2]:", sQuote2[-4:-2])  # Output: th

# 20:
sQuote3 = "-->Python<--"
print("20. sQuote3.strip('-'):", sQuote3.strip('-'))  # Output: >Python<
