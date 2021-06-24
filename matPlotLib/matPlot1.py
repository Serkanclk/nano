import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [3,7,4,8,9]
plt.grid(True) # arkaplanda grid
plt.xlabel("X val") # x title
plt.ylabel("Y val") # y title
plt.title("Test title") # title
plt.axis([0,5,0,9])# sınırlama
plt.plot(x,y, label="Grafik 1")
plt.legend() # labelin konumu
#plt.plt(x,y,'-*')
# buarda * noktalı gösterim için 
# - aralara çizgi çekmek için 
# ya da renk yazılabilir.
plt.show()