# Input name 
sName = input("What is your name: ")

sWeight = input("What is your weight on Earth in pounds:  ")

nEarthWeight = float(sWeight)

MERCURY_Gravity = 0.38
VENUS_Gravity = 0.91
MOON_Gravity = 0.165
MARS_Gravity = 0.38
JUPITER_Gravity = 2.34
SATURN_Gravity = 0.93
URANUS_Gravity = 0.92
NEPTUNE_Gravity = 1.12
PLUTO_Gravity = 0.066

# Total Results
nMercury = nEarthWeight * MERCURY_Gravity
nVenus = nEarthWeight * VENUS_Gravity
nMoon = nEarthWeight * MOON_Gravity
nMars = nEarthWeight * MARS_Gravity
nJupiter = nEarthWeight * JUPITER_Gravity
nSaturn = nEarthWeight * SATURN_Gravity
nUranus = nEarthWeight * URANUS_Gravity
nNeptune = nEarthWeight * NEPTUNE_Gravity
nPluto = nEarthWeight * PLUTO_Gravity

print(sName + " these are your total weights on each planet: ")

print("Mercury:", nMercury)
print("Venus:", nVenus)
print("Moon:", nMoon)
print("Mars:", nMars)
print("Jupiter:", nJupiter)
print("Saturn:", nSaturn)
print("Uranus:", nUranus)
print("Neptune:", nNeptune)
print("Pluto:", nPluto)
