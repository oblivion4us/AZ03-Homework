import pandas as pd
import matplotlib.pyplot as plt

file_path = 'processed_prices.csv'
data = pd.read_csv(file_path)

prices = data['Price']

plt.hist(prices, bins=20, edgecolor='black')

plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

plt.show()