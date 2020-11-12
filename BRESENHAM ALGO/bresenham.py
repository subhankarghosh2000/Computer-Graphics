import numpy as np
import matplotlib.pyplot as plt

def bresenham(x1,y1,x2,y2):
	X=[x1]
	Y=[y1]
	x,y=x1,y1
	dx=abs(x2-x1)
	dy=abs(y2-y1)
	p_y=2*dy-dx
	p_x=2*dx-dy
	if dx>dy:
		while x<x2:
			if p_y>=0:
				p_y=p_y+(2*dy)-(2*dx)
				y=y+1
				Y.append(y)
			else:
				p_y=p_y+(2*dy)
				Y.append(y)
			x=x+1
			X.append(x)
	else:
		while y<y2:
			if p_x>=0:
				p_x=p_x+(2*dx)-(2*dy)
				x=x+1
				X.append(x)
			else:
				p_x=p_x+(2*dx)
				X.append(x)
			y=y+1
			Y.append(y)
	for i in range(len(X)):
		print('x = ', X[i],'y = ', Y[i])
	plt.scatter(X,Y)
	plt.plot(X,Y)
	plt.show()

x1=int(input("Enter x coordinate of starting point : "))
y1=int(input("Enter y coordinate of starting point : "))
x2=int(input("Enter x coordinate of ending point   : "))
y2=int(input("Enter y coordinate of ending point   : "))

bresenham(x1,y1,x2,y2)




			