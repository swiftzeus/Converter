#An attempt to replicate planetary motion


G = 6.674 * 10**-11

m1 = float(input('What is the mass of the first object in kilograms? '))
m2 = float(input('What is the mass of the second object in kilograms? '))
r = float(input('What is the distance between the objects in metres? '))

Force = G * (m1 * m2)/r**2
print(Force)