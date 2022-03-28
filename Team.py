import matplotlib.pyplot as plt

m1 = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20]

m2 = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10]

days=["day 1","day 2","day 3","day 4","day 5","day 6","day 7","day 8","day 9","day 10",]

m3 = [26, 29, 48, 64, 6, 5, 36, 66, 72, 40]

m4= [26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

plt.scatter(m1, m2, c ="pink", linewidths = 2, marker ="o", edgecolor ="green", s = 50,label='Team A')
 
plt.scatter(m3, m4, c ="yellow",linewidths = 2, marker ="^", edgecolor ="red", s = 200,label='Team B')

d=plt.subplot()

d.set_xticklabels(days)

plt.xlabel("days")
plt.ylabel("Score")
plt.title("Team Score")
plt.legend()
plt.show()
