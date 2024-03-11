import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv", delimiter=',', skiprows=1)

#a)
rows, cols = np.shape(data)
print(str(rows)," people were measured.")   

#b)
height = data[:,1]
weight = data[:,2]

plt.scatter(height, weight,color="turquoise", s=1)
plt.xlabel("Height [cm]")
plt.ylabel("Weight [kg]")
plt.title("Height to weight ratio")
plt.show()

#c)
height50 = height[::50]
weight50 = weight[::50]

plt.scatter(height50, weight50,color="turquoise")
plt.xlabel("Height [cm]")
plt.ylabel("Weight [kg]")
plt.title("Height to weight ratio of every 50th person")
plt.show()

#d)
print("Min height: ", str(np.min(height)))
print("Max height: ", str(np.max(height)))
print("Average height: ", str(np.mean(height)))

#e)
men=data[np.where(data[:,0]==1)]
women=data[np.where(data[:,0]==0)]

print("Min male height: ", str(np.min(men[:,1])))
print("Max male height: ", str(np.max(men[:,1])))
print("Average male height: ", str(np.mean(men[:,1])))

print("Min female height: ", str(np.min(women[:,1])))
print("Max female height: ", str(np.max(women[:,1])))
print("Average female height: ", str(np.mean(women[:,1])))