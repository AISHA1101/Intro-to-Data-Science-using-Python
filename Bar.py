from collections import Counter
import matplotlib.pyplot as plt

nos = [16,30,52,9,35,8]
brand = ['Oppo','Asus','Redmi','Iphone','Samsung','oneplus']

plt.bar(range(len(nos)),nos)
plt.xticks(range(len(nos)),brand)

plt.show()