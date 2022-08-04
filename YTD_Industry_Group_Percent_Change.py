import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csvFile = pd.read_csv('197.csv')

percent_change = csvFile['% Chg YTD']
name = csvFile['Name']
symbol = csvFile['Symbol']
rank = csvFile['Ind Group Rank']
market_cap = csvFile['Ind Mkt Val (bil)']

df = pd.DataFrame(csvFile)
df.index.name = "Index"

df.columns.name = df.index.name
df.index.name = None

print(df)

fig = plt.figure(figsize=(15,8))
ax = sns.barplot(name,percent_change)
plt.xticks(rotation=90)
_, xlabels = plt.xticks()
ax.set_xticklabels(xlabels, size=3.5)
ax.xaxis.set_tick_params(labelsize=3.5)
plt.title("YTD Industry Group Percent Change",size=12)
plt.xlabel("Industry Group Name",size=12)
plt.ylabel("YTD Percent Change",size=12)
plt.tight_layout()
plt.show()
