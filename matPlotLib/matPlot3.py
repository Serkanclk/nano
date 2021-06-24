import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
y2 = np.cos(x)
plt.grid(True) # arkaplanda grid
plt.xlabel("X val") # x title
plt.ylabel("Y val") # y title
plt.title("Test title") # title

plt.plot(x,y,'b', label="Grafik 1")
plt.plot(x,y2,'r', label="Grafik 1")

plt.legend() # labelin konumu
#plt.plt(x,y,'-*')
# buarda * noktalı gösterim için 
# - aralara çizgi çekmek için 
# ya da renk yazılabilir.
plt.show()