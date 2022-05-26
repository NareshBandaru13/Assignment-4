import numpy as np
import matplotlib.pyplot as plt

xlist = [-1,0,0,1,1,3]
ylist = [0,0,0.7,0.7,1,1]
plt.plot(xlist,ylist)

plt.plot(1,0,marker="o",markeredgecolor="red",markerfacecolor="green")
plt.plot(0,1,marker="o",markeredgecolor="red",markerfacecolor="green")
plt.plot(0,0.7,marker="o",markeredgecolor="red",markerfacecolor="green")


plt.text(1,0,'1')
plt.text(0,1,'1')
plt.text(0,0.7,'q')

plt.xlabel('x',fontsize=13)
plt.ylabel('F(x)',fontsize=13)
plt.grid()

plt.show()