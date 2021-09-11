# An attempt to replicate planetary motion
import matplotlib.pyplot as plt
import numpy as np
a = np.zeros(3)
print(a)
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[a<5])
divisible_by_2 = a[a%2==0]
print(divisible_by_2)
print(a.sum())
# a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
# plt.plot(a)
# plt.show()

# x = np.linspace(0, 5, 20)
# y = np.linspace(0, 10, 20)
# plt.plot(x, y, 'purple') # line
# plt.plot(x, y, 'o')      # dots
# plt.show()

#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')
#X = np.arange(-5, 5, 0.15)
#Y = np.arange(-5, 5, 0.15)
#X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)

#ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')

#plt.show()

G = 6.674 * 10 ** -11


while m1.isdigit() == False:
    m1 = float(input('What is the mass of the first object in kilograms? '))
return int(m1)

while m2.isdigit() == False:
    m2 = float(input('What is the mass of the second object in kilograms? '))
return int(m2)

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

