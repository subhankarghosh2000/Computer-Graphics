import numpy as np
import matplotlib.pyplot as plt

def round_of(c):
	return int(c+0.5)

def digital_differential_algo(x1,y1,x2,y2):
	X=[x1]
	Y=[y1]
	x,y=x1,y1
	dx=abs(x2-x1)
	dy=abs(y2-y1)
	if dx>dy:
		length=dx
	else:
		length=dy
	if dx>dy:
		x_inc=1
		y_inc=dy/dx
	else:
		x_inc=dx/dy
		y_inc=1
	for i in range(1,length+1):
		x+= x_inc
		y+= y_inc
		plt.plot(round_of(x),round_of(y),'-ro')
		print('x = ', round_of(x),'y = ', round_of(y))
		X.append(X[i-1]+x_inc)
		Y.append(Y[i-1]+y_inc)
	X = list(map(round, X))
	Y = list(map(round, Y))
	plt.plot(X,Y)
	plt.show()

x1=int(input("Enter x coordinate of starting point : "))
y1=int(input("Enter y coordinate of starting point : "))
x2=int(input("Enter x coordinate of ending point   : "))
y2=int(input("Enter y coordinate of ending point   : "))

digital_differential_algo(x1,y1,x2,y2)