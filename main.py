# An attempt to replicate planetary motion


G = 6.674 * 10 ** -11

m1 = float(input('What is the mass of the first object in kilograms? '))
m2 = float(input('What is the mass of the second object in kilograms? '))
r = float(input('What is the distance between the objects in metres? '))


def Gravitationalforce(m1, m2, r):
    Force = G * (m1 * m2) / r ** 2
    print('The gravitational force of attraction between the two bodies is {} Newtons.'.format(Force))
    return Force


Force = Gravitationalforce(m1, m2, r)
Acceleration1 = Force / m1
Acceleration2 = Force / m2
print('Mass 1 is accelerating towards Mass 2 at {} m/s2 and Mass 2 towards Mass 1 at {} m/s2'.format(Acceleration1,
                                                                                                     Acceleration2))
