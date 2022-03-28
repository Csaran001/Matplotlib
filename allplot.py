import matplotlib.pyplot as plt
import numpy as np


# subplot
s1 = plt.subplot(221)
s2 = plt.subplot(222)
s3 = plt.subplot(223)
s4 = plt.subplot(224)

# plot 1
x1 = [7, 14, 21, 28, 35, 42, 49]
y1 = [5, 12, 10, 12, 13, 12, 10]
z1 = [3, 5, 1, 2, 5, 4, 3]

values = ["March 5", "March 6", "March 7", "March 8", "March 9", "March 10", "March 11"]

s1.plot(x1, y1, label="Follow")
s1.set_xticks(x1, values)
s1.set_xlabel("Days")
s1.set_ylabel("Followers Count")
s1.set_title("Insta Insights")


s1.plot(x1, z1, label="Unfollow")
s1.legend(title="Insta Followers")


# bar Chart 2

barWidth = 0.25

IT = [12, 30, 1, 8, 22]
ECE = [28, 6, 16, 5, 10]
CSE = [29, 3, 24, 25, 17]

br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

s2.bar(br1, IT, color='r', width=barWidth, edgecolor='grey', label='IT')
s2.bar(br2, ECE, color='g', width=barWidth, edgecolor='grey', label='ECE')
s2.bar(br3, CSE, color='b', width=barWidth, edgecolor='grey', label='CSE')

s2.set_xlabel('Branch', fontweight='bold', fontsize=8)
s2.set_ylabel('Students passed', fontweight='bold', fontsize=8)
s2.set_xticks([r + barWidth for r in range(len(IT))], ['2018', '2019', '2020', '2021', '2022'])

s2.set_title("Department")
s2.legend()



# bar Chart 3
x5 = ['2019', '2020', '2021', '2022']
yy1 = np.array([10, 20, 10, 30])
yy2 = np.array([20, 25, 15, 25])
yy3 = np.array([12, 15, 19, 6])
yy4 = np.array([10, 29, 13, 19])

w2 = 0.2

s3.bar(x5, yy1, color='r', width=w2, label="Mystery")
s3.bar(x5, yy2, bottom=yy1, color='b', width=w2, label="Sci-Fi")
s3.bar(x5, yy3, bottom=yy1+yy2, color='y', width=w2, label="Fantasy")
s3.bar(x5, yy4, bottom=yy1+yy2+yy3, color='g', width=w2, label="Comics")

s3.set_yticklabels(['10k', '20k', '30k', '40k', '50k', '60k'])

s3.set_xlabel("Books")
s3.set_ylabel("Total Count")
s3.legend(["Mystery", "Sci-Fi", "Fantasy", "Comics"])
s3.set_title("Book Sales")


# Pie Chart4
p = np.array([35, 25, 25, 15])
l = ['AUDI 35%', 'BMW 25%', 'FORD 25%', 'TESLA 15%']
e = [0.2, 0, 0, 0]
s4.pie(p, labels=l, startangle=90, explode=e, shadow=True)
s4.legend(prop={'size': 8}, title='car', loc='upper left')
s4.set_title("Car Sales")

plt.tight_layout()
plt.show()