# An attempt to replicate planetary motion


G = 6.674 * 10 ** -11

m1 = float(input('What is the mass of the first object in kilograms? '))
m2 = float(input('What is the mass of the second object in kilograms? '))
M = m1*m2
r1 = [1,2,3,4,5,6,7,8,9,10]

#Calculate gravitational force.
def Gravitationalforce(m1, m2, r):
    Force = G * (m1 * m2) / r ** 2
    print('The gravitational force of attraction between the two bodies is {} Newtons.'.format(Force))
    return Force

def Gravitationalforce1(r):
    Force1 = round(G * M / r**2,2)
    return Force1

newforce = map(Gravitationalforce1,r1)
newforce = list(newforce)
print(newforce)
x = 0
for i in newforce:
    print('The force at {} metres is {} Newtons'.format(r1[x],i))
    x += 1