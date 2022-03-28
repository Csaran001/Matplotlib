import matplotlib.pyplot as plt

year = [1960, 1980, 2000, 2010, 2015, 2020]
population = {
    'Russia 14.41 crores ': [12, 14, 15, 16, 17, 18],
    'USA 32.95 crores': [19, 23, 28, 30, 32, 33],
    'China 140.21 crores': [67, 98, 125, 133, 137, 140],
    'India 138 crores': [46, 70, 105, 123, 131, 138],

}

plt.stackplot(year, population.values(), labels=population.keys() )
plt.legend(title="Countries",loc='upper left')
plt.title('World population 7.2 billion')
plt.xlabel('Year')
plt.ylabel('Number of people (Crore)')

plt.show()