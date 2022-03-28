import numpy as np
import matplotlib.pyplot as plt


x5 = ['2019', '2020', '2021', '2022']
yy1 = np.array([10, 20, 10, 30])
yy2 = np.array([20, 25, 15, 25])
yy3 = np.array([12, 15, 19, 6])
yy4 = np.array([10, 29, 13, 19])

w2=0.2

ay=plt.subplot()

b1=ay.bar(x5, yy1, width=w2, label="Mystery")
b2=ay.bar(x5, yy2, bottom=yy1, width=w2, label="Sci-Fi")
b3=ay.bar(x5, yy3, bottom=yy1+yy2, width=w2, label="Fantasy")
b4=ay.bar(x5, yy4, bottom=yy1+yy2+yy3, width=w2, label="Comics" )

ay.bar_label(b1, label_type="center")
ay.bar_label(b2, label_type="center")
ay.bar_label(b3, label_type="center")
ay.bar_label(b4, label_type="center")


ay.set_yticklabels(['10k','20k','30k','40k','50k','60k'])

plt.xlabel("Books")
plt.ylabel("Total Count")
plt.legend()
plt.title("Books Sales")
plt.show()
