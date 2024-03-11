import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 3, 1]

y = [1, 2, 2, 1, 1]

plt.plot(x , y , linewidth = 8 , marker ="D", markersize = 10, color = "g")
plt.axis([0.0, 4.0, 0.0, 4.0])
plt.xlabel('x-os')
plt.ylabel('y-os')
plt.title('Zadatak 1')
plt.show()