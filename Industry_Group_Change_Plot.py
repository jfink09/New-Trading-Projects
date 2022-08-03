import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csvFile = pd.read_csv('groups.csv')

lastweek_rank = csvFile['Ind Grp Rnk Last Week']
thisweek_rank = csvFile['Ind Group Rank']

new_rank = lastweek_rank - thisweek_rank

new_rank.columns =['Ind Group', 'Change']

csvFile = pd.DataFrame(csvFile)
csvFile['Change'] = new_rank
print(csvFile)

name = csvFile['Name']
change = csvFile['Change']

fig = plt.figure(figsize = (15,8))
color = ['r' if change<0 else 'g' for change in change]
ax = sns.barplot(x=name, y=change, palette=color)
plt.xticks(rotation=90)
_, xlabels = plt.xticks()
ax.set_xticklabels(xlabels, size=3.5)
ax.xaxis.set_tick_params(labelsize=3.5)
plt.title("Industry Group Rank Change (Last To Current Rank)",size=12)
plt.xlabel("Industry Group Name",size=12)
plt.ylabel("Change In Industry Group Rank",size=12)
fig.set_tight_layout(True)
plt.show()
