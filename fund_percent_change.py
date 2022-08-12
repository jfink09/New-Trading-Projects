import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csvFile = pd.read_csv('ibd50.csv')

fund_change = csvFile["Funds % Increase"]

csvFile = pd.DataFrame(csvFile)
print(csvFile)

symbol = csvFile['Symbol']

fig = plt.figure(figsize = (15,8))

color = ['#ff0000' if fund_change<0 else '#00ff00' for fund_change in fund_change]
ax = sns.barplot(x=symbol, y=fund_change, palette=color)
plt.xticks(rotation=90)
_, xlabels = plt.xticks()
ax.set_xticklabels(xlabels, size=12,color='#ffffff')
ax.xaxis.set_tick_params(labelsize=12,color='#ffffff')
plt.title("Fund Percent Change Since Last Quarter For Stocks In IBD 50",size=16,color='#ffffff')
plt.xlabel("Stock Ticker Symbol",size=16,color='#ffffff')
plt.ylabel("Fund Percent Change",size=16,color='#ffffff')

ax.set_facecolor('#0b0b0c')
fig.patch.set_facecolor('#0b0b0c')

ax.spines['left'].set_color('#ffffff')
ax.spines['top'].set_color('#ffffff')
ax.spines['right'].set_color('#ffffff')
ax.spines['bottom'].set_color('#ffffff')

ax.tick_params(axis='y', colors='#ffffff', size=12)

fig.set_tight_layout(True)
plt.show()
