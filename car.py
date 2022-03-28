import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,25,25,15])
l=['AUDI 35%', 'BMW 25%', 'FORD 25%','TESLA 15%']
e=[0.2,0,0,0]
plt.pie(y,labels=l,startangle=90,explode=e,shadow=True)
plt.legend(title="car",loc='lower right',bbox_to_anchor =(1, 0, 0.5, 1))

plt.title("Car Sales")
plt.show()