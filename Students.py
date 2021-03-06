import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25

IT = [40, 30, 36, 55, 32]
ECE = [28, 19, 40, 15, 20]
CSE = [29, 38, 47, 35, 60]

ax = plt.subplot()

br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]


b1 = ax.bar(br1, IT, width = barWidth, label ='IT')
b2 = ax.bar(br2, ECE, width = barWidth, label ='ECE')
b3 = ax.bar(br3, CSE, width = barWidth,label ='CSE')

ax.bar_label(b1)
ax.bar_label(b2)
ax.bar_label(b3)

plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
plt.ylabel('Number of Students passed', fontweight='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(IT))],['2017', '2018', '2019', '2020', '2022'])

plt.legend(title="Department")
plt.show()
