import matplotlib.pyplot as plt


x = [7, 14, 21, 28, 35, 42, 49]
y = [40, 43, 47, 45, 50, 54, 60]
z = [5,7, 4, 6, 9, 10, 7]
values=["March 5","March 6","March 7","March 8","March 9","March 10","March 11",]

plt.plot(x, y,label="Follow")
plt.xticks(x,values)
plt.xlabel("Days")
plt.ylabel("Followers Count")
plt.title("Insights")

plt.plot(x, z,label="Unfollow")

plt.legend(title="Insta Followers")

plt.show()