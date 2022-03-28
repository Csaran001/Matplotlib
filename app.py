import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25

Insta = [4, 3, 6, 4, 3]
WhatsApp = [8, 4, 4, 5, 2]
Netflix = [6, 8, 7, 4, 6]

ax = plt.subplot()

br1 = np.arange(len(Insta))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]


b1 = ax.bar(br1, Insta, width = barWidth, label ='Insta',color='orange')
b2 = ax.bar(br2, WhatsApp, width = barWidth, label ='WhatsApp',color='g')
b3 = ax.bar(br3, Netflix, width = barWidth,label ='Netflix',color='r')

ax.bar_label(b1)
ax.bar_label(b2)
ax.bar_label(b3)

ax.set_ylim([0,15])

plt.xlabel('Days', fontsize = 15)
plt.ylabel('Number of Hours', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Insta))],['March 8', 'March 9', 'March 10', 'March 11', 'March 12'])

plt.legend(title="Apps")
plt.show()
